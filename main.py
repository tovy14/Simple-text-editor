import os
from file_io import read_file, write_to_file
from user_input import user_input



def main():
    filename = user_input()
    if os.path.exists(filename):
        read_file(filename)
        write_to_file(filename) 
    else:
        write_to_file(filename)

main ()