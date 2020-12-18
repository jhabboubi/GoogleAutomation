import os
from os import *


file_name = "thistoremove.txt"

if path.exists(file_name):
    os.remove(file_name)
    print("Removed!")
else: 
    print(file_name + " return: " + str(path.exists(file_name)))
    

