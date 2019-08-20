# -*- coding: utf8 -*-

# 내장함수
from urllib.request import urlopen
# 웹에 요청한 결과를 보내주는 모듈
from bs4 import BeautifulSoup
from time import sleep
import codecs
import datetime




def write(list):
    with codecs.open('ddanzi.tsv', 'a', encoding='utf8') as f:
        for result in list:
            f.write(result)
            f.write('\n')

def check_lastnumber(action, lastnumber):
    result = 0
    if action == "write":
        with open('lastnumber.txt', 'w') as f:
            f.write(str(lastnumber))
    else:
        with open('lastnumber.txt', 'r') as f:
            result = f.readline()

    return result

def gogo():
    # driver = webdriver.Chrome("./selenium/chromedriver")
    # #driver.implicitly_wait(3)
    # driver.get('http://www.ddanzi.com/free')
    # sleep(3)

    url = "http://www.ddanzi.com/free"
    html = urlopen(url)
    # html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    columns = soup.select('table.fz_change > tbody > tr')
    columns.reverse()

    total_list = []
    length = len(columns[:-6])
    lastnumber = int(check_lastnumber("read", ""))
    for _index, _column in enumerate(columns[:-6]):
        index = _column.find_all('td')
        list = []
        isExist = False

        for i, td in enumerate(index):
            now = datetime.datetime.now()
            # print("{} ~ {}".format(i, td))
            if i == 0:
                # print("{} - {}".format(td.text.strip(), lastnumber))
                if int(td.text.strip()) <= lastnumber:
                    isExist = True
                    break

                if _index == length - 1:
                    lastnumber = int(td.text.strip())

            if i == 1:
                list.append(td.a.text.strip().replace("\t", "").replace("\n", ""))
            elif i == 3:
                list.append('%s-%s-%s' % (now.year, str(now.month).zfill(2), now.day) + ' ' + td.text.strip())
            else:
                list.append(td.text.strip())

        if isExist:
            continue

        print('\t\t'.join(list))
        total_list.append('\t\t'.join(list))

    write(total_list)
    print('-----------------------------')
    check_lastnumber("write", lastnumber)

def main():
    while True:
        gogo()
        sleep(20)


if __name__=="__main__":
    main()