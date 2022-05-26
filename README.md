All parsers for data that I wrote.

dm – exploring the data from finviz about S$P 500, I found out that I need a table to analyse table from the site properly. So I wrote this parser for table. It built just for my occasion, because I made a dataframe with specific column names. Used: beautifulsoup

universal_script - pretty much the same as dm,just more stable and universal for parsing big tables. Used: pandas and regex

parse_mirror and parse_rally - for scrape these webpages.

parse_patreon - I was intrested in analysis of all creators, but I coudn't find all of them, so I wrote this script. Used: json, requests, pandas
