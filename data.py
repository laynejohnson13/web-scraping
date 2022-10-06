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

######
len(output_company_name)
output_company_name[1]
output_company_name[3]
###recieving error - list index out of range


job_title = soup.find_all('div', class_ = 'css-1m4cuuf e37uo190')
output_job_title = []
for i in job_title:
    print(i.text)
data = i.text
job_title.append(data)


location = soup.find_all()
for i in location:
    print(i.location)

list1 = company_name 
list2 = job_title


# create dictionary
dictionary = {'company': list1, 'position': list2}

## convert to dataframe
df = pd.DataFrame({'company':company_name,'position':job_title})

##convert to csv 
df.to_csv('/Users/laynejohnson/Desktop/HHA507:504 - classwork/web-scraping/data/indeed_scraped')





####upload Flying Point Surf Shop data

surf_shop = requests.get('https://www.flyingpointsurf.com/womens/dresses/')

##make beautifulsoup object
soup = BeautifulSoup(surf_shop.text, 'html.parser')

print(soup.prettify())


##Pull clothing items listed
item = soup.find_all('h1', class_ = "text-base margin-bottom-xs")
output_item = []
for i in item:
    print(i.text)
data = i.text
item.append(data)



##Pull prices for items
price = soup.find_all('ins', class_ = "prod-card__price")
output_price = []
for i in price:
    print(i.text)
data = i.text
price.append(data)




list1 = item 
list2 = price


# create dictionary
dictionary = {'item': list1, 'price': list2}

## convert to dataframe
df = pd.DataFrame({'item':item,'price':price})

##convert to csv 
df.to_csv('/Users/laynejohnson/Desktop/HHA507:504 - classwork/web-scraping/data/surf_shop_scraped')



###CLEAN DATA 