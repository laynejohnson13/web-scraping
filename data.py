import pandas as pd
import requests
from bs4 import BeautifulSoup

##pull down website 
with open('/Users/laynejohnson/Desktop/HHA507:504 - classwork/web-scraping/html/job_search_indeed.html') as f:
    soup = BeautifulSoup(f, 'lxml')


print(soup.prettify())

##Getting job titles
company_name = soup.find_all('span', class_ = "companyName")
for i in company_name:
    print(i.text)

job_title = soup.find_all('div', class_ = 'css-1m4cuuf e37uo190')
for i in job_title:
    print(i.text)


location = soup.find_all()
for i in location:
    print(i.location)


