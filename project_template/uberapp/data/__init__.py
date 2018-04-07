import os
from pathlib import Path


MY_DIR = Path(os.path.dirname(__file__))
with (MY_DIR / 'usernames.txt').open() as infile:
    usernames = infile.read().splitlines()
