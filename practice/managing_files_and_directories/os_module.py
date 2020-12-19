#!/usr/bin/env python3

from os import *

print(path.abspath('thistoremove.txt'))

print(getcwd())
mkdir("test.txt")
chdir("../")
print(getcwd())
