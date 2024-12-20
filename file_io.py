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
        if line =="SAVE":
            break
        content.append(line)
    try:
        with open(filename, mode) as file:
            file.write('\n'.join(content))
            print(f"{filename} saved.")
    except OSError:
        print(f"{filename} could not be saved")