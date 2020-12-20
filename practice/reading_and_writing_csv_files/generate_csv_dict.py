#!/usr/bin/env python3
import csv

with open("software.csv") as software:
    for row in csv.DictReader(software):
        print("{} has {} users".format(row["name"], row["users"]))
