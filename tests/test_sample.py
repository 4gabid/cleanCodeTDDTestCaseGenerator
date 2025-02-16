import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sample import add

def test_hello_world():
    assert add(1, 1) == 2
