import tweepy
import os
import time
import requests
import json
from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

API_key = os.getenv("API_KEY")
API_secret_key = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
}
session = requests.Session()
session.headers.update(headers)

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


def bitcoin_price():
    PARAMS = {'slug': 'bitcoin', 'convert': 'USD'}
    response_from_server = session.get(URL, params=PARAMS)
    value = json.loads(
        response_from_server.text)['data']['1']['quote']['USD']['price']
    change = json.loads(response_from_server.text
                        )['data']['1']['quote']['USD']['percent_change_1h']
    return round(value, 2), round(change, 3)


def ethereum_price():
    PARAMS = {'slug': 'ethereum', 'convert': 'USD'}
    response_from_server = session.get(URL, params=PARAMS)
    value = json.loads(
        response_from_server.text)['data']['1027']['quote']['USD']['price']
    change = json.loads(response_from_server.text
                        )['data']['1027']['quote']['USD']['percent_change_1h']
    return round(value, 2), round(change, 3)


def bnb_price():
    PARAMS = {'slug': 'bnb', 'convert': 'USD'}
    response_from_server = session.get(URL, params=PARAMS)
    value = json.loads(
        response_from_server.text)['data']['1839']['quote']['USD']['price']
    change = json.loads(response_from_server.text
                        )['data']['1839']['quote']['USD']['percent_change_1h']
    return round(value, 2), round(change, 3)


def solana_price():
    PARAMS = {'slug': 'solana', 'convert': 'USD'}
    response_from_server = session.get(URL, params=PARAMS)
    value = json.loads(
        response_from_server.text)['data']['5426']['quote']['USD']['price']
    change = json.loads(response_from_server.text
                        )['data']['5426']['quote']['USD']['percent_change_1h']
    return round(value, 2), round(change, 3)


def doge_price():
    PARAMS = {'slug': 'dogecoin', 'convert': 'USD'}
    response_from_server = session.get(URL, params=PARAMS)
    # data = json.loads(response_from_server.text)
    value = json.loads(
        response_from_server.text)['data']['74']['quote']['USD']['price']
    change = json.loads(response_from_server.text
                        )['data']['74']['quote']['USD']['percent_change_1h']
    return round(value, 5), round(change, 3)
    # pprint.pprint(data)


def main():
    btc, btc_change = bitcoin_price()
    eth, eth_change = ethereum_price()
    bnb, bnb_change = bnb_price()
    sol, sol_change = solana_price()
    api.update_status(
        f"#Crypto #Cryptocurrency #BTC #ETH #BNB #Solana #Bitcoin\n\nBTC = ${btc}\nChange = {btc_change}%\n\nETH = ${eth}\nChange = {eth_change}%\n\nBNB = ${bnb}\nChange = {bnb_change}%\n\nSolana = ${sol}\nChange = {sol_change}%\n\nFollow @CryptoPriceBot_ for hourly update!"
    )
    keep_alive()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)
