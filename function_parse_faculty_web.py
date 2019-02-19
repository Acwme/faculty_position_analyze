import re

def choose_function_faculty(index):
    switch = {
        1: parse_MIT,
        2: parse_Stanford,
        # 3: case3
    }
    function_faculty = switch[index]
    return function_faculty







def parse_MIT(soup):
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




def parse_Stanford(soup):
    people = soup.find_all('div', class_='postcard-left clearfix')
    file = [['name', 'title', 'website']]
    for person in people:

        name = person.select('h3 a')[0].text
        title = person.select('h3 small span')[0].text
        web = re.findall('<a.+?href=\"(.+?)\".*>Website</a>', str(person.select('div a')))
        if name and title and web:
            file.append([name, title, web[0]])

    return file