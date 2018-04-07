import os
from pathlib import Path


MY_DIR = Path(os.path.dirname(__file__))
usernames = (MY_DIR / 'usernames.txt').read_text().splitlines()
