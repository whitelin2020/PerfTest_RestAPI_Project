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
from util.Feeder import  *
from conf.configuration import *
from locust import HttpUser,TaskSet, task , between,constant,constant_pacing



class ApiTasks(TaskSet):
    def on_start(self):
        self.test_user_data_csv=USER_DATA_CREATED_CSV
        # self.test_user_data_csv=USER_DATA_DELETED_CSV

        user_data_list_dict=CSVDictFeeder(self.test_user_data_csv).read_csv_dataFile()
        self.lst_user_id=sorted([ k['id'] for k in user_data_list_dict])


    def on_stop(self):
        '''cleanup when the taskset is stopping '''
        pass


    @task
    def delete_api_user(self):
        if len(self.lst_user_id)>0:
            user_id=self.lst_user_id.pop(0)
            # print("user_id : {}".format(user_id))
            # delete_url = "https://gorest.co.in/public-api/users/{}".format(user_id)
            url = "/public-api/users/{}".format(user_id)
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": API_TOKEN
            }
            self.client.delete(url, headers=headers)
        else:
            print("All of user  has been deleted ! ")
            logging.error("All of user  has been deleted ! Locust will stop it !")
            self.user.environment.reached_end = True
            self.user.environment.runner.quit()







class ApiUser(HttpUser):
    tasks= [ApiTasks]
    wait_time = between(0.2, 1)
    # wait_time = between(1, 2)
    # wait_time = constant(0.5)
    host=HOST


# Test code
# def main():
#     user_data_list_dict = CSVDictFeeder(USER_DATA_CREATED_CSV).read_csv_dataFile()
#     # user_data_list_dict = CSVDictFeeder(self.test_user_data_csv).read_csv_dataFile()
#     print(user_data_list_dict)
#     lst_user_id = sorted([k['id'] for k in user_data_list_dict])
#     print(lst_user_id)
#     print("Total user deleted : {}".format(len(lst_user_id)))
#
# if __name__=="__main__":
#     import time
#     start_time = time.time()
#     main()
#     end_time = time.time()
#     print("This program took  {} second to finish ".format(end_time - start_time))