#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is a demo of how to read and write textual content using Python
Latest version can be found at https://github.com/letuananh/pydemo

References:
Python input & output:
    https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

@author: Le Tuan Anh <tuananh.ke@gmail.com>
'''

# Copyright (c) 2015, Le Tuan Anh <tuananh.ke@gmail.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

__author__ = "Le Tuan Anh <tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2015, pydemo"
__credits__ = [ "Le Tuan Anh" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

#------------------------------------------------------------------------------
# A function to read names from a file, each name on a line
#------------------------------------------------------------------------------
def read_names_from_file(file_name):
    ''' Read names from a file, each name on a line.
        Any line started with a hash (#) is a comment and will be ignored

        Arguments:
        file_name -- Path to input file (i.e. my_file.txt or /home/user/my_file.txt)
    '''
    names = [] # read names will be stored in this list

    with open(file_name, 'r') as names_file:
        for line in names_file:
            # if not a comment line
            if not line.startswith('#'):
                names.append(line.strip()) # add to list

    return names

#------------------------------------------------------------------------------
# Define the main method
#------------------------------------------------------------------------------
def main():
    '''This application will demonstrate how to read and write text file content with Python
    '''
    girl_names = read_names_from_file('girl_names_2014.txt')
    boy_names = read_names_from_file('boy_names_2014.txt')

    with open('couple_2014.txt', 'w') as couple_file:
        # Zip returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
        # Read more about zip here: https://docs.python.org/2/library/functions.html#zip
        for (girl_name, boy_name) in zip(girl_names, boy_names): 
            # write each couple to file
            couple_file.write('%s will marry %s in 18 years.\n' % (boy_name, girl_name))

#------------------------------------------------------------------------------
# Check if this file is run as an application
#------------------------------------------------------------------------------
if __name__ == "__main__":
    # If the condition is true, execute the main method
    main()
