## This script loads csv file in to db using pandas and sqlAlchemy
## It is header agnostic and replaces the table if exists. 

import pandas as pd
from sqlalchemy import create_engine

class CSVtoDB:
    def __init__(self, path):
        self.path = path
        
    def load_csv_file(self):
        self.df = pd.read_csv(self.path)
    
    def load_val_into_db(self):
        engine = create_engine("mysql://<username>:<password>@localhost/<dbname>")
        con = engine.connect()
        self.df.to_sql('<table_name>', con=con, if_exists='replace')
    

if __name__ == "__main__":
    c = CSVtoDB("<csv_file_path>")
    c.load_csv_file()
    c.load_val_into_db()