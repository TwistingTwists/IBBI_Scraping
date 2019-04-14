# date = day month year
# python nclt_StatusCause.py --start-date "01 03 2019" --end-date "04 03 2019" --filename test

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
                  " with additional " + str(len(output_rows)) + '\n\n', 'red','on_yellow',['bold']))


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

def make_nclt_StatusCauseurl(bench, sub_bench, date):
    # yr = year
    bench = bench
    sub_bench = sub_bench
    [d, m, yr] = toDateStr(date)

    nclt_StatusCauseList = "https://nclt.gov.in/status-of-cause-list?field_date_value%5Bvalue%5D%5Bday%5D=" + d + "&field_date_value%5Bvalue%5D%5Bmonth%5D=" + \
        m + "&field_date_value%5Bvalue%5D%5Byear%5D=" + yr + "&field_bench_target_id=" + \
            bench + "&field_bench_court_target_id_entityreference_filter=" + sub_bench
    return nclt_StatusCauseList


###########################################
# Status Cause List
###########################################
# nclt_StatusofCause_dict = { 364886 : [364886] , 119125 : [119126] , 5377 : [28595] , 5378 : [5396,5395,5394] , 5376 : [5393,5392] , 5374 : [5391,5390] , 5372 : [5389] , 5370 :[5388] , 5368 : [5387], 5366 : [5386] , 5377: [5385] , 5373 : [5384], 5371 : [5383] , 5369 : [5382] , 5367 : [5381] , 5375 : [5380] , 5365 : [5379] }
# nclt_StatusofCause_dict = { 5374 : [5390] , 5372 : [5389] , 5370 :[5388] , 5368 : [5387], 5366 : [5386] , 5377: [5385] , 5373 : [5384], 5371 : [5383] , 5369 : [5382] , 5367 : [5381] , 5375 : [5380] , 5365 : [5379] }

sample = { 364886 : [364886] , 119125 : [119126] , 5377 : [28595] , 5378 : [5396,5395,5394] , 5376 : [5393,5392] , 5374 : [5391,5390] , 5372 : [5389] , 5370 :[5388] , 5368 : [5387], 5366 : [5386] , 5377: [5385] , 5373 : [5384], 5371 : [5383] , 5369 : [5382] , 5367 : [5381] , 5375 : [5380] , 5365 : [5379] }
nclt_StatusofCause_dict = OrderedDict() 
for k,v in sample.items():
    nclt_StatusofCause_dict[k] = v





def StatusCause( start_date, end_date, filename="StatusCause",bb=364886, ss=364886):
    start, end = datetime.datetime.strptime(
            start_date, '%d %m %Y'), datetime.datetime.strptime(end_date, '%d %m %Y')

    dates = dr(start, end)
    print(colored(dates,'yellow'))
    # print(colored(dates[0].strftime('%d %m %Y') + " to " + dates[:-1].strftime('%d %m %Y'), 'yellow'))
    
    # ----------# ----------# ----------# ----------# ----------
    # modified original dictioinary according to user input bench and sub_bench for resuming
    keys = list(nclt_StatusofCause_dict)
    bb_index = keys.index(bb)
    todel = keys[:bb_index]
    current = nclt_StatusofCause_dict[keys[bb_index]]
    if ss in current:
            current.remove(ss)
            nclt_StatusofCause_dict[keys[bb_index]] = current

    for k in todel :
        del nclt_StatusofCause_dict[k]

    # ----------# ----------# ----------# ----------# ----------
    print(colored(nclt_StatusofCause_dict,'magenta'))
    for b, sub in nclt_StatusofCause_dict.items():
        # convert bench , sub_bench string to year
        benchh = str(b)
        sub = list(map(str, sub))

        
        # all dates for each sub bench corresponding to original bench
        for s in sub:
            urls = [(make_nclt_StatusCauseurl(benchh, s, d)) for d in dates]
            print(colored("Total urls : " + str(len(urls)), 'cyan'))
            for (i, url) in enumerate(urls):
                print(colored("\nparsing: " + " bench:"+ str(b) + " Sub:"+  str(s) + " date: " + str(dates[i]) + "  " + url, 'green'))
                soup = getSoupFromURL(url)
                tables = soup.find_all('table')

                if len(tables) == 1:
                    tablesToCSV(tables[0], filename)
                else:
                    for t in tables:
                        tablesToCSV(t, filename)


if __name__ == '__main__':
    fire.Fire(StatusCause)
