from user_input import user_input



def create_file():
    pass

def write_to_file(path):
    while  input()!= "SAVE":
        with open(path,"w+") as file:
            file.write(input("$: "))





write_to_file("./test.txt")