#This code is for parsing all information about campaigns from mirror

import requests
import pandas as pd
import re
import json

# #headers need for correct request
headers = {'User-Agent': 'Mozilla/5.0 '}


#open txt with links to all crowdfunds
names_list = open("crowdfunds_mirror.txt", "r")
names_list = names_list.read()
names = names_list.replace('\n', ' ').split(" ")

def mirror_creators(name):
    #parse
    url = name
    content = requests.get(url, headers=headers).text

    #this give only numbers and main info about campaign
    regex1 = r"crowdfundBlockData[\s\w\W]*\"bac"
    match1 = re.findall(regex1, content, re.MULTILINE)
    dirty_data1 = "{" + match1[0][21:-5] + "}" +"}"
    res1 = json.loads(dirty_data1)
    dataframe1 = pd.DataFrame.from_dict(res1, orient="index")
    dataframe1.to_csv('mirror_creators.csv', mode = 'a')

    #this give all the backers for each campaign
    regex2=r",\"backers[\s\w\W]*\"events"
    match2 = re.findall(regex2, content, re.MULTILINE)
    res2 = json.loads(match2[0][11:-8])
    dataframe2 = pd.DataFrame.from_dict(res2)
    dataframe2['name'] = url
    dataframe2.to_csv('mirror_backers.csv', mode = 'a')


for name in names:
    mirror_creators(name)
    