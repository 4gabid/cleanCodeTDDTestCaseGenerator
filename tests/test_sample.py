import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from JamaTestCaseGenerator import validateVPM

def test_validVPM():
    assert validateVPM() == True
