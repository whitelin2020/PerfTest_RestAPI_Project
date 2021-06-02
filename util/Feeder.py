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

import csv
import time,sys

class CSVFeeder:
    "Read test data from csv file using an iterator"
    def __init__(self, csvfile):
        try:
            file = open(csvfile,"r")
            self.file = file
        except TypeError:
            pass  # "file" was already a pre-opened file-like object
        self.reader = csv.reader(self.file,dialect='excel', quoting=csv.QUOTE_ALL)
        # print(self.reader)

    def __next__(self):
        try:
            return next(self.reader)
        except StopIteration:
            # reuse file on EOF
            self.file.seek(0, 0)
            return next(self.reader)

    def read_csv_dataFile(self):
        lst=[]
        try:
            for row in self.reader :
                lst.append(row)
            return lst
        except Exception as ex:
                print("CSV File {} has writing error {}".format(self.file, ex))


class CSVDictFeeder:
    "Read test data from csv file using an iterator"
    def __init__(self, csvfile):
        try:
            self.file =open(csvfile,"r")
            # self.file = file
            self.reader = csv.DictReader(self.file, dialect='excel', quoting=csv.QUOTE_ALL)
            # self.data_dicts = (dict(data) for data in self.reader)

        except TypeError as ex:
            print("Open CSV file has error {}.".format(ex))


    def __next__(self):
        try:
            # return next(data for data in self.reader)
            return next((self.reader))

        except StopIteration:
            # reuse file on EOF
            self.file.seek(0, 0)
            next(self.reader)  # skip header line
            return next(self.reader)

    def read_csv_dataFile(self):
        lst_dict=[]
        try:
            for row in self.reader :
                # print(row)
                d=dict(row)
                lst_dict.append(d)
            return lst_dict
        except Exception as ex:
                print("CSV File {} has reading error {}".format(self.file, ex))




class CSVDictWriter(object):
    ''' convert list of dictionary to a csv file  '''
    def __init__(self, csvfile):
        self.csv_file=csvfile
        try:
            # with open(csvfile,"r") as fp:
            self.file =open(self.csv_file,"w",newline="")
        except TypeError:
            pass  # "file" was already a pre-opened file-like object
        # self.file = file


    def to_csv(self,lst_of_dict):
        if len(lst_of_dict)>0:
            col_name = lst_of_dict[0].keys()
            self.writer = csv.DictWriter(self.file, col_name, dialect='excel', quoting=csv.QUOTE_ALL)
            try:
                self.writer.writeheader()
                self.writer.writerows(lst_of_dict)
            except Exception as ex:
                print("[CSVDictWriter] CSV File {} has writing error {}".format(self.csv_file, ex))

            self.file.close()






# for test class only
def main():
    CSV_PATH="..\\data\\test_user_data.csv"
    test_data_reader=CSVDictFeeder(CSV_PATH)

    # ------test read_csv_dataFile() method
    all_test_data=test_data_reader.read_csv_dataFile()
    # print(len(all_test_data))

    # test_data=all_test_data[:3000]
    # print(len(test_data))
    # for k in all_test_data:
    #     print(k)
    # print(sys.getsizeof(all_test_data))


    # ---- test __next__() method (save memory space) with less time efficicy
    # print("===csv Dict FileHeader")
    # for _ in range(3000):
    #     print(dict(next(test_data_reader)))
    # print(sys.getsizeof(test_data_reader))


    #------
    # write_csv_data(CSV_PATH,test_data)
    # read_csv_data(CSV_PATH)
    csv_reader=CSVFeeder(CSV_PATH)

    #------test read_csv_dataFile() method
    # all_test_data = csv_reader.read_csv_dataFile()
    # print(type(csv_reader))
    # print(len(all_test_data))
    # for k in all_test_data[:3000]:
    #     print(k)
    # print(sys.getsizeof(all_test_data))

    #---- test __next__() method
    print("===csv Header")
    cols=next(csv_reader)
    print(cols)
    for _ in range(3000):
        print(dict(zip(cols,next(csv_reader))))
    print(sys.getsizeof(csv_reader))



if __name__=="__main__":
    import time
    start_time = time.time()
    main()
    end_time = time.time()
    print("This program took  {} second to finish ".format(end_time - start_time))
