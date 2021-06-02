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
import json
from util.comm import *
from conf.configuration import *
from locust import HttpUser,TaskSet, task, between,constant,constant_pacing
from util.Feeder import *



def generate_user_info(num_of_user,csv_filepath):
    first_name_lst = ["Marco", "Jerry", "David", "Tracy", "Stacy", "Freeman", "Grace", "Betty", "Annie", "Bernie"]
    last_name_lst = ["Lin", "Tam", "Lee", "Almeida", "Cruz", "Li", "Leo", "Ming", "Ma", "Te"]
    name_list = ["{}_{}".format(fname, lname) for lname in last_name_lst for fname in first_name_lst]


    lst_res=[]
    d={}
    for k in range(1, num_of_user + 1):
            name = "{}_{}_{}".format(random.choice(first_name_lst),random.choice(last_name_lst),k)
            email = "{}@15ce.com".format(name.replace("_", "."))
            gender = "Male" if k % 2 == 0 else "Female"
            status = "Active"  if k % 5 == 0 else "Inactive"
            d = {"name": name, "gender": gender, "email": email, "status": status,
                 # "id": "EMPTY"
                 }
            lst_res.append(d)

    data_csv=CSVDictWriter(csv_filepath) #store all genreated user info into csv file
    data_csv.to_csv(lst_res)

    return lst_res




class ApiTasks(TaskSet):
    def on_start(self):
        self.user_created_lst=[]
        self.user_lst=generate_user_info(NUMBER_OF_USER,USER_DATA_CSV)


    def on_stop(self):
        '''cleanup when the taskset is stopping '''
        pass


    @task
    def create_api_user(self):
        # base_url = "https://gorest.co.in/public-api/users"
        url = "/public-api/users"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": API_TOKEN
        }

        # print("self.user_lst lenght : {}".format(len(self.user_lst)))
        if len(self.user_lst)>0:
            d=self.user_lst.pop(0)
            data_d=d
            res=self.client.post(url,headers=headers,data=json.dumps(data_d))

        else:
            print("[{}]All user which in the csv files has been created !  ".format(get_current_time()))
            logging.error("All user which in the csv files has been created !  Locust will stop it !")
            self.user.environment.reached_end = True
            self.user.environment.runner.quit()


class ApiUser(HttpUser):
    tasks= [ApiTasks]
    wait_time = between(0.5, 1)
    # wait_time = between(1, 2)
    # wait_time = constant(0.5)
    host=HOST


# def main():
#     generate_user_info(20,USER_DATA_CSV)
#     # lst=CSVFeeder(USER_DATA_CSV).read_csv_dataFile()
#     # lst=CSVDictFeeder(USER_DATA_CSV).read_csv_dataFile()
#     # print(lst)
#
#     user_data_list_dict = CSVDictFeeder(USER_DATA_CSV).read_csv_dataFile()
#     print(user_data_list_dict)
#
#
#
# if __name__=="__main__":
#     main()