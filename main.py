import os
from file_io import read_file, write_to_file, find_and_replace
from user_input import user_input


def main():
    filename = user_input()
    if os.path.exists(filename):
        read_file(filename)
        answer = input(
            "What do you want to do with this file, ovewrite it, or append to it (o/a/r)?: ")
        match answer:
            case "a":
                write_to_file(filename, "a")
            case "o":
                write_to_file(filename, "w")
            case "r":
                search = input("What do you want to search for?: ")
                replace = input("With what do you want to replace with?: ")
                find_and_replace(filename, search, replace)

    else:
        write_to_file(filename, "w")


main()
