# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import haiku_generator
from hypothesis import given, strategies as st

# TODO: replace st.nothing() with an appropriate strategy


@given(line=st.text(alphabet='bcdfghjklmnpqrstvwxyzaeiouy', min_size=1, max_size=20))
def test_fuzz_syllables_in_line(line):
    haiku_generator.syllables_in_line(line=line)

