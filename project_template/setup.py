#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Setup script for uberapp (Change this to your amazing project name).
Latest version can be found at https://github.com/dakside/pydemo

References:
    Python documentation:
        https://docs.python.org/
    argparse module:
        https://docs.python.org/3/howto/argparse.html
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

:copyright: (c) 2018 Le Tuan Anh <tuananh.ke@gmail.com>
:license: MIT, see LICENSE for more details.
'''

import io
import os
from setuptools import setup

########################################################################


def read(*filenames, **kwargs):
    ''' Read contents of multiple files and join them together '''
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


readme_file = 'README.rst' if os.path.isfile('README.rst') else 'README.md'
long_description = read(readme_file)
pkg_info = {}
exec(read('uberapp/__version__.py'), pkg_info)

# packages to distribute
packages = ['uberapp',
            'uberapp.data']
# non-code files to distribute
package_data = {'uberapp': ['data/*.txt']}

setup(
    name='uberapp',  # package file name (<package-name>-version.tar.gz)
    project_urls={
        "Bug Tracker": "https://github.com/dakside/pydemo/issues",
        "Source Code": "https://github.com/dakside/pydemo"
    },
    tests_require=[],
    install_requires=[],
    keywords="nlp",
    # Reference: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Development Status :: 2 - Pre-Alpha',
                 'Environment :: Plugins',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: {}'.format(pkg_info['__license__']),
                 'Operating System :: OS Independent',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='test',
    platforms='any',
    version=pkg_info['__version__'],
    url=pkg_info['__url__'],
    license=pkg_info['__license__'],
    author=pkg_info['__author__'],
    author_email=pkg_info['__email__'],
    description=pkg_info['__description__'],
    long_description=long_description,
    packages=packages,
    package_data=package_data,
    include_package_data=True
)
