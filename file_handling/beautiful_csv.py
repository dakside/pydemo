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
import sys
import os
import argparse

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
	out_file_path -- output file which contains the formatted data
	Return:
	linecount ------ number of lines in the input file
	'''
	
	maxlengths = []
	linecount = 0
	# Identify the max lenght of each field
	try:
		with open(in_file_path,'r') as csvfile:
			csvreader = csv.reader(csvfile,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
			for row in csvreader:
				if len(maxlengths) < len(row):
					maxlengths += [0] * ( len(row) - len(maxlengths) )
				for idx, val in enumerate(row):
					if len(val) > maxlengths[idx]:
						maxlengths[idx] = len(val)
				linecount += 1
				print(row)
			print(maxlengths)
	except Exception as err:
		print('Cannot process the input file %s' % input_file_path)
		print(err)
		return linecount
	
	# Align each column respected to its max length
	try:
		print('Output as formatted data: ')
		# If no output file, just print out the results
		if out_file_path is None:
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
		# If there is output file, print out the results 
		# and write them to the output file
		else:
			with open(in_file_path,'r') as csvfile:	
				csvreader = csv.reader(csvfile,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
				with open(out_file_path,'w',newline='') as csvfileout:
					csvwriter = csv.writer(csvfileout)
					for row in csvreader:
						for idx, val in enumerate(row):
							if maxlengths[idx] > len(val):
								if (is_number(val)):
									row[idx] = " " * (maxlengths[idx] - len(val)) + row[idx]
								else:
									row[idx] += " " * (maxlengths[idx] - len(val))
						csvwriter.writerow(row)
						print(row)
	except Exception as err:
		print('Cannot write to the output file %s' % output_file_path)
		print(err)
		return linecount
	
	return linecount
	#pass

########################################################################
def process_file(inputfilename, outputfilename, verbose=True):
	'''Count the number of lines in a file if it exists (return -1 if file doesn't exist)
	
	Arguments:
		inputfilename -- Path to the file to be processed
		outputfilename - output which contains the formatted data
	
	Return -1 if the file cannot be found otherwise return the number of lines
	in the input file
	'''
	length_of_file = -1	
	if os.path.isfile(inputfilename):
		length_of_file = beautifulize(inputfilename, outputfilename)
		if verbose:
			print("Verbose mode - Length of file: %d" % (length_of_file))
	else:
		if verbose:
			print("Verbose mode - Length of file: %d" % (length_of_file))
		else:
			print("I cannot find the file [%s]" % (inputfilename))
	return length_of_file

#------------------------------------------------------------------------------
# Define the main method
#------------------------------------------------------------------------------
def main():
	'''The main entry of the application (i.e. The tasks should start from here)
	'''
	parser = argparse.ArgumentParser(description="Allign table in csv file to beautifulize.")
	parser.add_argument('inputfilepath', nargs='?', help='The path to the file that you want to process.')
	parser.add_argument('outputfilepath', nargs='?', help='Output file you want to save processed data ')
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", action="store_true", help='Verbose mode which display line count of the input file')

	if len(sys.argv) == 1:
		# User didn't pass any value in, show help
		parser.print_help()
	else:
		args = parser.parse_args()		
		if args.inputfilepath: # If there is an input, process it
			if args.outputfilepath: # If there is an ouput, write to it
				process_file(args.inputfilepath, args.outputfilepath, args.verbose)
			else: # If not output, just print to screen
				print('No output file, outcomes will NOT be stored!')
				process_file(args.inputfilepath, None, args.verbose)
	pass # Do nothing, yes Python has a statement to do nothing :D

#------------------------------------------------------------------------------
# Check if this file is run as an application
#------------------------------------------------------------------------------
if __name__ == "__main__":
	# If the condition is true, execute the main method
	main()
