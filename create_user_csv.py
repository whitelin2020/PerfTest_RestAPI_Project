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


import gevent.monkey
gevent.monkey.patch_all()
import requests
from util.Feeder import  *
from conf.configuration import *
import time


def get_user_info_by_email(lst_dict):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        }

    lst_user_dict=[]
    for k in lst_dict:
        para_email= {"email": k['email'] }
        query_url = "https://gorest.co.in/public-api/users"
        get_user_r=requests.get(query_url,headers=headers,params=para_email)

        # #debug only
        # print("GET URL :{} for email:{} ".format(get_user_r.url,para_email['email']))
        # print("status code : {}".format(get_user_r.status_code))

        json_res = get_user_r.json()

        if len(json_res["data"])>0:
            user_id=json_res["data"][0]['id']
            user_info_d=json_res["data"][0]
            print("Add user_id: {} | user_info : {} into CSV file !".format(user_id,user_info_d))
            lst_user_dict.append(user_info_d)
        else:
            print("Please wait ...")

    return  lst_user_dict



def main():
    user_data_list_dict = CSVDictFeeder(USER_DATA_CSV).read_csv_dataFile()
    # print(user_data_list_dict)

    lst_user_info_d=get_user_info_by_email(user_data_list_dict)
    created_user_csv=CSVDictWriter(USER_DATA_CREATED_CSV)
    created_user_csv.to_csv(lst_user_info_d)
    print("{} file has genreated !".format(USER_DATA_CREATED_CSV))


if __name__=="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("This program TestHelper took  {} second to finish ".format(end_time - start_time))