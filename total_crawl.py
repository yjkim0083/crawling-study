# -*- coding: utf8 -*-

# 내장함수
from urllib.request import urlopen
# 웹에 요청한 결과를 보내주는 모듈
from bs4 import BeautifulSoup
from time import sleep
import codecs
import argparse


def gogo(page_num):
    # driver = webdriver.Chrome("./selenium/chromedriver")
    # #driver.implicitly_wait(3)
    # driver.get('http://www.ddanzi.com/free')
    # sleep(3)

    url = "http://www.ddanzi.com/index.php?mid=free&page={}".format(page_num)
    try:
        html = urlopen(url)
    except Exception as e:
        sleep(1)
        print("this page_num:{} error!!!".format(page_num))
        gogo(page_num)
    # html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    columns = soup.select('table.fz_change > tbody')[1].select('tr')

    #print(len(columns))

    columns.reverse()

    total_list = []
    for _index, _column in enumerate(columns):
        index = _column.find_all('td')
        list = []

        for i, td in enumerate(index):
            # print("{} ~ {}".format(i, td))
            if i == 0:
                if td.text.strip() == '공지':
                    break

            if i == 1:
                list.append(td.a.text.strip().replace("\t", "").replace("\n", ""))
                # http://www.ddanzi.com/index.php?mid=free&page=144980&document_srl=4299141
                href = td.find('a')['href']
                list.append("http://www.ddanzi.com/index.php?mid=free&" + href.split("&")[2])
            else:
                list.append(td.text.strip())

        if len(list) > 0:
            total_list.append('\t\t'.join(list))

    return total_list

def main(args):
    page = args.start
    end_page = args.end
    with codecs.open('ddanzi_total_{}.tsv'.format(args.start), 'a', encoding='utf8') as f:
        while True:
            result = gogo(page)
            for content in result:
                f.write(content)
                f.write('\n')

            page = page - 1
            if page < end_page:
                break
            sleep(1)


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)

args = parser.parse_args()
main(args)