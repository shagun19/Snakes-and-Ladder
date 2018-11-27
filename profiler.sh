#!/bin/sh
outputfile=$1
while :;
do
                top -bc -n 1 -w 512 | grep "load average\|snakes-ladders" >> $outputfile
                echo >> $outputfile
                sleep 1
done
