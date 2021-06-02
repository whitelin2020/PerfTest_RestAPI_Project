#!/bin/bash

DATE=`date +%Y_%m%d_%H%M%S`
mkdir -p result/${DATE}

locust  -f create_user_api_test.py  --headless -u 2  -r 1  -t4m    --csv="result/${DATE}/create_user_api_test_data"  --html="result/${DATE}/create_user_api_test.html"  --logfile="logs/create_user_api_test_${DATE}.log"
