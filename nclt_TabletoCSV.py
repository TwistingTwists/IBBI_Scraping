import requests
from bs4 import BeautifulSoup
from urls import make_nclt_StatusCauseurl, make_nclt_url


import argparse


parser = argparse.ArgumentParser(description='NCLT or CauseList or IBBI')
parser.add_argument(
    '-n', '--nclt', help='NCLT', required=True)
parser.add_argument(
    '-c', '--cause', help='Status Cause List ', required=False)
parser.add_argument(
    '-i', '--ibbi', help='IBBI Database', required=False)


# making URLS from desired params
nclt_url = make_nclt_url("5378", "300", "2018")


nclt_get = requests.get(nclt_url, verify=False).text
nclt_soup = BeautifulSoup(nclt_get)


# contains tables on the first page
# use table[0] for header, table[1] for first row and so on.
table = nclt_soup.find_all('tr')


if __name__ == '__main__':
    args = parser.parse_args()
