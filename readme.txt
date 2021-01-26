Built on python-craigslist module:
https://pypi.org/project/python-craigslist/
**************************************************************************
Notes: 
A super simple program designed to be used with a postgresql database containing a 'clscraper' db and 'listings' table. 
A backup of a sample database is included, which can be used/modified for your individual purposes. 
Alternately you can change the 'use_database' {yes|no} configuration option to output listings to 'listings.txt' instead.
Posts notifications to a slack channel, slack URL configured in the config file. 

This program was originally created to scrape for local used car listings. See the python-craigslist docs at the link above to get the proper subclass and filters to meet individual needs, and modify as needed. 
'testScrape.py' and 'test_config.ini' are included, and intended to be used to test new filters and categories to assist in modifying the main module. 

***************************************************************************
Pyodbc drivers:
You will need to install pyodbc on your system and determine which postgresql driver to use
based on what you have available on your system. 
> pyodbc.drivers()

For me, ubuntu used "PostgreSQL Unicode", while windows utilized "PostgreSQL ODBC Driver(ANSI)". 
This is configured within connectDb.py.
****************************************************************************

Modules & files:
clScraper.py- Main contains main loop for scraping, posting to db, and notifying via Slack (easily modified to notify via sms).
Logger.py - Fully customizable logger to allow you to log exactly what you want to see, or simply print to console.
config.ini - Contains configuration options. Remember to import your config options at the top of clScraper.py if you modify them or use another subclass. 
connectDB - Module that handles database connection. 
logFile.txt - output file for logging. 

*****************************************************************************

Config options:
*Note*
[OPTIONS] are universal to the program no matter what you're scraping for. [FILTERS] are specific to the subclass you choose to use. 
See python-craigslist docs for complete list of subclasses and filter options. 
You will need to modify the configuration options to fit your subclass, and remember to import them in the main clScraper.py file. 

site = top level domain for your local craigslist site. ex. https://monterey.craigslist.org/
category = the category you're scraping for. ex. 'cto' is cars and trucks for sale. 
sortBy = order in which you want your results returned. 
maxResults = max number of results you want returned each scrape. 
sleepTime = time interval to sleep (seconds) between each scrape. 
slackURL = URL of the slack channel to post new results to. 

query = your search query- same/similar to what you would enter to search for your desired results on craigslist. 
searchDistance = distance from your locale you'd like to see results for.
zipCode = zip of your locale. 
minPrice = minimum price of results. 
maxPrice = maximum price of results. 
hasImage = has image included with listing (Boolean, * for either). 

