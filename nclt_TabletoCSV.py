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

#######################################################
# global possible options
nclt_b_list = [5365, 5366, 5367, 5368, 5369, 5370, 5371,
               5372, 5373, 5374, 5375, 5376, 5377, 5378, 119125, 36488]
nclt_bench_list = list(map(str, nclt_b_list))


for n in nclt_bench_list:
    url = make_nclt_url(n,)
# making URLS from desired params
nclt_url = make_nclt_url("5378", "300", "2018")


nclt_get = requests.get(nclt_url, verify=False).text
nclt_soup = BeautifulSoup(nclt_get)


# contains tables on the first page
# use table[0] for header, table[1] for first row and so on.
table = nclt_soup.find_all('tr')


# directly find tables
table = nclt_soup.find_all('table')
##################################################################

#-----------------------------------------------------------------

##################################################################

nclt_StatusofCause_dict = { 364886 : [364886] , 119125 : [119126] , 5377 : [28595] , 5378 : [5396,5395,5394] , 5376 : [5393,5392] , 5374 : [5391,5390] , 5372 : [5389] , 5370 :[5388] , 5368 : [5387], 5366 : [5386] , 5377: [5385] , 5373 : [5384], 5371 : [5383] , 5369 : [5382] , 5367 : [5381] , 5375 : [5380] , 5365 : [5379] }


#def make_nclt_StatusCauseurl(bench, sub_bench, year)

for b,sub in nclt_StatusofCause_dict.items() : 
    yr = ['2017' ,'2018', '2019']
    mon = ['1', '2','3','4', '5', '6','7', '8', '9', '10', '11','12']
    
    benchh = str(b)
    s = list(map(str,sub))
    make_nclt_StatusCauseurl (benchh,s,yr)


##################################################################
if __name__ == '__main__':
    args = parser.parse_args()
