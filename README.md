# haiku_generator

Simple haiku generator written in Python. Validates haiku syllable count and generates random haikus from a corpus of words.

## Favorite randomly generated haiku
**This**
> overestimates  
> mouths incontrovertible  
> equivalency  

**or this**
> edna liturgy  
> afterlives abdicated  
> taunts justifying  

**okay, last one**
> inexperienced  
> felucca tarts remarriage  
> prescribed bengali  

## Setup
* Minimum requirements
  * [Python 3.11](https://www.python.org/downloads/)
* Recommended
  * [asdf](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf)
  * [poetry](https://python-poetry.org/docs/)
  * [docker-compose](https://docs.docker.com/compose/install/)

## Quickstart
```bash
# vanilla python
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python haiku_generator.py

# asdf
asdf install python 3.11.5
asdf install poetry latest

# poetry
poetry install
poetry run python haiku_generator.py
```

## Docker
* Use the Docker image instead of installing locally
```bash
# by default, entrypoint is the script, command (option) is `--help`
λ docker run -it --rm ghcr.io/pythoninthegrass/haiku_generator:main

 Usage: haiku_generator.py [OPTIONS]

╭─ Options ────────────────────────────────────────────────────────────╮
│ --validate  -v        Validate a haiku                               │
│ --generate  -g        Generate a haiku                               │
│ --help                Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────╯

# override command (option) with `--validate` or `-v`
λ docker run -it --rm ghcr.io/pythoninthegrass/haiku_generator:main -v
Downloading words_dictionary.json...
Downloading cmudict...
[nltk_data] Downloading package cmudict to /app/nltk_data...
[nltk_data]   Unzipping corpora/cmudict.zip.
Validating haiku...
Enter the first line: <ctrl-c>

# override command (option) with `--generate` or `-g`
λ docker run -it --rm ghcr.io/pythoninthegrass/haiku_generator:main -g
Downloading words_dictionary.json...
Downloading cmudict...
[nltk_data] Downloading package cmudict to /app/nltk_data...
[nltk_data]   Unzipping corpora/cmudict.zip.
Generating haiku...
extenuating
anesthesiologists
insubordinate

# override entrypoint with `bash` and run the script from within the container
λ docker run -it --rm --entrypoint=bash ghcr.io/pythoninthegrass/haiku_generator:main
appuser@1d5cc39be76d:/app$ ll
total 80
drwxr-xr-x 1 appuser appuser   126 Oct 17 01:58 .
drwxr-xr-x 1 root    root        0 Oct 17 02:06 ..
-rwxr-xr-x 1 appuser appuser  6536 Oct 17 01:57 haiku_generator.py
-rw-r--r-- 1 appuser appuser 64245 Oct 17 01:57 poetry.lock
-rw-r--r-- 1 appuser appuser  2030 Oct 17 01:57 pyproject.toml
-rw-r--r-- 1 appuser appuser  2302 Oct 17 01:57 requirements.txt
drwxr-xr-x 1 appuser appuser   230 Oct 17 01:57 test
appuser@1d5cc39be76d:/app$ ./haiku_generator.py --help

 Usage: haiku_generator.py [OPTIONS]

╭─ Options ────────────────────────────────────────────────────────────╮
│ --validate  -v        Validate a haiku                               │
│ --generate  -g        Generate a haiku                               │
│ --help                Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────╯

# run without any options
λ docker run -it --rm --entrypoint=bash ghcr.io/pythoninthegrass/haiku_generator:main
appuser@b1aff86b728f:/app$ ./haiku_generator.py
Downloading words_dictionary.json...
Downloading cmudict...
[nltk_data] Downloading package cmudict to /app/nltk_data...
[nltk_data]   Unzipping corpora/cmudict.zip.
Welcome to the Haiku Generator!

Would you like to validate or generate a haiku?

1. validate
2. generate
3. exit

Please enter a number: 3
Goodbye!

# exit the container
appuser@1d5cc39be76d:/app$ exit
exit
```

## Development
* Testing
    ```bash
    # activate virtual environment
    poetry shell
    
    # generate tests
    hypothesis write haiku_generator.validate_haiku > test_validate_haiku.py

    # run specific test
    pytest -k test_validate_haiku
    ```

## TODO
* [Open Issues](https://github.com/pythoninthegrass/haiku_generator/issues)
* Generate more human-esque poems lmao
* CI
  * Auto format (e.g., pep8)
  * Re-add devcontainer
    * Use `docker.yml` to build image
* Write more tests
  * properties based ([hypothesis](https://youtu.be/mkgd9iOiICc?si=3Fpk7s7RvZZQtWB0&t=1120))
  * unit
  * integration
* QA
  * 479K word json file
    * json vs. sqlite vs. something else (parquet?)
* GUI

## Further Reading
[How to Write a Haiku, With Examples | Grammarly Blog](https://www.grammarly.com/blog/how-to-write-haiku/)

[NLTK :: nltk.corpus.reader.cmudict](https://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html)

[dwyl/english-words: :memo: A text file containing 479k English words for all your dictionary/word-based projects e.g: auto-completion / autosuggestion](https://github.com/dwyl/english-words)

[Typer](https://typer.tiangolo.com)

[What you can generate and how — Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/data.html#)

[Publishing Docker images - GitHub Docs](https://docs.github.com/en/actions/publishing-packages/publishing-docker-images#publishing-images-to-github-packages)
