#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Basic XML processing
Latest version can be found at https://github.com/letuananh/pydemo

References:
    Python documentation:
        https://docs.python.org/
    LXML tutorial:
        http://lxml.de/tutorial.html
    PEP 0008 - Style Guide for Python Code
        https://www.python.org/dev/peps/pep-0008/
    PEP 0257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
'''

# Copyright (c) 2016, Le Tuan Anh <tuananh.ke@gmail.com>
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
__copyright__ = "Copyright 2016, basic_xml"
__credits__ = []
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

########################################################################

import os
import logging
from lxml import etree
from collections import namedtuple

# -------------------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------------------

DATA_FOLDER = os.path.abspath(os.path.expanduser('./data'))

# -------------------------------------------------------------------------------
# DATA STRUCTURES
# -------------------------------------------------------------------------------

Person = namedtuple('Person', ['name', 'age'])


# -------------------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------------------

def create_xml_file(args):
    pass


def dev_mode():
    print("I'm working on this ...")


# -------------------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------------------

def main():
    ''' This program will create XML files based on boy names and girl names data
    '''
    logging.basicConfig(level=logging.INFO)
    BOY_NAMES_FILE = 'data/boy_names_2014.txt'
    GIRL_NAMES_FILE = 'data/girl_names_2014.txt'
    COUPLES_XML_FILE = 'data/couples.xml'

    # Read boy names and girl names
    with open(BOY_NAMES_FILE, 'r') as boyfile, open(GIRL_NAMES_FILE, 'r') as girlfile:
        logging.info('Reading boy names from %s' % (BOY_NAMES_FILE))
        boy_names = [x.strip() for x in boyfile.readlines() if not x.startswith('#')]
        logging.info('Reading girl names from %s' % (GIRL_NAMES_FILE))
        girl_names = [x.strip() for x in girlfile.readlines() if not x.startswith('#')]

    # Create an XML root node 'couples' ...
    couples = etree.Element('couples')
    # ... which contains many couple nodes inside
    for husband, wife in zip(boy_names, girl_names):
        etree.SubElement(couples, 'couple', husband=husband, wife=wife)
    # write couples' information to file
    logging.info("Writing couples' information to %s" % (COUPLES_XML_FILE))
    with open(COUPLES_XML_FILE, 'wb') as outfile:
        outfile.write(etree.tostring(couples, xml_declaration=True, pretty_print=True))

    # Read data from XML file
    logging.info("Looking for Leo & Anna marriage statuses from %s" % (COUPLES_XML_FILE))
    tree = etree.iterparse(COUPLES_XML_FILE)
    for event, element in tree:
        if event == 'end' and element.tag == 'couple':
            # do something to the element ...
            husband = element.get('husband')
            wife = element.get('wife')
            if husband == 'Leo' or wife == 'Anna':
                print("According to our sources, %s and %s love each other and they are married" % (husband, wife))
            # and then we can clear the element to save memory
            element.clear()

    # Done!
    pass


if __name__ == "__main__":
    main()
