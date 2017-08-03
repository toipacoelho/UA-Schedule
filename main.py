# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import table

prefix="https://paco.ua.pt/H/2017_2018_1_Semestre/PUB/"

r = requests.get(prefix)

r.encoding = 'utf8'

data = r.text

soup = BeautifulSoup(data, "html.parser")

outer = soup.find("li").find("ul")

for li in outer.find_all("li", recursive=False):
    print(li.contents[0])

for li in outer.find_all("li", recursive=False):
    if "TELEMÁTICA" in li.contents[0]:
        print()
        for link in li.contents[1].find_all('a'):
            print(link.get('href'))
            table.process(prefix + link.get('href'))
