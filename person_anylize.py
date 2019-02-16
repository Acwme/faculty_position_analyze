import requests
from bs4 import BeautifulSoup
import re
import csv


web = 'https://profiles.stanford.edu/ayfer-ozgur-aydin'


r = requests.get(web).content
soup = BeautifulSoup(r, 'html.parser')

soup.find_all('div', id_='professionalEducationContent')
if soup.select('#professionalEducationContent'):
    edu = soup.select('#professionalEducationContent')[0].text  # '#' represent 'id', '.' represent class?
else:
    edu = ''
    print(web)

phd = re.findall('\nPh.+?\ (.+?)\\n', edu) if len(re.findall('\nPh.+?\ (.+?)\\n', edu)) else [0]
msc = re.findall('\nM.+?\ (.+?)\\n', edu) if len(re.findall('\nM.+?\ (.+?)\\n', edu)) else [0]
bsc = re.findall('\nB.+?\ (.+?)\\n', edu) if len(re.findall('\nB.+?\ (.+?)\\n', edu)) else [0]


print('aaa')