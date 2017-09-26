#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This is a demo Python tool which counts the lines of any give file.
Latest version can be found at https://github.com/letuananh/pydemo

References:
argparse module:
    https://docs.python.org/2/howto/argparse.html
PEP 257 - Python Docstring Conventions:
    https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
'''

# Copyright (c) 2015, Le Tuan Anh <tuananh.ke@gmail.com>
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

__author__ = "Le Tuan Anh <tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2015, pydemo"
__credits__ = []
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

########################################################################

import sys
import os
import argparse


# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

def count_lines(filename, quiet=True):
    '''Count the number of lines in a file if it exists (return -1 if file doesn't exist)

    Arguments:
        filename -- Path to the file to be processed

    Return -1 if the file cannot be found
    '''
    length_of_file = -1
    if os.path.isfile(filename):
        with open(filename) as infile:
            length_of_file = len(infile.readlines())
            if quiet:
                print(length_of_file)
            else:
                print("File [%s] has [%s] line(s)." % (filename, length_of_file))
    else:
        if quiet:
            print(length_of_file)
        else:
            print("I cannot find the file [%s]" % (filename,))
    return length_of_file


# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------

def main():
    '''Main entry of this demo application.
    '''
    parser = argparse.ArgumentParser(description="Count number of lines in a file.")
    parser.add_argument('filepath', help='The path to the file that you want to process.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    if len(sys.argv) == 1:
        # User didn't pass any value in, show help
        parser.print_help()
    else:
        args = parser.parse_args()
        if args.verbose:
            print("You have activated my talkative mode ...")
        if args.filepath:
            count_lines(args.filepath, args.quiet)
        if args.verbose:
            print("Bye sweetie ...")
    pass


if __name__ == "__main__":
    main()
