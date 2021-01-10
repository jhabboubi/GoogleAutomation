#!/bin/bash

for logfile in /var/log/*log; do
    echo "--------------------"
    echo "Processing: $logfile"
    cut -d' ' -f1- $logfile | sort | uniq -c | sort -nr
done
