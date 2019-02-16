import requests
from bs4 import BeautifulSoup
import re
import csv
from base import base

class university(base):
    def __init__(self):
        super(university, self).__init__()
        self.faculty_url = 'https://ee.stanford.edu/people/faculty?sort=1&filter=0&area=9505&page=0&results=64'
        self.file = [['school', 'name', 'title', 'website']]
        self.edu = ['phd', 'msc', 'bs']
        self.school_name = 'stanford'


    # def parse_person(self):
    #     for person in self.file:
    #         person_url = person[2]
    #         soup = self.bs4url(person_url)
    #         soup.find_all('div', id_='professionalEducationContent')
    #         edu = soup.select('#professionalEducationContent')[0].text   # '#' represent 'id', '.' represent class?
    #         phd = re.findall('PhD,\ (.+?)\\n', edu)[0]
    #         msc = re.findall('M.S.,\ (.+?)\\n', edu)[0]
    #         bs = re.findall('B.S.,\ (.+?)\\n', edu)[0]





    def parse_faculty(self):
        soup = self.bs4url(self.faculty_url)
        for person in people:

            name = person.select('h3 a')[0].text
            title = person.select('h3 small span')[0].text
            web = re.findall('<a.+?href=\"(.+?)\".*>Website</a>', str(person.select('div a')))
            if name and title and web:
                self.file.append([self.school_name, name , title, web[0]])


        return self.file







if __name__ == '__main__':
    # print('what is going on')
    a = university()
    a.parse_faculty()
     KL