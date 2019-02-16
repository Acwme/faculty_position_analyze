import requests
from bs4 import BeautifulSoup
import re
import csv

list = [['school', 'name', 'title', 'web', 'phd', 'msc', 'bsc']]
with open('MIT2.csv', 'r') as f:
# with open('stanford.csv', 'r') as f:
    D_reader = csv.DictReader(f)
    for row in D_reader:
        name = row['name']
        title = row['title']
        web = row['website']

        # try:
        r = requests.get(web).content
        soup = BeautifulSoup(r, 'html.parser')

        soup.find_all('div', id_='professionalEducationContent')
        if soup.select('#professionalEducationContent'):
            edu = soup.select('#professionalEducationContent')[0].text   # '#' represent 'id', '.' represent class?
        else:
            edu = ''
            print(web)

        phd = re.findall('\nPh.+?\ (.+?)\\n', edu) if len(re.findall('\nPh.+?\ (.+?)\\n', edu)) else [0]
        msc = re.findall('\nM.+?\ (.+?)\\n', edu) if len(re.findall('\nM.+?\ (.+?)\\n', edu)) else [0]
        bsc = re.findall('\nB.+?\ (.+?)\\n', edu) if len(re.findall('\nB.+?\ (.+?)\\n', edu)) else [0]

        # except:
        #     print('error', web)
        #     continue

        list.append(['stanford', name, title, web, phd[0], msc[0], bsc[0]])

print(list)

with open('stanford_all.csv', 'w+') as f:
    writer = csv.writer(f)
    for data in list:
        writer.writerow(data)

