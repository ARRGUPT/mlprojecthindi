# database(mysql/mongodb/postgres) ---> read data(in utils.py) ---> train test split ---> output(having dataset in train test split format)

import os                                             # for current working directory
import sys                                            # to handle CustomException
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject.exception import CustomException
from mlproject.logger import logging
import pandas as pd
from mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split


from dataclasses import dataclass                     # for input parameters initialization


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            #reading data from database
            df = read_sql_data()
            logging.info("Reading completed from mysql database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
            
            
            

        except Exception as e:
            raise CustomException(e, sys)