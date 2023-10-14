# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import haiku_generator
from hypothesis import given, strategies as st


@given(st.text(alphabet='bcdfghjklmnpqrstvwxyz', min_size=1))
def test_syllables_in_word(word):
    haiku_generator.syllables_in_word(word=word)

