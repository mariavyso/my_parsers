import requests
import pandas as pd
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
def get_table():
    for n in range(100000000000):
        n = 21+(n-1)*20
        url = f'https://finviz.com/screener.ashx?v=111&f=idx_sp500&r={n}'
        content = requests.get(url, headers=headers).text
        regex = r"""(<table.class=\"table-light[\s\w\W]*.</table>\n)"""
        matches = re.findall(regex, content, re.MULTILINE | re.IGNORECASE | re.VERBOSE)
        raw_table = str(matches)
        table = pd.read_html(raw_table, header=0)[0]
        table.to_csv("/Users/vysocina/Desktop/ghhhhg.csv", mode="a")
    
get_table()


