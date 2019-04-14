import requests
from bs4 import BeautifulSoup
import csv
import fire
import re
from termcolor import colored
from collections import OrderedDict
# for datetime in urls
import datetime

####################################
# general funcs
####################################


def getSoupFromURL(url):
    getme = requests.get(url, verify=False)
    # soup = BeautifulSoup(getme.content, "html5lib")
    soup = BeautifulSoup(getme.content, "lxml")
    return soup


def tablesToCSV(table, filename):
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)

    with open(filename + '.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)
    print(colored("Written " + filename + ".csv " +
                  " with additional " + str(len(output_rows)) + '\n\n', 'red', 'on_yellow', ['bold']))


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

    field_bench_target_id = bench
    title = title
    year = year
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
        return int(re.findall('\d+', str(data[0]))[0])


def ibbi(bench, title, filename, lastPage=4):
    firstPage = 1

    # get last page from webpage itself
    # lastPage = getLastPage(soup, 'li', 'last')

    for i in range(firstPage, lastPage+1):
        url = make_nclt_url(bench, title, i)
        soup = getSoupFromURL(url)
        tables = soup.find_all('table')

        if len(tables) == 1:
            tablesToCSV(tables[0], filename)
        else:
            for t in tables:
                tablesToCSV(t, filename)


if __name__ == '__main__':
    fire.Fire(NCLT)
