import warnings
import contextlib
import csv
from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning
from termcolor import colored

old_merge_environment_settings = requests.Session.merge_environment_settings


@contextlib.contextmanager
def no_ssl_verification():
    opened_adapters = set()

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        # Verification happens only once per connection so we need to close
        # all the opened adapters once we're done. Otherwise, the effects of
        # verify=False persist beyond the end of this context manager.
        opened_adapters.add(self.get_adapter(url))

        settings = old_merge_environment_settings(
            self, url, proxies, stream, verify, cert)
        settings['verify'] = False

        return settings

    requests.Session.merge_environment_settings = merge_environment_settings

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', InsecureRequestWarning)
            yield
    finally:
        requests.Session.merge_environment_settings = old_merge_environment_settings

        for adapter in opened_adapters:
            try:
                adapter.close()
            except:
                pass


def getSoupFromURL(url):
    """ get beautifulsoup from url without sslwarmings"""
    with no_ssl_verification():
        getme = requests.get(url, verify=False)
        # soup = BeautifulSoup(getme.content, "html5lib")
        soup = BeautifulSoup(getme.content, "lxml")
    return soup


def tablesToCSV(table, filename):
    """ take html table and filename to save it to"""
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
