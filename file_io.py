import os
from user_input import user_input

with open(user_input(), "rb") as file:
    file.write(input("$: "))
