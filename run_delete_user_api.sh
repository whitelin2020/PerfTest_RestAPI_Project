#!/bin/bash

DATE=`date +%Y_%m%d_%H%M%S`
mkdir -p result/${DATE}


locust  -f delete_user_api_test.py  --headless -u 2  -r 1  -t6m  --csv="result/${DATE}/delete_user_api_test_data"  --html="result/${DATE}/delete_user_api_test.html"  --logfile="logs/delete_user_api_test_${DATE}.log"
