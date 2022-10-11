import pandas as pd
import requests
from bs4 import BeautifulSoup

##pull down website 
with open('/Users/laynejohnson/Desktop/HHA507:504 - classwork/web-scraping/html/job_search_indeed.html') as f:
    soup = BeautifulSoup(f, 'lxml')


print(soup.prettify())

##Getting job titles
company_name = soup.find_all('span', class_ = "companyName")
output_company_name = []
for i in company_name:
    print(i.text)
data = i.text
company_name.append(data)

######recieving error that 'str' objet has no attribute 'text'
len(output_company_name) 
output_company_name[1]
output_company_name[3]
##out of range 


job_title = soup.find_all('div', class_ = 'css-1m4cuuf e37uo190')
output_job_title = []
for i in job_title:
    print(i.text)
data = i.text
job_title.append(data)

len(output_job_title) 
output_job_title[1]
output_job_title[3]


list1 = company_name
list2 = job_title


# create dictionary
dictionary = {'company': list1, 'position': list2}

## convert to dataframe
df = pd.DataFrame({'company':company_name,'position':job_title})

##convert to csv 
df.to_csv('/Users/laynejohnson/Desktop/HHA507:504 - classwork/web-scraping/data/indeed_scraped')

