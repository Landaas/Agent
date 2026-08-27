"""
Variables and types
Strings
Lists, tuples, sets and dictionaries
Conditions
for and while
Functions
Arguments and return values
Exceptions
Imports
Comprehensions
enumerate()
zip()
sorted()
any() / all()
f-strings
Basic type hints


def load_files():
    ...

def process_files(files):
    ...

def save_results(results):
    ...

def notify(results):
    ...



Exercises

Build:

Password strength checker
Filename parser
Duplicate remover for a list
Log-line analyzer
CSV-style data processor using lists/dicts
Mini-project

Downloads Folder Analyzer

Given a folder, report:

number of files
file extensions
total storage
largest files
oldest files
duplicate filenames
"""

#Module 2 — Filesystem Automation

from pathlib import Path #Imports Path from Python’s pathlib module. It provides a convenient way to work with file and folder paths.
import shutil #Imports the shutil module, which is used for higher-level file operations such as copying, moving, and deleting folders/files.
import os #Imports the os module. It provides tools for interacting with the operating system, including files, directories, environment variables, and paths.

from pathlib import Path

downloads = Path.home() / "Downloads" # Creates a Path object representing the Downloads folder in the user's home directory.

for path in downloads.iterdir(): #Iterates over each item in the Downloads folder. The iterdir() method returns an iterator of Path objects for each file and folder in the directory.
    if path.is_file(): #Checks if the current path is a file (not a directory). The is_file() method returns True if the path points to a regular file.
        print(path.name, path.suffix, path.stat().st_size) #Prints the name, file extension (suffix), and size (in bytes) of each file in the Downloads folder. The stat() method retrieves information about the file, and st_size gives the size of the file in bytes.