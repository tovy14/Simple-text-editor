import os
from pathlib import Path
from file_io import create_file, write_to_file
from user_input import user_input


path = Path()

def main():
    write_to_file(user_input())

main ()