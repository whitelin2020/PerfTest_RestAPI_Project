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

import random
import requests
import time

from conf.configuration import *
from locust import TaskSet,HttpUser,task,between,constant,constant_pacing



def test_get_all_api_users():
    base_url = "https://gorest.co.in/public-api/users"
    headers = {
        "Accept": "application / json",
        "Content-Type": "application/json"
    }
    r = requests.get(base_url, headers=headers)
    json_res = r.json()
    # response header string
    # print((r.headers))
    return json_res



class ApiTasks(TaskSet):
    def on_start(self):
        all_user_data = test_get_all_api_users()
        pagination_dict = all_user_data['meta']["pagination"]
        # print(pagination_dict)
        self.total_user = int(pagination_dict['total'])
        self.total_page = int(pagination_dict['pages'])
        self.user_per_page = int(pagination_dict['limit'])


    def on_stop(self):
        '''cleanup when the taskset is stopping '''
        pass

    @task
    def get_all_api_user(self):
        url = "/public-api/users"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.client.get(url, headers=headers)


    @task
    def get_single_api_user(self):
        user_id=random.choice([x for x in range(self.total_user)])
        url = "/public-api/users/{}".format(user_id)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.client.get(url, headers=headers)




class ApiUser(HttpUser):
    tasks= [ApiTasks]
    wait_time = between(0.1, 0.5)  # meaning send request 2~10 time/second
    # wait_time = constant(0.5)   #  meaning send request 2 time/second
    host=HOST

