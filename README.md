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

## Setup
* Minimum requirements
  * [Python 3.11](https://www.python.org/downloads/)
* Recommended
  * [asdf](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf)
  * [poetry](https://python-poetry.org/docs/)

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

## Development
* Testing
    ```bash
    # generate tests
    poetry shell
    hypothesis write haiku_generator.validate_haiku > test_validate_haiku.py

    # run specific test
    pytest -k test_validate_haiku
    ```

## TODO
* [Open Issues](https://github.com/pythoninthegrass/haiku_generator/issues)
* Generate more human-esque poems lmao
* CI
  * Auto format (e.g., pep8)
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

[What you can generate and how — Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/data.html#)
