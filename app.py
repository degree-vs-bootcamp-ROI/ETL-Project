from flask import Flask, render_template

import pandas as pd

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
#dbconn = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
#db = dbconn.indeed_db

# Get source data for dynamically populated templates
source_df = pd.read_csv('indeed_jobs.csv')

source_df['job_title'].dropna()

df_dropna = source_df.dropna(axis=0, how='any', thresh=None, subset=['job_title'], inplace=False)

jobs_df = df_dropna.dropna(axis=0, how='any', thresh=None, subset=['location'], inplace=False)

# Define dictionary and list
jobs_dict = {}
job_list = []

# Set index / set counter to 1
i = 1

# Loop through jobs data frame and assign to dictionary
for _, record in jobs_df.iterrows():
    jobs_dict['job_title'] = record.job_title
    jobs_dict['company'] = record.company
    jobs_dict['location'] = record.location
    jobs_dict['posted'] = record.posted

    #Append dictionary to job list
    job_list.append(jobs_dict)

    # Test if we have already have 30 rows of data then break
    if i == 30:
        break
    else:
        i += 1

# Define routes
@app.route("/")
def welcome():
    return render_template('index.html')
  
@app.route("/graph.html")
def Visualization():
    return render_template('graph.html')


@app.route("/data.html")
def ViewData():
    return render_template('data.html',job_list = job_list)


@app.route("/about.html")
def About():
    return render_template('about.html')

















if __name__ == '__main__':
    app.run(debug=True)

