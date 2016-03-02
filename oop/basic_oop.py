#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This script demonstrates how to use OOP in Python
Latest version can be found at https://github.com/letuananh/pydemo

References:
Classes in Python:
    https://docs.python.org/2/tutorial/classes.html

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

########################################################################

import logging

########################################################################

class Classroom:
    ''' This class represents a classroom model. Each class has its own code and a group of students.
    '''
    def __init__(self, class_code):
        self.students   = []
        self.class_code = class_code

    def add(self, student):
        ''' This method will add an existing student into this classroom
        '''
        self.students.append(student)

    def __repr__(self):
        ''' This method will print details of a classroom object 
        '''
        return "Classroom{code='%s',Students=%s}" % (self.class_code, self.students)

    def __str__(self):
        ''' A shorter & more human friendly way of printing an object
        '''
        return "Classroom %s" % (self.class_code)


class Student:
    ''' Each student object has a name and age.
    '''

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __repr__(self):
        return "Student{name='%s',age=%s}" % (self.name, self.age)

    def __str__(self):
        return "Student %s" % (self.name)

#----------------------------------------------------------------------------
# Define the main method
#------------------------------------------------------------------------------
def main():
    '''The main entry of the application (i.e. The tasks should start from here)
    '''
    
    # Create a classroom
    c = Classroom("Philosophy 101")
    print("%s is created." % c)

    # ... now we create students
    descartes = Student("Rene Descartes", 419)
    nietzsche = Student("Friedrich Nietzsche", 171)
    print("%s is created." % descartes)
    print("%s is created." % nietzsche)

    # ... add the students to the classroom
    c.add(descartes)
    c.add(nietzsche)

    # Bonus: You can use repr to get deeper information, this can be useful for debugging
    print("-" * 20)
    print(repr(c))
    logging.info(repr(c))

    pass

#------------------------------------------------------------------------------
# Check if this file is run as an application
#------------------------------------------------------------------------------
if __name__ == "__main__":
    # If the condition is true, execute the main method
    main()
