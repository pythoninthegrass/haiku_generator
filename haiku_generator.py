#!/usr/bin/env python3

import httpx
import json
import nltk
import os
import random
import string
import typer
from pathlib import Path
from nltk.corpus import cmudict
from textwrap import dedent
from typing import Annotated

app = typer.Typer()

# TODO: setup short circuit if no internet connection

# setup httpx client
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0"
}
client = httpx.Client()

# download english-words/words_dictionary.json
if not Path("./words_dictionary.json").is_file():
    typer.echo("Downloading words_dictionary.json...")
    raw_json = client.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json", headers=headers)
    with open("./words_dictionary.json", "w") as f:
        json.dump(raw_json.json(), f)

# download cmudict
base_dir = Path("./nltk_data")
file_path = Path(f"{base_dir}/corpora/cmudict")
if not Path(file_path).exists():
    typer.echo("Downloading cmudict...")
    nltk.download("cmudict", download_dir=base_dir)
    Path(f"{base_dir}/corpora/cmudict.zip").unlink()

# set cmudict path
nltk_data_path = str(Path(base_dir).resolve())
nltk.data.path.append(nltk_data_path)

# load cmudict
d = cmudict.dict()


def syllables_in_word(word):
    """Count syllables in a word"""
    count = 0
    if word.lower() not in d:
        return None
    phones = d[word.lower()]
    if phones is None:
        return None
    else:
        for phone in phones[0]:
            if phone[-1].isdigit():
                count += 1
        return count


def syllables_in_line(line):
    """Estimate syllables in a line"""
    # split lines into words
    try:
        words = line.split()
    except AttributeError:
        return None

    # remove punctuation
    regular_punc = list(string.punctuation)
    special_punc = ["—", "<", ">"]
    punc = regular_punc + special_punc
    words = [word.strip("".join(punc)) for word in words]

    # remove empty strings
    words = [word for word in words if word]

    # count syllables in each word
    syllables = [syllables_in_word(word) for word in words]
    if None in syllables:
        return None
    else:
        return sum(syllables)


def validate_haiku(first_line=None, second_line=None, third_line=None):
    """Validate a haiku"""
    first_line_syllables = syllables_in_line(first_line)
    second_line_syllables = syllables_in_line(second_line)
    third_line_syllables = syllables_in_line(third_line)

    # strip whitespace
    first_line = first_line.strip()
    second_line = second_line.strip()
    third_line = third_line.strip()

    match (first_line_syllables, second_line_syllables, third_line_syllables):
        case (5, 7, 5):
            print("This is a haiku!")
            print(f"{first_line}\n{second_line}\n{third_line}")
        case (5, 7, _):
            print(f"This is not a traditional haiku. The third line has {third_line_syllables} syllables.")
        case (5, _, 5):
            print(f"This is not a traditional haiku. The second line has {second_line_syllables} syllables.")
        case (_, 7, 5):
            print(f"This is not a traditional haiku. The first line has {first_line_syllables} syllables.")
        case (_, _, _):
            print(dedent(
                f"""\
                This is not a traditional haiku.
                The first line has {first_line_syllables} syllables.
                The second line has {second_line_syllables} syllables.
                The third line has {third_line_syllables} syllables.
                """))


def generate_line(words, syllables):
    """Generate a line with the given number of syllables"""
    line = ""
    while syllables_in_line(line) != syllables:
        rng_key = random.randint(1, 10)
        line = " ".join(random.choices(words, k=rng_key))
    return line


def generate_haiku():
    """Generate a haiku"""
    with open("./words_dictionary.json") as f:
        words_dictionary = json.load(f)

    words = list(words_dictionary.keys())

    first_line = generate_line(words, 5)
    second_line = generate_line(words, 7)
    third_line = generate_line(words, 5)

    print(f"{first_line}\n{second_line}\n{third_line}")


def main(
    validate: Annotated[bool, "validate"] = typer.Option(False,
                                                         "-v", "--validate",
                                                         help="Validate a haiku"),
    generate: Annotated[bool, "generate"] = typer.Option(False,
                                                         "-g", "--generate",
                                                         help="Generate a haiku"),
):
    typer_prompt = """\
    Welcome to the Haiku Generator!

    Would you like to validate or generate a haiku?

    1. validate
    2. generate
    3. exit

    Please enter a number"""

    if validate:
        typer.echo("Validating haiku...")
        first_line = typer.prompt("Enter the first line")
        second_line = typer.prompt("Enter the second line")
        third_line = typer.prompt("Enter the third line")
        validate_haiku(first_line, second_line, third_line)
        return
    elif generate:
        typer.echo("Generating haiku...")
        generate_haiku()
        return

    user_input = typer.prompt(dedent(typer_prompt))

    if user_input == "1":
        typer.echo("Validating haiku...")
        first_line = typer.prompt("Enter the first line")
        second_line = typer.prompt("Enter the second line")
        third_line = typer.prompt("Enter the third line")
        validate_haiku(first_line, second_line, third_line)
    elif user_input == "2":
        typer.echo("Generating haiku...")
        generate_haiku()
    elif user_input == "3":
        typer.echo("Goodbye!")
    else:
        typer.echo("Invalid input")


if __name__ == "__main__":
    typer.run(main)
