#!/bin/bash

DATE=`date +%Y_%m%d_%H%M%S`
mkdir -p result/${DATE}

locust  -f query_user_api_test.py  --headless -u 10  -r 5  -t120s  --csv="result/${DATE}/query_user_api_test_data"  --html="result/${DATE}/query_user_api_test.html"  --logfile="logs/query_user_api_test_${DATE}.log"
