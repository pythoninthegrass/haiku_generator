# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import haiku_generator
import pytest
from hypothesis import given, strategies as st


@given(st.just(None))
def test_fuzz_check_internet_connection(_):
    haiku_generator.check_internet_connection()


@pytest.fixture
def _():
    return None

