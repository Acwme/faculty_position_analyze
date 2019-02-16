import requests
from bs4 import BeautifulSoup
import re
import csv


class base():
    def __init__(self):
        # super(base, self).__init__()
        pass

    def bs4url(self, url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        return soup


    def savecsv(self, filename, list):
        with open(filename, 'w+') as f:
            writer = csv.writer(f)
            for data in list:
                writer.writerow(data)


    def get_CV(self, filename):
        content = []
        with open(filename, 'r') as f:
            D_reader=csv.DictReader(f)
            for row in D_reader:
                print(row['website'])
        return content