import requests
from bs4 import BeautifulSoup
from urls import make_nclt_StatusCauseurl, make_nclt_url

# making URLS from desired params
nclt_url = make_nclt_url("5378", "300", "2018")


nclt_get = requests.get(nclt_url, verify=False).text
nclt_soup = BeautifulSoup(nclt_get)


# contains tables on the first page
# use table[0] for header, table[1] for first row and so on.
table = nclt_soup.find_all('tr')
