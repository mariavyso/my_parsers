![GitHub top language](https://img.shields.io/github/languages/top/mariavyso/my_parsers?style=plastic)


All parsers for data that I wrote.

dm – exploring the data from finviz about S$P 500, I found out that I need a table to analyze the table from the site properly. So I wrote this parser for the table. It was built just for my occasion because I made a data frame with specific column names. Used: beautifulsoup

universal_script - pretty much the same as dm, just more stable and universal for parsing big tables. Used: pandas and regex

parse_mirror and parse_rally - for scraping these webpages. Used: requests and pandas

parse_patreon - I was interested in the analysis of all the creators, but I couldn't find all of them, so I wrote this script. Used: JSON, requests, pandas

parse_youtube - I decided to analyze some YouTube channels and make a table with simple data(the number of followers, started data, the number of videos). Used: requests, pandas.
