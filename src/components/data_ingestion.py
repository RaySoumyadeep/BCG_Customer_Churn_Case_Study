import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
#from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    client_data_path: str=os.path.join('artifacts',"client_data.csv")
    price_data_path: str=os.path.join('artifacts',"price_data.csv")
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            client_df=pd.read_csv('artifacts/client_data.csv')
            price_df=pd.read_csv('artifacts/price_data.csv')
            logging.info('Read the dataset as dataframe')

            churn_data = pd.merge(client_df, price_df, on='id')

            logging.info("Merging of data initiated")

            churn_data.to_csv('notebooks/data/churn_data.csv',index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.client_data_path,
                self.ingestion_config.price_data_path
            )
        except:
            pass

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion



