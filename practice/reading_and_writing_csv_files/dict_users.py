#!/usr/bin/env python3

import csv
users = [{"name": "Sol Mansi", "username": "solm", "department" : "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department" : "User Experience Resreach"},
    {"name": "Charlie Gray", "username": "greyc", "department" : "Development"}]

keys = ["name","username", "department"]
with open("by_department.csv","w") as by_department:
    writer =csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)