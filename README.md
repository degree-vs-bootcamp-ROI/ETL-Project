# US Job Market Tests Positive for COVID-19

**Team:** Karl Ramsay (Project Manager), Oswaldo Moreno (Data Engineer), Swati Dontamsetti (Data Engineer), Amber Marting (Data Analyst), Firzana Razak (Data Analyst), Anthony Brown (Data Analyst)

## Overview
The United States has cut nearly 10 million jobs in recent weeks due to the COVID-19 shutdown. This project will provide an analysis of the impact the COVID-19 shutdown has had on the Data Science job market.

Hypothesis: As new cases of COVID-19 crop-up, the number of job postings will decline.

We decided to use <a href="https://www.indeed.com/">Indeed</a> for our job postings search, and we compared the results with the data from the <a href="https://covid19.healthdata.org/united-states-of-america">Institute for Health Metrics and Evaluation</a> on COVID-19 cases, to see if our hypothesis is true, and to what degree.

We have the data shown for all of the United States, but we also broke the data down by "Top Cities" for Data Science jobs as provided by <a href="https://datajobs.com/">DataJobs</a>: New York, Chicago, Boston, San Francisco (Bay Area), and Seattle.

### <center>Some Considerations</center>
Indeed on provides how many dags ago a job was posted as it's timestamp on a posting, and it only goes back so far as 30 days. So any jobs posted before 29 days ago shows up as 30+. This means that 30 days ago in our graphs means 30+ days ago.

However, since, most states issued lockdowns around <a href="https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States">March 19th</a>, which is 32 days ago from the day we collected our data from Indeed (April 20th), this timed out perfectly for our analysis.

This data is all very new and current, so there is no way of creating a longitudinal study. And as both job-postings are limited in their window of staying on websites, and there is no real test-case to compare this too, there is no way to see how our current results compare to other pandemics of the past.
