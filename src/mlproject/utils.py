# reading of data from database will be doen here

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject.exception import CustomException
from mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():                                # will return dataframe
    logging.info("Reading SQL database started")
    
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info("Connected to the mysql database successfully", mydb)
        
        df = pd.read_sql_query("SELECT * FROM student", mydb)
        print(df.head())
        
        return df
    
        
    except Exception as e:
        raise CustomException(e, sys)