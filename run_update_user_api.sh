#!/bin/bash

DATE=`date +%Y_%m%d_%H%M%S`
mkdir -p result/${DATE}

locust  -f update_user_api_test.py  --headless -u 2  -r 1  -t60s  --csv="result/${DATE}/update_user_api_test_data"  --html="result/${DATE}/update_user_api_test.html"  --logfile="logs/update_user_api_test_${DATE}.log"
