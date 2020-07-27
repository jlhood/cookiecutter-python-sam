"""Setup unit test environment."""

import sys
import os

import test_constants

# make sure tests can import the app code
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../../src/')

# disable x-ray during unit test runs
os.environ['AWS_XRAY_SDK_ENABLED'] = 'false'

# set expected config environment variables to test constants
os.environ['TABLE_NAME'] = test_constants.TABLE_NAME
