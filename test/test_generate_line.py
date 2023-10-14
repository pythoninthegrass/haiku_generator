# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import haiku_generator
from hypothesis import given, strategies as st


@given(words=st.lists(
        st.text(
            alphabet='bcdfghjklmnpqrstvwxyzaeiouy',
            min_size=1, max_size=10)),
            syllables=st.integers(min_value=5,
                                  max_value=6)
        )
def test_fuzz_generate_line(words, syllables):
    total_syllables = sum(haiku_generator.syllables_in_word(word) or 0 for word in words)
    if total_syllables >= syllables:
        haiku_generator.generate_line(words=words, syllables=syllables)
