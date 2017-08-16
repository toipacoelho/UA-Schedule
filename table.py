# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


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

