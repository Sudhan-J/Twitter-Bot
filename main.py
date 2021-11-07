import tweepy
import cfscrape  
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
    scraper = cfscrape.create_scraper()
    scrap = scraper.get(url)
    soup = bs.BeautifulSoup(scrap.text,"html.parser")
    elembtc = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > a')
    change_elem = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(1) > td:nth-child(5) > span')
    val = elembtc[0].text.strip()
    change = change_elem[0].text.strip()
    return val,change

def eth_info(url):
    scraper = cfscrape.create_scraper()
    scrap = scraper.get(url)
    soup = bs.BeautifulSoup(scrap.text,"html.parser")
    elemeth = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > a')
    change_elem = soup.select('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div:nth-child(1) > div.h7vnx2-1.bFzXgL > table > tbody > tr:nth-child(2) > td:nth-child(5) > span')
    valeth = elemeth[0].text.strip()
    change = change_elem[0].text.strip()
    return valeth,change

def main():
    get_url = 'https://coinmarketcap.com/'
    btc,change = btc_info(get_url)
    eth,changeeth = eth_info(get_url)
    api.update_status(f"#Crypto #Cryptocurrency #BTC #ETH\nPrices!\n\nBTC = {btc}\nChange = {change}\n\nETH = {eth}\nChange = {changeeth}\n\nFollow @pricebotcrypto for hourly update!")
    

if __name__ == "__main__":
    while True:
        keep_alive()
        main()
        time.sleep(3600)