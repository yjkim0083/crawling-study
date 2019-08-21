# -*- coding: utf8 -*-

import pandas as pd
import pymysql
import codecs
import datetime

# data = pd.read_csv('./ddanzi_total-2.tsv', encoding='utf-8', sep='\t\t', header=None, engine='python')
#
# print(len(data.duplicated() == True))





db = pymysql.connect(host='192.168.100.210', port=3306, user='root', passwd='pwd123', use_unicode=True, db='HELLO_WORLD', charset='utf8mb4', autocommit=False)
cursor = db.cursor()
sql = """
insert into crawl2(DT, title, writer, like_cnt, view_cnt) values (%s, %s, %s, %s, %s)
"""


lines = None
with codecs.open("ddanzi-preprocess.tsv", "r", encoding='utf8') as f:
    lines = f.readlines()

print("START!!", datetime.datetime.now())
cnt = 0
for line in lines:
    line = line.replace("\n", "")
    values = line.split("|")

    if len(values) > 5:
        print("PASS!!!!!!!!!!!", values)
        continue
    print(values)

    cursor.execute(sql, (values[2], values[0], values[1], values[3] if values[3] != '' else 0  , values[4] if values[4] != '' else 0))
    cnt += 1
    if cnt % 100 == 0:
        db.commit()

db.commit()
db.close()
print("END!!", datetime.datetime.now())






