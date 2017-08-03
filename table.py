# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


def process(url):
    r = requests.get(url)

    r.encoding = 'utf-8'

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    weekdays = soup.findAll("td", {"class": "td_cabecalho"})

    for day in weekdays:
        print(day.text)
        print(day.get('colspan'))
    return 0
