import tweepy
import cloudscraper  
import bs4 as bs
import os
import time
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
    scraper = cloudscraper.create_scraper()
    scrap = scraper.get(url)
    soup = bs.BeautifulSoup(scrap.text,"html.parser")
    elembtc = soup.select('#root > div > div.ControlHomepage__PricesTablePositioner-lzy6fr-4.JejXf > section > div > table > tbody > tr:nth-child(1) > td.styles__Column-sc-4x2924-1.AssetTableRow__AssetColumn-bzcx4v-1.AssetTableRow__PriceColumn-bzcx4v-6.dWwxMG > div > span.TextElement__Spacer-hxkcw5-0.cicsNy.Header__StyledHeader-sc-1xiyexz-0.dWwkYJ.AssetTableRow__StyledHeader-bzcx4v-12.AssetTableRow__StyledHeaderDark-bzcx4v-14.hfJTMn')
    change_elem = soup.select('#root > div > div.ControlHomepage__PricesTablePositioner-lzy6fr-4.JejXf > section > div > table > tbody > tr:nth-child(1) > td.styles__Column-sc-4x2924-1.AssetTableRow__AssetColumn-bzcx4v-1.AssetTableRow__PercentChangeColumn-bzcx4v-16.ghAXfv > span')
    val = elembtc[0].text.strip()
    change = change_elem[0].text.strip()
    return val,change

def eth_info(url):
    scraper = cloudscraper.create_scraper()
    scrap = scraper.get(url)
    soup = bs.BeautifulSoup(scrap.text,"html.parser")
    elemeth = soup.select('#root > div > div.ControlHomepage__PricesTablePositioner-lzy6fr-4.JejXf > section > div > table > tbody > tr:nth-child(2) > td.styles__Column-sc-4x2924-1.AssetTableRow__AssetColumn-bzcx4v-1.AssetTableRow__PriceColumn-bzcx4v-6.dWwxMG > div > span.TextElement__Spacer-hxkcw5-0.cicsNy.Header__StyledHeader-sc-1xiyexz-0.dWwkYJ.AssetTableRow__StyledHeader-bzcx4v-12.AssetTableRow__StyledHeaderDark-bzcx4v-14.hfJTMn')
    change_elem = soup.select('#root > div > div.ControlHomepage__PricesTablePositioner-lzy6fr-4.JejXf > section > div > table > tbody > tr:nth-child(2) > td.styles__Column-sc-4x2924-1.AssetTableRow__AssetColumn-bzcx4v-1.AssetTableRow__PercentChangeColumn-bzcx4v-16.ghAXfv > span')
    valeth = elemeth[0].text.strip()
    change = change_elem[0].text.strip()
    return valeth,change

def main():
    get_url = 'https://www.coinbase.com/'
    while(True):
        try:
            btc,change = btc_info(get_url)
            eth,changeeth = eth_info(get_url)
            api.update_status(f"#Crypto Prices!\n\nBTC = {btc}\nChange = {change}\n\nETH = {eth}\nChange = {changeeth}")
            break
        except:
            continue

def run():
    while True:
        main()
        time.sleep(3600)

if __name__ == "__main__":
    run()