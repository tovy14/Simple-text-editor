import os
from file_io import read_file, write_to_file
from user_input import user_input



def main():
    filename = user_input()
    if os.path.exists(filename):
        read_file(filename)
        if input("What do you want to do with this file, ovewrite it, or append to it (o/a)?: ") == "a":
              write_to_file(filename, "a")
        else:
             write_to_file(filename, "w")
    else:
        write_to_file(filename, "a")

main ()