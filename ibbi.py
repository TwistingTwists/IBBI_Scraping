import requests
from bs4 import BeautifulSoup
import csv
# import click
import fire
import re
from termcolor import colored
from req import getSoupFromURL, tablesToCSV
# for datetime in urls
import datetime

####################################
# urls Makers
####################################


def make_IBBI_urls(title, page=1):
    def Switching(argument):
        switcher = {
            0: "Public+Announcement+of+Corporate+Insolvency+Resolution+Process",
            1: "Public+Announcement+of+Liquidation+Process",
            2: "Public+Announcement+of+Voluntary+Liquidation+Process",
        }
        return switcher.get(argument, "__")

    # &date= 2019-04-01

    def getIBBIurls(f, title, pg):
        ibbi_CIRP = "https://ibbi.gov.in/public-announcement?ann=" + \
            Switching(0) + "&title=" + title + "&date=" + "&page=" + pg
        ibbi_LP = "https://ibbi.gov.in/public-announcement?ann=" + \
            Switching(1) + "&title=" + title + "&date=" + "&page=" + pg
        ibbi_VLP = "https://ibbi.gov.in/public-announcement?ann=" + \
            Switching(2) + "&title=" + title + "&date=" + "&page=" + pg

        return [ibbi_CIRP, ibbi_LP, ibbi_VLP]

    # [ibbi_CIRP, ibbi_LP, ibbi_VLP] = getIBBIurls(Switching, title, str(page))
    return getIBBIurls(Switching, title, str(page))


###########################################
# IBBI
###########################################
# get all three announcement links
# query = args.istr


def garbage():
    [ibbi_CIRP, ibbi_LP, ibbi_VLP] = make_IBBI_urls(query, pageNo)

    # currently only for CIRP
    soup = getSoupFromURL(ibbi_CIRP)

    # get table from ibbi.gov.in page after query has been run
    tables = soup.find_all('table')


# which = str of options among CIRP, LP, VLP
def ibbi(query, filename, lastPage=4):
    firstPage = 1

    # get last page from webpage itself
    # lastPage = getLastPage(soup, 'li', 'last')

    for i in range(firstPage, lastPage+1):
        [ibbi_CIRP, ibbi_LP, ibbi_VLP] = make_IBBI_urls(query, i)
        soup = getSoupFromURL(ibbi_CIRP)
        tables = soup.find_all('table')

        if len(tables) == 1:
            tablesToCSV(tables[0], filename)
        else:
            for t in tables:
                tablesToCSV(t, filename)


def getLastPage(soup, el, clas):
    data = soup.find_all(el, class_=clas)
    if not data:
        print("work it.")
    else:
        return int(re.findall('\d+', str(data[0]))[0])


if __name__ == '__main__':
    fire.Fire(ibbi)
