#This code is for parse all information about creators from Rally (numbers and social links)

import requests
import pandas as pd
import re
import json

#create 2 dataframes for future data
rally_data_numbers = pd.DataFrame(columns = ['CirculatingSupply', 'TotalTransaction', 'TotalSupporters', 'TotalSupportVolume', 'TotalRLYBacking', 'Price', 'Symbol', 'PriceInRly', 'CoinStartingPrice'])
rally_data_links = pd.DataFrame(columns = ['name','tiktok', 'twitch', 'discord', 'metrics', 'twitter', 'youtube', 'benefits', 'facebook', 'homepage', 'telegram', 'clubhouse', 'instagram', 'preferred'])

#headers need for correct request
headers = {'User-Agent': 'Mozilla/5.0 '}

names_list = open("text.txt", "r")
names_list = names_list.read()
names = names_list.replace('\n', ' ').split(" ")
names = names[0:-1]

def get_tables(name):
    url = "https://rally.io/creator/" + name
    content = requests.get(url, headers=headers).text

    #regex1 take all numbers, that we want
    regex1 = r"({\"__typename\"[\s\w\W]*\},\"o)"

    #regex2 take links to social networks
    regex2 = r"(rl\"[\s\w\W]*},\"cr)"

    match1 = re.findall(regex1, content)
    match2 = re.findall(regex2, content)
    match = match1+match2

    #trim the data that we need for numbers
    dirty_numbers_data = match[0][0:-3]+"}"
    res = json.loads(dirty_numbers_data)
    keys = res.get("coinSummary")

    #define where we take values
    totalcoins = keys.get('totalCoins')
    tottrans = keys.get('totalTransaction')
    totsup = keys.get('totalSupporters')
    totsupvol = keys.get('totalSupportVolume')
    totrlyb = keys.get('totalRLYBacking')
    price = keys.get('price')
    symbol = keys.get('symbol')
    pricerly = keys.get('priceInRly')
    coinstartp =keys.get('coinStartingPrice')

    #add values from the webpage to dataframe
    global rally_data_numbers
    rally_data_numbers = rally_data_numbers.append({'CirculatingSupply' : totalcoins, 'TotalTransaction' : tottrans, 'TotalSupporters' : totsup, 'TotalSupportVolume' : totsupvol, 'TotalRLYBacking' : totrlyb, 'Price' : price, 'Symbol' :symbol, 'PriceInRly' : pricerly, 'CoinStartingPrice' : coinstartp}, ignore_index=True)

    #save the dataframe to csv
    rally_data_numbers.to_csv("rally_numbers.csv")

    #trim the data that we need for links to social
    dirty_links_data = match[1][4:-4]
    res2 = json.loads(dirty_links_data)

    #define the values
    name_of_coin = symbol
    tiktok = res2.get('tiktok')
    twitch = res2.get('twitch')
    discord = res2.get('discord')
    metrics = res2.get('metrics')
    twitter = res2.get('twitter')
    yt = res2.get('youtube')
    benefits = res2.get( 'benefits')
    fb = res2.get('facebook')
    hp = res2.get('homepage')
    telegram = res2.get('telegram')
    ch = res2.get('clubhouse')
    insta = res2.get('instagram')
    pref = res2.get('preferred')

    #add values from the webpage to dataframe
    global rally_data_links
    rally_data_links = rally_data_links.append({'name' : name_of_coin,'tiktok' : tiktok, 'twitch' : twitch, 'discord' : discord, 'metrics' : metrics, 'twitter' : twitter, 'youtube' : yt, 'benefits' : benefits, 'facebook' : fb, 'homepage' : hp, 'telegram' : telegram, 'clubhouse' : ch, 'instagram' : insta, 'preferred' : pref}, ignore_index=True)

    #save the dataframe to csv
    rally_data_links.to_csv("rally_links.csv")

for name in names:
    get_tables(name)
