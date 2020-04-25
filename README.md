# US Job Market Tests Positive for COVID-19

Team: Karl Ramsay (Project Manager), Oswaldo Moreno (Data Engineer), Swati Dontamsetti (Data Engineer), Amber Marting (Data Analyst), Firzana Razak (Data Analyst), Anthony Brown (Data Analyst)

## Overview
The United States has cut nearly 10 million jobs in the recent weeks due to the COVID-19 shutdown. This project will provide an analysis of the impact the COVID-19 shutdown has had on the Data Science job market.

We decided to use <a href="https://www.indeed.com/">Indeed</a> for our job postings search. We cross-referenced the results with the data from the <a href="https://covid19.healthdata.org/united-states-of-america">Institute for Health Metrics and Evaluation</a> on Covid-19 cases.

We have the data shown for all of the United Statest, but we also broke the data down by "Top Cities" for Data Science jobs as provided by <a href="https://datajobs.com/">DataJobs</a>: New York, Chicago, Boston, San Francisco (Bay Area), and Seattle.

### Some Considerations
Indeed on provides how many dags ago a job was posted as it's timestamp on a posting, and it only goes back so far as 30 days. So any jobs posted before 29 days ago shows up as 30+. This means that 30 days ago in our graphs is actually means 30+ days ago.

However, since, most states issued lockdowns around <a href="https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States">March 19th</a>, which is 32 days ago from the day we collected our data from Indeed (April 20th), this timed out perfectly for our analysis.
