#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Demo with statement of Python.
Latest version can be found at https://github.com/dakside/pydemo

References:
    Python documentation:
        https://docs.python.org/
    PEP 343 - ``with'' statement
        https://www.python.org/dev/peps/pep-0343/
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/
    ---
    Jeff Preshing's tutorial:
        http://preshing.com/20110920/the-python-with-statement-by-example/
    Fredrik Lundh's tutorial:
        http://effbot.org/zone/python-with-statement.htm
    

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


import logging


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------

class SmartDB:
    ''' A sample database class that support with statement
    '''
    def __init__(self, info):
        print("__init__")
        self.info = info
        self.state = ''
        self.set_state('new')

    def set_state(self, state):
        old_state = self.state
        self.state = state
        print("\tStated changed from [%s] to [%s]" % (old_state, state))

    def select(self):
        ''' Mock-up select data
        '''
        self.set_state('selecting data')
        data = 'foo'
        self.set_state('idle')
        return data


    def close(self):
        ''' Close database connection
        '''
        self.set_state('closed')

    def __enter__(self):
        ''' Enter with statement
        '''
        print("__enter__")
        self.set_state('running')
        return self

    def __exit__(self, type, value, traceback):
        ''' Exit with statement, clean up resource, etc.
        '''
        try:
            print("__exit__")
            self.set_state('closing')
            self.close()
        except Exception as e:
            logging.getLogger(__name__).exception("Error while closing database")


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

def main():
    '''Main entry of this demo application.
    '''
    print("main()")
    with SmartDB('foo') as db:
        print("__with__")
        print("\t* Data = %s" % db.select())
    print("Done!")


if __name__ == "__main__":
    main()
