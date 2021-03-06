#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script for testing uberapp
Latest version can be found at https://github.com/dakside/pydemo

References:
    Python documentation:
        https://docs.python.org/
    Python unittest
        https://docs.python.org/3/library/unittest.html
    --
    argparse module:
        https://docs.python.org/3/howto/argparse.html
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

:copyright: (c) 2018 Le Tuan Anh <tuananh.ke@gmail.com>
:license: MIT, see LICENSE for more details.
'''

# Copyright (c) 2017, Le Tuan Anh <tuananh.ke@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import unittest
from uberapp.userlib import authenticate


# ------------------------------------------------------------------------------
# Test cases
# ------------------------------------------------------------------------------

class TestDemoLib(unittest.TestCase):

    def test_all_usernames(self):
        print("Test reading usernames from text file")
        from uberapp.data import usernames
        self.assertEqual(usernames, ['foo', 'boo', 'bar'])

    def test_null_args(self):
        print("Testing authenticate function with empty args")
        username = None
        password = None
        self.assertFalse(authenticate(username, password))

    def test_null_username(self):
        print("Testing authenticate function with empty username")
        username = None
        password = 'enoN'
        self.assertFalse(authenticate(username, password))

    def test_null_password(self):
        print("Testing authenticate function with empty password")
        username = 'None'
        password = None
        self.assertFalse(authenticate(username, password))

    def test_valid_login(self):
        print("Testing valid combination")
        username = 'foo'
        password = 'oof'
        self.assertTrue(authenticate(username, password))


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
