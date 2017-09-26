#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python logging demo
Latest version can be found at https://github.com/letuananh/logging_demo

References:
    Python documentation:
        https://docs.python.org/
    PEP 0008 - Style Guide for Python Code
        https://www.python.org/dev/peps/pep-0008/
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
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

__author__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2017, logging_demo"
__license__ = "MIT"
__maintainer__ = "Le Tuan Anh"
__version__ = "0.1"
__status__ = "Prototype"
__credits__ = []

########################################################################

import os
import logging
import logging.config
import json
import argparse
from collections import namedtuple


# -------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------

def setup_logging(filename, log_dir=None):
    ''' Try to load logging configuration from a file. Set level to INFO if failed.
    '''
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    if os.path.isfile(filename):
        with open(filename) as config_file:
            try:
                config = json.load(config_file)
                print("Setting up logging using {}".format(filename))
                logging.config.dictConfig(config)
            except Exception as e:
                logging.exception("Could not load logging config")
                # default logging config
                logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)


def getLogger():
    return logging.getLogger(__name__)


setup_logging('logging.json', 'logs')

# -------------------------------------------------------------------------------
# DATA STRUCTURES
# -------------------------------------------------------------------------------

Person = namedtuple('Person', ['name', 'age'])


# -------------------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------------------

def lookup_meaning():
    left = 40
    right = 2
    getLogger().debug("Source: left={}, right={}".format(left, right))
    meaning = left + right
    getLogger().info("Found meaning: {}".format(meaning))
    return meaning


def test_log():
    getLogger().debug("__main__ debug")
    getLogger().info("__main__ info")
    getLogger().warning("__main__ warning")
    getLogger().error("__main__ error")
    getLogger().critical("__main__ critical")
    logging.debug("__root__ debug")
    logging.info("__root__ info")
    logging.warning("__root__ warning")
    logging.error("__root__ error")
    logging.critical("__root__ critical")


def uber_action(args):
    if args.reveal:
        test_log()
    meaning = lookup_meaning()
    print("The meaning of life is {}".format(meaning))
    getLogger().warning("The cake is a lie.")


def config_logging(args):
    ''' Override root logger's level '''
    if args.quiet:
        logging.getLogger().setLevel(logging.CRITICAL)
    elif args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)


# -------------------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------------------

def main():
    '''Main entry of logging_demo
    '''

    parser = argparse.ArgumentParser(description="Python logging demo", add_help=False)
    parser.set_defaults(func=None)

    # Optional argument(s)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    tasks = parser.add_subparsers(help="Task to be done")

    uber_task = tasks.add_parser('uber', parents=[parser], help='To perform an uber action')
    uber_task.add_argument('--reveal', action="store_true")
    uber_task.set_defaults(func=uber_action)

    # Main script
    args = parser.parse_args()
    config_logging(args)
    if args.func is not None:
        args.func(args)
    else:
        parser.print_help()
    pass


if __name__ == "__main__":
    main()
