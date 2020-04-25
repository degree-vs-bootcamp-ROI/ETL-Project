from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
dbconn = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = dbconn.indeed_db
# Get source data for dynamically populated templates
# source_df = pd.read_csv('indeed_cleaned.csv')

jobs = []
jobs = db.jobs.find().limit(300)
# # Set index / set counter to 1
# i = 1

# Define routes
@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/graph.html")
def Visualization():
    return render_template('graph.html')

@app.route("/job-impact.html")
def JobImpact():
    return render_template('job-impact.html')


@app.route("/data.html")
def ViewData():
    jobs = db.jobs.find().limit(50)
    return render_template('data.html', jobs=jobs)


@app.route("/ny-data.html")
def ViewNYdata():
    jobs = db.jobs.find().limit(50)
    return render_template('ny-data.html', jobs=jobs)


@app.route("/il-data.html")
def ViewILData():
    jobs = db.jobs.find().limit(50)
    return render_template('il-data.html', jobs=jobs)


@app.route("/ma-data.html")
def ViewMAData():
    jobs = db.jobs.find().limit(50)
    return render_template('ma-data.html', jobs=jobs)


@app.route("/ca-data.html")
def ViewCAData():
    jobs = db.jobs.find().limit(50)
    return render_template('ca-data.html', jobs=jobs)


@app.route("/wa-data.html")
def ViewWAData():
    jobs = db.jobs.find().limit(50)
    return render_template('wa-data.html', jobs=jobs)


@app.route("/team.html")
def About():
    return render_template('team.html')


if __name__ == '__main__':
    app.run(debug=True)
