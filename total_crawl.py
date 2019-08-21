# -*- coding: utf8 -*-

# 내장함수
from urllib.request import urlopen
# 웹에 요청한 결과를 보내주는 모듈
from bs4 import BeautifulSoup
from time import sleep
import codecs


def gogo(page_num):
    # driver = webdriver.Chrome("./selenium/chromedriver")
    # #driver.implicitly_wait(3)
    # driver.get('http://www.ddanzi.com/free')
    # sleep(3)

    url = "http://www.ddanzi.com/index.php?mid=free&page={}".format(page_num)
    print("url => {}".format(url))
    html = urlopen(url)
    # html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    columns = soup.select('table.fz_change > tbody > tr')
    columns.reverse()

    total_list = []
    for _index, _column in enumerate(columns[:-6]):
        index = _column.find_all('td')
        list = []

        for i, td in enumerate(index):
            # print("{} ~ {}".format(i, td))
            if i == 1:
                list.append(td.a.text.strip().replace("\t", "").replace("\n", ""))
            else:
                list.append(td.text.strip())

        total_list.append('\t\t'.join(list))

    return total_list

def main():
    page = 144980
    with codecs.open('ddanzi_total.tsv', 'a', encoding='utf8') as f:
        while True:
            result = gogo(page)
            for content in result:
                f.write(content)
                f.write('\n')

            page = page - 1
            if page == 0:
                break
            sleep(1)


if __name__=="__main__":
    main()