#!/bin/sh
file=300
while true; do
    timeout 60s python3 validate.py -c $file -s 1
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 2
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 3
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 4
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 5
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 6
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 7
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 8
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 9
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done

while true; do
    timeout 60s python3 validate.py -c $file -s 10
    if [ $? -eq 124 ]; then
        echo "The python script took longer than 1 minute. Restarting..."
    else
        break
    fi
done