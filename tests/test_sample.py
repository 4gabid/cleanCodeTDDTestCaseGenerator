import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from JamaTestCaseGenerator import isVPMValid

@pytest.mark.parametrize("value", [10, 20, 40, 50, 60, 70])
def test_validVPM(value):
    assert isVPMValid(value) == True

