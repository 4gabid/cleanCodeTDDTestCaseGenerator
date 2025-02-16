import pytest
from JamaTestCaseGenerator import isVPMValid

@pytest.mark.parametrize("value", pytest.lazy_fixture('valid_vpms'))
def test_validVPM(value):
    assert isVPMValid(value) == True

@pytest.mark.parametrize("value", pytest.lazy_fixture('invalid_vpms'))
def test_invalidVPM(value):
    assert isVPMValid(value) == False

