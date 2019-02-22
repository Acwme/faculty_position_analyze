import re

def choose_function_professor(index):
    switch = {
        1: parse_MIT,
        2: parse_Stanford,
        3: parse_Berkeley,
        4: parse_Caltech,
        5: parse_Michigan,
        6: parse_CMU,

    }
    function_faculty = switch[index]
    return function_faculty


def parse_MIT(soup):
    pass


def parse_Stanford(soup):
    soup.find_all('div', id_='professionalEducationContent')
    if soup.select('#professionalEducationContent'):
        edu = soup.select('#professionalEducationContent')[0].text  # '#' represent 'id', '.' represent class?
    else:
        edu = ''

    phd = re.findall('\nPh.+?\ (.+?)\\n', edu) if len(re.findall('\nPh.+?\ (.+?)\\n', edu)) else [0]
    msc = re.findall('\nM.+?\ (.+?)\\n', edu) if len(re.findall('\nM.+?\ (.+?)\\n', edu)) else [0]
    bsc = re.findall('\nB.+?\ (.+?)\\n', edu) if len(re.findall('\nB.+?\ (.+?)\\n', edu)) else [0]

    # except:
    #     print('error', web)
    #     continue

    list=[phd[0], msc[0], bsc[0]]

    return list


def parse_Berkeley(soup):
    edu = soup.find_all('section', class_='section publications')[0]

    phd = re.findall(' (Ph.*)', str(edu)) if len(re.findall(' (Ph.*)', str(edu))) else [0]
    msc = re.findall(' (M.*)', str(edu)) if len(re.findall(' (M.*)', str(edu))) else [0]
    bsc = re.findall(' (B.*)', str(edu)) if len(re.findall(' (B.*)', str(edu))) else [0]


    list=[phd[0], msc[0], bsc[0]]

    return list




def parse_Caltech(soup):
    edu = soup.find_all('section', class_='section publications')[0]

    phd = re.findall(' (Ph.*)', str(edu)) if len(re.findall(' (Ph.*)', str(edu))) else [0]
    msc = re.findall(' (M.*)', str(edu)) if len(re.findall(' (M.*)', str(edu))) else [0]
    bsc = re.findall(' (B.*)', str(edu)) if len(re.findall(' (B.*)', str(edu))) else [0]


    list=[phd[0], msc[0], bsc[0]]

    return list

def parse_Michigan(soup):
    edu = soup.find_all('section', class_='section publications')[0]

    phd = re.findall(' (Ph.*)', str(edu)) if len(re.findall(' (Ph.*)', str(edu))) else [0]
    msc = re.findall(' (M.*)', str(edu)) if len(re.findall(' (M.*)', str(edu))) else [0]
    bsc = re.findall(' (B.*)', str(edu)) if len(re.findall(' (B.*)', str(edu))) else [0]


    list=[phd[0], msc[0], bsc[0]]

    return list

def parse_CMU(soup):
    text = str(soup.select('p'))
    phd = re.findall('<p>Ph.*?([a-zA-Z >]University [a-zA-Z ,]*)</p>', text) if len(re.findall('<p>Ph.*?([a-zA-Z >]University [a-zA-Z ,]*)</p>', text)) else [0]
    msc = re.findall('<p>M.*?([a-zA-Z >]University [a-zA-Z ,]*)</p>', text) if len(re.findall('<p>M.*?([a-zA-Z >]University [a-zA-Z ,]*)</p>', text)) else [0]
    bsc = re.findall('<p>B.*?([a-zA-Z >]University [a-zA-Z ,]*)</p>', text) if len(re.findall('<p>B.*?([a-zA-Z >]University [a-zA-Z ,]*)</p>', text)) else [0]



    list=[phd[0], msc[0], bsc[0]]

    return list