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


# '{"name":"Tenali Ramakrishna", "gender":"Male", "email":"tenali.ramakrishna@15ce.com", "status":"Active"}'
import random
import csv
import time

first_name_lst=["Marco","Jerry","David","Tracy","Stacy","Freeman","Grace","Betty","Annie","Bernie"]
last_name_lst=["Lin","Tam","Lee","Almeida","Cruz","Li","Leo","Ming","Ma","Te"]
name_list=[ "{}_{}".format(fname,lname) for lname in last_name_lst  for fname in first_name_lst   ]

print(name_list)

num_of_user=10000
num_of_cnt=num_of_user/len(name_list)

def generate_user_data(num_of_cnt,name_lst):
    lst_res=[]
    for user in name_list:
        d={}
        for k in range(1,num_of_user+1):
            name="{}_{}".format(user,k)
            email="{}@15ce.com".format(name.replace("_","."))
            gender="Male" if k%2==0 else "Female"
            status="Active"
            d={"name":name , "gender": gender, "email": email, "status": status ,"id":"EMPTY"}
            lst_res.append(d)
    print(lst_res)
    print(len(lst_res))
    return  lst_res

def write_csv_data(FilePath,lst_data):
    with open(FilePath,"w",newline='') as fp:
        keys = lst_data[0].keys()
        writer=csv.DictWriter(fp,keys,dialect='excel',quoting=csv.QUOTE_ALL)
        try:
            writer.writeheader()
            writer.writerows(lst_data)
        except Exception as ex:
            print("CSV File {} has writing error {}".format(FilePath,ex))


def read_csv_data(FilePath):
    lst_dict=[]
    with open(FilePath,"r",newline='') as fp:
        try:
            reader = csv.DictReader(fp, dialect='excel', quoting=csv.QUOTE_ALL)
            # reader = csv.reader(fp, dialect='excel', quoting=csv.QUOTE_ALL)
            for row in reader:
                d = {"name": row['name'] , "gender": row['gender'] , "email": row['email'], "status": row['status'], "id": row['id']}
                print(d)
                lst_dict.append(d)
            return lst_dict
        except Exception as ex:
            print("CSV File {} has writing error {}".format(FilePath,ex))



def main():
    CSV_PATH="..\\data\\test_user_data.csv"
    all_test_data=generate_user_data(num_of_user, name_list)
    test_data=all_test_data[:]
    # write_csv_data(CSV_PATH,test_data)
    read_csv_data(CSV_PATH)



if __name__=="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("This program took  {} second to finish ".format(end_time - start_time))



