import requests
from bs4 import BeautifulSoup
import csv
import re

# for datetime in urls
import datetime

####################################
# datetime for urls
####################################


def toDateStr(x): return x.strftime('%d, %m, %Y').split(',')


# start_date = 'year month date'
start_date = datetime.date(2014, 4, 4)
end_date = datetime.date(2014, 4, 10)
# end date is not inclusive.

dr = [
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
        nclt_url = "jalun"
    return nclt_url



def getLastPage(soup, el, clas):
    data = soup.find_all(el, class_=clas)
    if not data:
        print("work it.")
    else:
        return int(re.findall('\d+', str(data[0]))[0])
