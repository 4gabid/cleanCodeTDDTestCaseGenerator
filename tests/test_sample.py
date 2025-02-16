import pytest
from JamaTestCaseGenerator import isVPMValid

@pytest.fixture
def valid_vpms():
    return [10, 20, 40, 50, 60, 70]

@pytest.mark.parametrize("value", pytest.lazy_fixture('valid_vpms'))
def test_validVPM(value):
    assert isVPMValid(value) == True

