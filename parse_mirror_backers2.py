# This code is for the old mirror crowdfunds, that can't be parsed by original code

import requests
import pandas as pd


#open txt with the numbers of the contracts
contracts_list = open("contract.txt", "r")
contracts_list = contracts_list.read()
contracts = contracts_list.replace('\n', ' ').split(" ")

def get_backers(contract):
    json_data = {
        'operationName': 'CrowdfundBlockData',
        'variables': {
            'address': contract,
        },
        'query': """
            query CrowdfundBlockData($address: String!) {
                crowdfundBlockData(address: $address) {
                    backers {
                        eth
                        tokens
                        address
                        blockNumber
                        avatarURL
                        twitterUsername
                        percentage
                    }
                }
            }
        """,
    }


    response = requests.post('https://mirror-tokengate.xyz/graphql', json=json_data)
    rj = response.json()
    rrr = rj["data"]["crowdfundBlockData"]["backers"]
    df = pd.DataFrame(rrr)
    df.to_csv("mirror_backers2.csv", mode = 'a')


for contract in contracts:
    get_backers(contract)