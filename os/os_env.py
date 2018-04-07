#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Interact with OS environment using Python
Latest version can be found at https://github.com/dakside/pydemo

References:
    Python documentation:
        https://docs.python.org/
    PEP 0008 - Style Guide for Python Code
        https://www.python.org/dev/peps/pep-0008/
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
'''

# Copyright (c) 2018, Le Tuan Anh <tuananh.ke@gmail.com>
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

__author__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2018, pydemo"
__license__ = "MIT"
__maintainer__ = "Le Tuan Anh"
__version__ = "0.1"
__status__ = "Prototype"
__credits__ = []

########################################################################

import os
import sys

# -------------------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------------------

DATA_FOLDER = os.path.abspath(os.path.expanduser('./data'))


# -------------------------------------------------------------------------------
# Application logic
# -------------------------------------------------------------------------------

def read_std_in():
    if not sys.stdin.isatty():
        return sys.stdin.read()
    else:
        return None


# -------------------------------------------------------------------------------
# Main method
# -------------------------------------------------------------------------------

def main():
    '''Main entry of os_env
    '''
    pydemo_home = os.environ.get('PYDEMO_HOME', '.')
    print("PYDEMO_HOME: {}".format(os.path.abspath(pydemo_home)))
    indata = read_std_in()
    if not indata:
        print("No stdin")
    else:
        print("stdin data: {}".format(indata.strip()))


if __name__ == "__main__":
    main()
