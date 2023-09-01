import numpy as np
from sqlalchemy import create_engine
import glob as g 
import pandas as pd 

engine = create_engine("postgresql+psycopg2://postgres:passer@localhost:5433/ETL_DATABASE")

class ETLProcess: 
    def __init__(self):
        pass

    # Extraction 

    def load_csv(self): 
        dico = {}
        fichiers = g.glob("*.csv")
        for file in fichiers: 
            dico[file] = pd.read_csv(file)
        return dico 
    
    def load_json(self): 
        dico = {}
        fichiers = g.glob("*.json")
        for file in fichiers: 
            dico[file] = pd.read_json(file)
        return dico 
    
    def load_sql(self):
        data = pd.read_sql("select * from table_source", engine)
        return data 
    
    # Transform 

    def transform(self): 
        data_csv = self.load_csv().get("data.csv").drop(columns=["id"], axis=1)
        data_json = self.load_json().get("data.json").drop(columns=["id"], axis=1)
        data_sql = self.load_sql().drop(columns=["id"], axis=1)
        data = pd.concat([data_csv, data_json, data_sql], axis=0, ignore_index=True)
        data["majeur"] = data["age"]>=18
        return data

    # Save
    def save(self): 
        data = self.transform()
        data.to_sql("table_final", engine)
        print("!!! table crée !!!")
    
if __name__ == "__main__": 
    etl = ETLProcess()
    etl.save()