#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jerry lin
#
# Created:     
# Copyright:   (c) jlin 
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-

import datetime
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

def get_current_time_string():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def get_current_day_string():
    return datetime.datetime.now().strftime("%Y_%m%d_%H%S")

def get_current_day_string2():
    return datetime.datetime.now().strftime("%Y_%m%d")

def unix_timestampe_to_datetime(x):
    return datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%dT%H:%M:%S')

def utc_datetime_to_unix_timestamp(time_string):
    dt=datetime.datetime.strptime(time_string,"%Y-%m-%dT%H:%M:%S")
    time_stamp=(dt - datetime.datetime(1970,1,1)) / datetime.timedelta(seconds=1)
    # print("unix timestamp: {}".format(int(time_stamp)))
    return int(time_stamp)

def get_current_utc_time():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

def get_current_utc_timestamp_string():
    delta=int((datetime.datetime.utcnow()-datetime.datetime(1970,1,1)) / datetime.timedelta(seconds=1))
    # print("timestamp: {}".format(int(delta)))
    return delta


