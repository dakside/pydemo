#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This tools is used to read a tab seperated file and format it into a table 

@author: Hoang Duc Chinh <dc.hoang.vn@gmail.com>
'''

# Copyright (c) 2015, Hoang Duc Chinh <dc.hoang.vn@gmail.com>
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

__author__ = "Hoang Duc Chinh <dc.hoang.vn@gmail.com>"
__copyright__ = "Copyright 2015, pydemo"
__credits__ = [ "Hoang Duc Chinh" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Hoang Duc Chinh"
__email__ = "<dc.hoang.vn@gmail.com>"
__status__ = "Prototype"

import csv

def is_number(s):
	''' check if a string is a float
	
	Arguments:
	s -- input string to be checked
	'''
	try:
		float(s)
		return True
	except ValueError:
		return False

def beautifulize(in_file_path,out_file_path):
	''' Read a CSV file and format the data and then write the output to another 
	file.
	
	Arguments:
	in_file_path  -- input file to be read
	out_file_path -- output which contains the formatted data
	'''
	maxlengths = []
	with open(in_file_path,'r') as csvfile:
		csvreader = csv.reader(csvfile,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		for row in csvreader:
			if len(maxlengths) < len(row):
				maxlengths += [0] * ( len(row) - len(maxlengths) )
			for idx, val in enumerate(row):
				if len(val) > maxlengths[idx]:
					maxlengths[idx] = len(val)
			print(row)
		print(maxlengths)
	
	with open(in_file_path,'r') as csvfile:	
		csvreader = csv.reader(csvfile,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		for row in csvreader:
			for idx, val in enumerate(row):
				if maxlengths[idx] > len(val):
					if (is_number(val)):
						row[idx] = " " * (maxlengths[idx] - len(val)) + row[idx]
					else:
						row[idx] += " " * (maxlengths[idx] - len(val))
			print(row)
	pass

#------------------------------------------------------------------------------
# Define the main method
#------------------------------------------------------------------------------
def main():
	'''The main entry of the application (i.e. The tasks should start from here)
	'''
	beautifulize('test.csv','test.beautiful.csv')
	pass # Do nothing, yes Python has a statement to do nothing :D

#------------------------------------------------------------------------------
# Check if this file is run as an application
#------------------------------------------------------------------------------
if __name__ == "__main__":
	# If the condition is true, execute the main method
	main()
