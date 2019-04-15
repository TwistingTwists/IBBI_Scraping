import requests
from bs4 import BeautifulSoup
import csv
import fire
import re
from termcolor import colored
from collections import OrderedDict
# for datetime in urls
import datetime
from req import no_ssl_verification, getSoupFromURL, tablesToCSV


####################################
# datetime for urls
####################################


def toDateStr(x):
    [d, m, yr] = x.strftime('%d, %m, %Y').split(',')
    # make sure no spaces left in date
    [dd, mm, yy] = [d.replace(" ", ""), m.replace(
        " ", ""), yr.replace(" ", "")]
    # make sure no zeroes before dates
    return [dd.replace("0", ""), mm.replace("0", ""), yy]


# start_date = 'year month date'
start_date = datetime.date(2014, 4, 4)
end_date = datetime.date(2014, 4, 10)
# end date is not inclusive.
yr = ['2017', '2018', '2019']
mon = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def dr(start_date, end_date):
    return [
        datetime.date.fromordinal(ordinal)
        for ordinal in range(
            start_date.toordinal(),
            end_date.toordinal(),
        )
    ]


####################################
# urls Makers
####################################

def make_nclt_url(bench, title, year, page=1):

    # convert to string
    field_bench_target_id, title, year = list(map(str, [bench, title, year]))

    if page == 1:
        nclt_url = "https://nclt.gov.in/order-judgements?field_bench_target_id=" + field_bench_target_id + "&field_search_date_value_1%5Bmin%5D%5Bdate%5D=&field_search_date_value_1%5Bmax%5D%5Bdate%5D=&title=" + title + \
            "&field_search_date_value%5Bvalue%5D%5Byear%5D=" + year + \
            "&field_name_of_petitioner_value=&field_name_of_respondent_value=&field_search_date_value%5Bvalue%5D%5Byear%5D=&advocate_name=&field_search_date_value%5Bvalue%5D%5Byear%5D="
    else:
        nclt_url = "https://nclt.gov.in/order-judgements?field_bench_target_id=" + field_bench_target_id + "&field_search_date_value_1%5Bmin%5D%5Bdate%5D=&field_search_date_value_1%5Bmax%5D%5Bdate%5D=&title=" + title + \
            "&field_search_date_value%5Bvalue%5D%5Byear%5D=" + year + \
            "&field_name_of_petitioner_value=&field_name_of_respondent_value=&field_search_date_value%5Bvalue%5D%5Byear%5D=&advocate_name=&field_search_date_value%5Bvalue%5D%5Byear%5D=" + \
            "&page=" + str(page-1)
    return nclt_url


def getLastPage(soup, el, clases):
    data = soup.find_all(el, {'class': clases})
    if not data:
        print("work it.")
    else:
        st = data[0].find('a').get('href')

        pageEqualNo = re.findall(r'\bpage=\d+\b', st)

        return pageEqualNo[0][5:]


def nclt(bench, title, filename, yr=2018, lastPage=5):

    # for pg in range(firstPage+1, lastPage+1):
    pg = 1
    while pg < lastPage+1:
        print('\n\tgetting URLS from ' + str(pg) + 'to ' + str(lastPage+1))
        urls = [make_nclt_url(bench, title, yr, p)
                for p in range(pg, lastPage+1)]
        for i, url in enumerate(urls):
            print("url for loop: ", str(i))
            # print(colored(" pageNo: " + str(pg) + "\n", 'green'))
            print(url)
            soup = getSoupFromURL(url)

            # find tables and write to file.
            tables = soup.find_all('table')

            if len(tables) == 1:
                tablesToCSV(tables[0], filename)
            else:
                for t in tables:
                    tablesToCSV(t, filename)

        # get last page from webpage itself
        lp = getLastPage(soup, 'li', ['pager-last'])
        if lp:
            lastPage = int(lp)
            print(colored("\nActual lastpage = " + str(lastPage), 'magenta'))
        else:
            lastPage = pg
            print("only one page!\n", lastPage)

        pg += 1


def nclt_allBench(start, end, filename, yr=2018, lastPage=5):
    # bench = [5365, 5366, 5367, 5368, 5369, 5370, 5371, 5372,5373, 5374, 5375, 5376, 5377, 5378, 119125, 364886]
    bench = [5378]
    for cp in range(start, end):
        for b in bench:
            print(colored("\n Bench: " + str(b) + " cp: " + str(cp), 'magenta'))
            nclt(b, cp, filename, yr, lastPage)


if __name__ == '__main__':
    fire.Fire(nclt_allBench)
