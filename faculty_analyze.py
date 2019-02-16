import requests
from bs4 import BeautifulSoup
import re
import csv

def geturl():

    url = 'http://www.eecs.mit.edu/people/faculty-advisors'

    return url



def requesthtml(url):

    r = requests.get(url)
    # print(r.url)         # url
    return r.content     #return binary data

def parseHTML(html):
    soup = BeautifulSoup(html, 'html.parser') #使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出
    people = soup.find_all('div', class_='postcard-left clearfix')
    file = [['name', 'title', 'website']]
    for person in people:

        name = person.select('h3 a')[0].text
        title = person.select('h3 small span')[0].text
        web = re.findall('<a.+?href=\"(.+?)\".*>Website</a>', str(person.select('div a')))
        if name and title and web:
            file.append([name, title, web[0]])

    return file


def parseMIT(html):
    soup = BeautifulSoup(html, 'html.parser')  # 使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出
    people = soup.select('#block-system-main > div > div > div > div.view-content > div > ul > li')
    file = [['name', 'title', 'website']]
    for person in people:

        name = person.select('div.views-field.views-field-title > span > a')
        if name:
            name = name[0].text
            title = person.select('div.views-field.views-field-field-person-title > div.field-content')[0].text
            web = re.findall('<a.+?href=\"(.+?)\".*</a>', str(person.select('div.views-field.views-field-title > span > a')))[0]
            file.append([name, title, web])

    return file

def savecsv(filename, list):
    with open(filename, 'w+') as f:
        writer = csv.writer(f)
        for data in list:
            writer.writerow(data)

def get_CV(filename):
    content = []
    with open(filename, 'r') as f:
        D_reader=csv.DictReader(f)
        for row in D_reader:
            print(row['website'])
    return content


if __name__ == '__main__':
    url = geturl()
    html = requesthtml(url)
    weblist = parseMIT(html)
    savecsv('MIT2.csv', weblist)
    # CV = get_CV('stanford.csv')
    # for personal_web in CV:
    #     print(personal_web)


