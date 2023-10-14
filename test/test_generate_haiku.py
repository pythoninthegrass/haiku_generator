# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import haiku_generator
from datetime import timedelta
from hypothesis import given, settings, strategies as st


@settings(deadline=timedelta(milliseconds=500))
@given(st.integers(min_value=1, max_value=3))
def test_generate_haiku(num_haikus):
    for _ in range(num_haikus):
        haiku_generator.generate_haiku()
