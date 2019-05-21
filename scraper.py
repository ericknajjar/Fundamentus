# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

from bs4 import BeautifulSoup
import scraperwiki

def p2f(x):
    striped = x.strip('%')
    splited = striped.split(',')
    integer = splited[0].replace('.','')
    decimal = splited[1]

    return float(integer+'.'+decimal)/100
  


url = 'https://www.fundamentus.com.br/resultado.php'
html = scraperwiki.scrape(url)
soup = BeautifulSoup(html, 'lxml')

table = soup.find('table').tbody
allRows = table.find_all('tr')

for content in allRows:
    ticker = content.span.text
    roic_text = content.find_all("td")[14].text
    net_worth_text = content.find_all("td")[17].text
    roic = p2f(roic_text) 
    net_worth = p2f(net_worth_text)
    scraperwiki.sqlite.save(unique_keys=['ticker'], data={"ticker": ticker, "roic": roic,"net_worth":net_worth})
