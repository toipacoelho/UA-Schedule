# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import table

def process(url):
    r = requests.get(url)

    r.encoding = 'utf-8'

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    '''
    weekdays = soup.findAll("td", {"class": "td_cabecalho"})

    for day in weekdays:
        print(day.text)
        print(day.get('colspan'))
    return 0
    '''
    courses = soup.findAll("td", {"class": "td_evento"})

    list=[]

    for lab in courses:
        list.append(lab.text.split(',', 1)[0])
        #print(lab.get('rowspan'))

    for each in set(list):
        print(each)

    return 0

prefix="https://paco.ua.pt/H/2017_2018_1_Semestre/PUB/"

r = requests.get(prefix)

r.encoding = 'utf8'

data = r.text

soup = BeautifulSoup(data, "html.parser")

outer = soup.find("li").find("ul")

#for li in outer.find_all("li", recursive=False):
    #print(li.contents[0])

for li in outer.find_all("li", recursive=False):
    if "TELEMÁTICA" in li.contents[0]:
        print()
        for link in li.contents[1].find_all('a'):
            print("ANO: " + link.get('href')[11])
            process(prefix + link.get('href'))

class Cadeira:

    def __init__(self, name, code):
        self.name = name
        self.code = code


