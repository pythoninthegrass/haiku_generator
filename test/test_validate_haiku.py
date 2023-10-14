# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import haiku_generator
from hypothesis import given, strategies as st


@given(first_line=st.none(), second_line=st.none(), third_line=st.none())
def test_fuzz_validate_haiku(first_line, second_line, third_line):
    haiku_generator.validate_haiku(
        first_line=first_line, second_line=second_line, third_line=third_line
    )

