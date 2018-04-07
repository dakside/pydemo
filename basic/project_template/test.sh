#!/bin/bash

echo "Sample test code"
# Alternative: test a specific file
# python -m unittest test.test_demolib
python -m unittest discover -s ./test
