from typing import Counter
import cloudscraper  
import bs4 as bs

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
            print(f"BTC = {btc}\nChange = {change}")
            print(f"ETH = {eth}\nChange = {changeeth}")
            break
        except:
            continue