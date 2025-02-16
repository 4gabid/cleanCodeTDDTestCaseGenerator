import sys
import os
import pytest

@pytest.fixture(scope='session', autouse=True)
def add_src_to_path():
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

@pytest.fixture(scope='module')
def valid_vpms():
    return [10, 20, 40, 50, 60, 70]

@pytest.fixture(scope='module')
def invalid_vpms():
    return [80, 30, "VPM10", "VPM20", "abc", "@#$%", 10.5, None]
