#!/bin/bash

DATE=`date +%Y-%m%d-%H:%M:%S`

echo "current Time : ${DATE} "
echo "It is creating user info csv file. Please wait ..."
python3 create_user_csv.py
