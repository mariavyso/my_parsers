import requests
import pandas as pd
import re

#create new dataframe
df = pd.DataFrame(columns=["views", "subscribers", "joined"])

#open txt with youtube names
names_list = open("yt_names.txt", "r")
names_list = names_list.read()
names = names_list.replace('\n', ' ').split(" ")

headers = {'User-Agent': 'Mozilla/5.0 '}

def parse_yt(name):
    #parse
    url = f"https://www.youtube.com/" + name
    r = requests.get(url)

    mtc = re.search(r"var ytInitialData = (.*?);</script>", r.text, re.DOTALL)
    yt_init_str = mtc.group(1)

    mtc = re.search(r'"viewCountText":{"simpleText":"(.*?) views"}', yt_init_str)
    views = mtc.group(1)

    mtc = re.search(r'subscribers"}},"simpleText":"(.*?) subscribers"}', yt_init_str)
    subscribers = mtc.group(1)

    mtc = re.search(r'"text":"Joined "},{"text":"(.*?)"}', yt_init_str)
    joined = mtc.group(1)

    #append new data to the dataframe
    yt_table = df.append({"views" : views, "subscribers" : subscribers, "joined" : joined},  ignore_index=True)

    #save to csv
    yt_table.to_csv("yt_data.csv", mode="a")
    

for name in names:
    try:
        parse_yt(name)
    except:
        print(name, "error")



