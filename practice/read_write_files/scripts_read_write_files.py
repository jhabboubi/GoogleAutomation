#!/usr/bin/env python3

#path is relative path (must be on practice directory to work)

file_location="spider.txt"
file = open(file_location)
#reads oneline at a time, points to next line.
print(file.readline())

# Reads all the file
print(file.read())

#close file to unlock for other users and save resources on machine.
file.close()

#with open block will auto close the file
with open(file_location) as file:
    print(file.readline())

# iterating through files
#.upper() will upper case all letters and .strip() delete all surrounding taps and whitespace 
with open(file_location) as file:
    for line in file:
        print(line.upper().strip())


# saving file content in a list
file = open(file_location)
lines = file.readlines()
file.close()
print(lines)


#write content to files 

file_location_write ="novel.txt"
with open(file_location_write,"a") as file:
    file.write("It was a dark and stormy night\n")


