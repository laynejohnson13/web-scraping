Required packages:

- requests
- needed to pip install bs4 - from bs4 import BeautifulSoup
- pandas

Websites scraped:

https://www.indeed.com/?from=gnav-jobsearch--jasx

**Indeed uses anti-webscraping services so I downloaded into local html file

https://www.flyingpointsurf.com/womens/dresses/


Indeed:

- found h1 tag which included the company name
- found ins tag which included the job title (position)

Flying Point Surf:

- found h1 tag which included the item being listed for sale
- found ins tag which listed the price per item for sale


ERRORS:

- ran into problems with appending the data in both .py scripts - recieving error that 'str' objet has no attribute 'text'
