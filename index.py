"""
# COMMENTS : 
----------------------------------------
|       Matin Araghi - 97573150        |
|                                      |
|  Python Selenium Digikala Scraping   |
----------------------------------------

Nokte1: baraye vared kardan name mahsool , be function e main moraje konid va name mahsool ra dar varialbe product_name gharar dahid.
Nokte2: baraye inke entekhab konid chanding page search shavad, be function e main moraje konid va tedad safhe hayi ke mikhahid search sahvad ra benevisid.

*Nokte3*: khooroojie in barname ra mitavanid besorate JSON , dar file result.json ke dar hamin directory gharar darad bebinid. (price ha bar asase Toman mibashad.)

Nokte4: Chrome e shoma baiad version e 95 bashad. zira chromedriver baraie noskhe chrome version 95 download shode ast.

"""



import json

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('chromedriver', options=options)


def write_json(ads):
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(ads, f, ensure_ascii=False, indent=4)

def get_html(url):
    browser.get(url)
    return browser.page_source

def scrape_data(card):
        title = card['data-title-fa'].strip()
        price = card['data-price'].strip()

        data = {'title': title, 'price': price}

        return data

def main():

    # Write product name in product_name variable:      -default: "canon 5d"
    product_name = "canon 5d"

    # Write number of the pages that you want to search in product_pages variable:        -default: 3
    product_pages = 1

    ads_data = []

    for i in range(1, product_pages + 1):
        url = f'https://www.digikala.com/search/?q={product_name}&pageno={i}&sortby=22'
        html = get_html(url)

        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.find_all('div', {'class': 'c-product-box c-promotion-box js-product-box is-plp'})

        for card in cards:
            data = scrape_data(card)
            ads_data.append(data)

    write_json(ads_data)

    browser.close()


if __name__== '__main__':
    main()