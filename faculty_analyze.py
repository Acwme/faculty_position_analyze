import requests
from bs4 import BeautifulSoup
import csv
import function_parse_faculty_web as ff
import function_parse_professor_web as fp

def geturl(index):

    url = {
        1:'http://www.eecs.mit.edu/people/faculty-advisors',
        2:'https://ee.stanford.edu/people/faculty?sort=1&filter=0&area=9505&page=0&results=64',
        3:'https://www2.eecs.berkeley.edu/Faculty/Lists/list.html?_ga=2.63704108.2049483718.1550803104-822994221.1550803104',
        # 4:
        5:'https://www.eecs.umich.edu/eecs/faculty/eecsfaculty.html',
        6: 'https://www.ece.cmu.edu/directory/faculty.html',
    }

    return url[index]



def request_web(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser') #使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出
    return soup     #return binary data



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
    index = 6
    url = geturl(index)
    soup = request_web(url)
    function_faculty = ff.choose_function_faculty(index)
    professor_list = function_faculty(soup)
    print(professor_list)
    total_list = [['name', 'title', 'professor_web', 'phd', 'msc', 'bsc']]
    for n in range(1, len(professor_list)):
        professor_name = professor_list[n][0]
        professor_title = professor_list[n][1]
        professor_web = professor_list[n][2]

        prof_soup = request_web(professor_web)
        function_professor = fp.choose_function_professor(index)
        professor_education = function_professor(prof_soup)
        professor_info = professor_list[n]+professor_education
        # print(professor_info)
        total_list.append(professor_info)
    print(total_list)

    # savecsv('MIT2.csv', weblist)
    # CV = get_CV('stanford.csv')
    # for personal_web in CV:
    #     print(personal_web)


