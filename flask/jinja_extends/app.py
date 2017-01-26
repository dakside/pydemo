#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Hello Flask
Latest version can be found at https://github.com/letuananh/pydemo

References:
    Python documentation:
        https://docs.python.org/
    Flask documentation:
        http://flask.pocoo.org/

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
__copyright__ = "Copyright 2016, pydemo"
__credits__ = ["Le Tuan Anh"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

########################################################################

from flask import Flask
from flask import render_template

########################################################################


app = Flask(__name__)


@app.route('/')
def rootpage():
    title = "THE RED-HEADED LEAGUE (Arthur Conan Doyle)"
    paragraphs = ["""I had called upon my friend, Mr. Sherlock Holmes, one day in the
     autumn of last year and found him in deep conversation with a very
     stout, florid-faced, elderly gentleman with fiery red hair. With an
     apology for my intrusion, I was about to withdraw when Holmes pulled
    me abruptly into the room and closed the door behind me.""",
                  """ "You could not possibly have come at a better time, my dear Watson," he said cordially.""",
                  """ "I was afraid that you were engaged." """]
    return render_template('child.html', title=title, paragraphs=paragraphs)


if __name__ == '__main__':
    app.debug = True  # To show error message
    app.run()
    # app.run(host='0.0.0.0') to listen on all public IPs
