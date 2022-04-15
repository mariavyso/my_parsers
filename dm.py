from bs4 import BeautifulSoup
import requests
import pandas as pd

# For last_page you should write the number of the last page for your link
def get_table(last_page):
    # Defining of the dataframe
    df = pd.DataFrame(columns=['No', 'Ticker', 'Company', 'Sector', 'Industry', 'Country', 'Market Cap', 'P/E', 'Price', 'Change', 'Volume'])
    # Definig user agent
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # Script to parse all pages from first to last
    for n in range(0,last_page):
        n = 21+(n-1)*20
        print(n)
        url = f'https://finviz.com/screener.ashx?v=111&f=idx_sp500&r={n}'
        print(url)
        content = requests.get(url, headers=headers).text
        soup = BeautifulSoup(content, features="html.parser")
        table = soup.find('table', class_='table-light')
   
    # Collecting rows
        for row in table.findAll('tr', attrs={"valign": "top"}):
            columns = row.findAll('td')
            if(columns != []):
                no = columns[0].text.strip()
                ticker = columns[1].text.strip()
                company = columns[2].text.strip()
                sector = columns[3].text.strip()
                industry = columns[4].text.strip()
                country = columns[5].text.strip()
                marketcap =columns[6].text.strip()
                pe = columns[7].text.strip()
                price = columns[8].text.strip()
                change = columns[9].text.strip()
                volume =columns[10].text.strip()
    # Add values to dataframe
                df = df.append({'No': no, 'Ticker':ticker, 'Company' : company, 'Sector':sector, 'Industry':industry, 'Country':country, 'Market Cap':marketcap, 'P/E':pe, 'Price':price, 'Change':change, 'Volume':volume}, ignore_index=True)
    # Save Dataframe to csv
        df.to_csv('/Users/......name.csv')
            
    return 








