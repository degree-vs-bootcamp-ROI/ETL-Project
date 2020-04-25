import pandas as pd
import pymongo

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
dbconn = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = dbconn.indeed_db

db.jobs.delete_many({})
# Get source data for dynamically populated templates
source_df = pd.read_csv('../model/indeed_cleaned.csv')
source_df.reset_index(inplace=True)

source_df['job_title'].dropna()


df_dropna = source_df.dropna(axis=0, how='any', thresh=None, subset=[
                             'job_title'], inplace=False)

jobs_df = df_dropna.dropna(axis=0, how='any', thresh=None, subset=[
                           'location'], inplace=False)

# Define dictionary and list
jobs_dict = jobs_df.to_dict("records")
db.jobs.insert_many(jobs_dict)
