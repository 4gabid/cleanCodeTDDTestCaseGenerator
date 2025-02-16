import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from JamaTestCaseGenerator import isVPMValid

def test_validVPM10():
    assert isVPMValid(10) == True

def test_validVPM20():
    assert isVPMValid(20) == True

def test_validVPM30():
    assert isVPMValid(30) == True

