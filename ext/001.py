#! usr/bin/python
from bs4 import BeautifulSoup
from urllib import FancyURLopener
from random import choice
import numpy as np
import pandas as pd


# making the bot a browser
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]


class MyOpener(FancyURLopener, object):
    version = choice(user_agents)


myopener = MyOpener()

# reading webpage
content = myopener.open("https://ihub.co.ke/jobs")
soup = BeautifulSoup(content, 'html.parser')

# listings
title = []
company = []
job_location = []
job_category = []
link = []
date = []


# locating all jobs
job_listings = soup.find_all("div", {"class": "container-fluid jobsboard-row"})

#Extracting job Information
for job in job_listings:
    # job title
    name = job.h3.a.text.strip()
    title.append(name)

    # company
    company_name = job.find('div', class_='job-company').text.strip()
    company.append(company_name)

    # category of job
    category = job.find('div', class_='job-cat').text.strip()
    job_category.append(category)

    #dat0
    date_0 = job.find('div', class_='job-time').text.strip()
    date.append(date_0)

    link_0 = job.find('div', class_='job-more').a
    link.append(link_0)

#writing information into dataframe

report = pd.DataFrame({'Job_Title': title,
                       'Comany': company,
                       'Type':job_category,
                       'Date_of_Posting':date,
                       'link_to_job': link})

report.to_csv('jobs.csv', encoding='utf-8', index=False)