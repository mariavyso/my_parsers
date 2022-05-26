from itertools import product
import json
from string import ascii_lowercase
from time import sleep
import requests
import pandas as pd
df = pd.DataFrame(columns = ['key'])

headers = {
    'user-agent': 'Mozilla/5.0'
}

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]


for key in keywords:

    url = 'https://www.patreon.com/api/search?q=' + str(key) + '&page%5Bsize%5D=1000&src=navbar&json-api-version=1.0'
    sleep(0.5)

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        total = data['meta']['hits_total']
    except:
        data = []
        total = 99999

    if total > 1000:
        table = df.append({'key' : key}, ignore_index = True)
        table.to_csv('more_than_1000.csv', mode = 'a')
        print(key, 'not happy', total)
    
    else:
        filename = f'{key}.json'
        with open(filename, 'w') as f:
            json.dump(data, f)
            f.close()
            print(key, 'happy', total)
        










