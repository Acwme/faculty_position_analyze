import re

def choose_function_professor(index):
    switch = {
        1: parse_MIT,
        2: parse_Stanford,
        # 3: case3
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
