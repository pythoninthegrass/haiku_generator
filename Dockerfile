# syntax=docker/dockerfile:1.6

# full semver just for python base image
ARG PYTHON_VERSION=3.11.6

FROM python:${PYTHON_VERSION}-slim-bullseye AS builder

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

# update apt repos and install dependencies
RUN apt -qq update && apt -qq install \
    --no-install-recommends -y \
    curl \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# pip env vars
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# poetry env vars
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION=1.6.1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1

# path
ENV VENV="/opt/venv"
ENV PATH="$POETRY_HOME/bin:$VENV/bin:$PATH"

COPY requirements.txt requirements.txt

RUN python -m venv $VENV \
    && . "${VENV}/bin/activate"\
    && python -m pip install "poetry==${POETRY_VERSION}" \
    && python -m pip install -r requirements.txt

FROM python:${PYTHON_VERSION}-slim-bullseye AS runner

# setup standard non-root user for use downstream
ENV USER_NAME=appuser
ENV USER_GROUP=appuser
ENV HOME="/home/${USER_NAME}"
ENV HOSTNAME="${HOST:-localhost}"
ENV VENV="/opt/venv"

ENV PATH="${VENV}/bin:${VENV}/lib/python${PYTHON_VERSION}/site-packages:/usr/local/bin:${HOME}/.local/bin:/bin:/usr/bin:/usr/share/doc:$PATH"

# standardise on locale, don't generate .pyc, enable tracebacks on seg faults
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# workers per core
# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/blob/master/README.md#web_concurrency
ENV WEB_CONCURRENCY=2

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies
RUN apt -qq update && apt -qq install \
    --no-install-recommends -y \
    bat \
    curl \
    dpkg \
    git \
    iputils-ping \
    less \
    lsof \
    make \
    p7zip \
    perl \
    shellcheck \
    tldr \
    tree \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd $USER_NAME \
    && useradd -m $USER_NAME -g $USER_GROUP

COPY --from=builder --chown=${USER_NAME}:${USER_GROUP} $VENV $VENV

USER $USER_NAME

# qol: .bashrc
RUN tee -a $HOME/.bashrc <<EOF
# shared history
HISTFILE=/var/tmp/.bash_history
HISTFILESIZE=100
HISTSIZE=100

stty -ixon

# aliases
alias ..='cd ../'
alias ...='cd ../../'
alias ll='ls -la --color=auto'
EOF

WORKDIR /app

COPY --chown=${USER_NAME}:${USER_GROUP} . .

# $PATH
ENV PATH=$VENV_PATH/bin:$HOME/.local/bin:$PATH

# port needed by app
EXPOSE 8000

# CMD ["sleep", "infinity"]

ENTRYPOINT [ "/app/haiku_generator.py" ]
CMD [ "--help" ]
