#!/usr/bin/env python3
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'
uClient = uReq(my_url) #opens connection and "grabs" webpage and downloads webpage
page_html = uClient.read() 
uClient.close()
page_soup = soup(page_html, "html.parser") #html parsing

#grabs each product on page
containers = page_soup.findAll("div", {"class": "item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip() #.strip removes whitespace before and after new lines
    
    offer_container = container.findAll("p", {"class": "item-promo"})
    offer = offer_container[0].text.strip()

    print("Brand:", brand)
    print("Product Name:", product_name)
    print("Offer:", offer)
    print("Shipping:", shipping)
    print("\n")

