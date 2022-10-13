import pandas as pd
import requests
from bs4 import BeautifulSoup

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
    ##data = i.text
    if i.text == None:
        print('skipping')
    else:
        output_item.append(i.text)

len(output_item)
output_item[0]
output_item[3]





##Pull prices for items
price = soup.find_all('ins', class_ = "prod-card__price")
output_price = []
for i in price:
    print(i.text)
    if i.text == None:
        print('skipping')
    else:
        output_price.append(i.text)

len(output_price)
output_price[0]
output_price[3]


list1 = item 
list2 = price


# create dictionary
dictionary = {'item': list1, 'price': list2}

## convert to dataframe
df = pd.DataFrame({'item':item,'price':price})

##convert to csv 
df.to_csv('/Users/laynejohnson/Desktop/HHA507:504 - classwork/web-scraping/data/surf_shop_scraped')
