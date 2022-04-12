import tweepy
import requests
import bs4 as bs
import os
import time
from keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()



API_key = os.getenv("API_KEY")
API_secret_key = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(API_key,API_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


def btc_info(url):
    time.sleep(2)
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text,"html.parser")
    elembtc = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > a')
    change_elem = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(1) > td:nth-child(5) > span')
    val = elembtc[0].text.strip()
    change = change_elem[0].text.strip()
    return val,change

def eth_info(url):
    time.sleep(2)
    res = requests.get(url)
    soup = bs.BeautifulSoup(res.text,"html.parser")
    elemeth = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > a')
    change_elem = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(2) > td:nth-child(5) > span')
    valeth = elemeth[0].text.strip()
    change = change_elem[0].text.strip()
    return valeth,change

def sol_info(url):
    time.sleep(4)
    res = requests.get(url)
    soup = bs.BeautifulSoup(res.text,"html.parser")
    elemsol = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(9) > td:nth-child(4) > div > a > span')
    change_elem = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(9) > td:nth-child(5) > span')
    valsol = elemsol[0].text.strip()
    change = change_elem[0].text.strip()
    return valsol,change

def Cardano_info(url):
    time.sleep(4)
    res = requests.get(url)
    soup = bs.BeautifulSoup(res.text,"html.parser")
    elemada = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(7) > td:nth-child(4) > div > a > span')
    change_elem = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(7) > td:nth-child(5) > span')
    valada = elemada[0].text.strip()
    change = change_elem[0].text.strip()
    return valada,change




def main():
    get_url = 'https://coinmarketcap.com/'
    btc,change = btc_info(get_url)
    eth,changeeth = eth_info(get_url)
    sol,changesol = sol_info(get_url)
    ada, changeada = Cardano_info(get_url)
    api.update_status(f"#Crypto #Cryptocurrency #BTC #ETH #Solana #ADA #Bitcoin \n\nBTC = {btc}\nChange = {change}\n\nETH = {eth}\nChange = {changeeth}\n\nSolana = {sol}\nChange = {changesol}\n\nADA = {ada}\nChange = {changeada}\n\n\nFollow @pricebotcrypto for hourly update!")
    keep_alive()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)