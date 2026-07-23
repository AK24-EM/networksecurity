import certifi
import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.loggers import logging

class NetworkDataExtract():
    def __init__(self):
        try :
            pass
        except Exception as e:
            raise NetworkSecurityException(e , sys)

    
    def cv_to_json(self , file_path):
        try:
            print(f"file_path is: {repr(file_path)}")
            data = pd.read_csv(file_path)
            data.reset_index(drop=True , inplace=True) 
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e , sys)

    def push_to_mongodb(self , records , database , collections):
        try:
            self.database = database
            self.collections = collections
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collections = self.database[self.collections]
            self.collections.insert_many(self.records)
            return (len(self.records))
            logging.info("Data pushed to MongoDB")
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    file_path = '/Users/aayushkamble/Desktop/mlops/Network_data/phishingdata.csv'
    DATABASE = "Networksecurity"
    COLLECTION = "phishing"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json(file_path)
    print(records)
    no_of_records =networkobj.push_to_mongodb(records , DATABASE , COLLECTION)
    print(no_of_records)
