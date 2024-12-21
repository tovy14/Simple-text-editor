import os


def read_file(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
                print(content)
    except OSError:
        print(f"{filename} could not be opened")


def write_to_file(filename, mode):
    content = []
    while True:
        line = input("$: ")
        if line == "SAVE":
            break
        content.append(line)
    try:
        with open(filename, mode) as file:
            file.write('\n'.join(content))
            print(f"{filename} saved.")
    except OSError:
        print(f"{filename} could not be saved")


def find_and_replace(filename, search, replace):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
                content.index(search)
                replaced = content.replace(search, replace)
            with open(filename, "w") as file:
                file.write(replaced)
    except ValueError:
        print("Word not found in document!")
