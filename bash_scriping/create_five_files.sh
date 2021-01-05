#!/bin/bash
start=`date +%s`
n=1
result=${PWD##*/}
echo $result
mkdir -p files
cd files
while [ $n -le 5 ]; do
    touch file$n.HTM
    ((n+=1))
done

end=`date +%s`
runtime=$((end-start))
echo $runtime