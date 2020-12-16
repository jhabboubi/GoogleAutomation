
#!/usr/bin/env python3
import re
import csv
import operator
error={}
per_user={}

with open("syslog.log") as f:
        for line in f:
                match=re.search(r"ticky: ERROR: ([\w ]*) \((\w+)\)", line)
                if match:
                        msg, user = match.groups()
                        error[msg] = error.get(msg,0) +1
                        if user  in per_user:
                                per_user[user][1] +=1
                        else:
                                per_user[user]=[0,0]
                else:
                        match = re.search(r"ticky: INFO .* \((\w+)\)", line)
                        if match:
                                user = match.groups()[0]
                                if user in per_user:
                                        per_user[user][0] += 1
                                else:
                                        per_user[user] = [1,0]

