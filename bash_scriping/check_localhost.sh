#!/bin/bash

#the script is going to check if localhost exist on the machine 
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything OK!"
else "Error: 127.0.0.1 not found!"
fi
