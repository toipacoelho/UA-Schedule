# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import logging

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
    
    courses = soup.findAll("td", {"class": "td_evento"})

    list=[]

    for lab in courses:
        list.append(lab.text.split(',', 1)[0])
        #print(lab.get('rowspan'))

    for each in set(list):
        print(each)
    
    
    hours = soup.find_all("td", {"class": "td_lateral"})

    list = []

    for lab in hours:
        list.append(lab.text.split(',', 1)[0])
        # print(lab.get('rowspan'))

    for each in set(list):
        print(each)

    '''

    for td in soup.find("td", {"class": "td_lateral"}).parent.find_next_siblings():
        for string in td.stripped_strings:
            print(repr(string))
    return 0

prefix="https://paco.ua.pt/H/2017_2018_1_Semestre/PUB/"

r = requests.get(prefix)
r.encoding = 'utf8'

data = r.text

soup = BeautifulSoup(data, "html.parser")

outer = soup.find("li").find("ul")

process("https://paco.ua.pt/H/2017_2018_1_Semestre/PUB/plano_8240-5_8240-5_375_11-09-2017_-_18-12-2017.html")

'''
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

    def addT(self, turma):
        logging.exception("Not yet implemented")
        return 0

    def addC(self, comp):
        logging.exception("Not yet implemented")
        return 0

class Turma:

    def __init__(self, name):
        self.name = name

    def addA(self, aula):
        logging.exception("Not yet implemented")
        return 0

class Aula:

    def __init__(self, dia, inicio, fim):
        self.dia = dia
        self.inicio = inicio
        self.fim = fim

'''


