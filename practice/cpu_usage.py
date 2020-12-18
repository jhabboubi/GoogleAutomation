#!/usr/bin/env python3

import psutil

def check_cpu_usage(percent):s
    usage = pustil.cpu_precent()
    return usage < percent
if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everything ok")

