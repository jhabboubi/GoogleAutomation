#!/usr/bin/env python3

from os import *

print(path.abspath('thistoremove.txt'))

print(getcwd())
mkdir("test_dir")
chdir("../")
print(getcwd())
