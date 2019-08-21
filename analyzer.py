# -*- coding: utf8 -*-

import pandas as pd
import pymysql
import codecs
import datetime

data = pd.read_csv('./logs/40001_50000.log', encoding='utf-8', sep='\t\t', header=None, engine='python')
df = data.loc[:, [2,3,4,5,6,7]].copy()
df = df.drop_duplicates()
df = df.fillna('')
list = df.values.tolist()

# for i in list[0:6]:
#     print(i)

'''
['남양 볼매!', 'http://www.ddanzi.com/index.php?mid=free&document_srl=572536845', '탈퇴하고싶다', '17:34:44', nan, 0]
['아니 정당한 전형 과정을 거쳐 대학, 의전 입학했는데', 'http://www.ddanzi.com/index.php?mid=free&document_srl=572537184', 'Pizzicato_Five', '17:34:42', nan, 0]
['후쿠시마 해수가 지구를 한바퀴 돌아온다는 머저리가 아직도 있음?', 'http://www.ddanzi.com/index.php?mid=free&document_srl=572537035', '티르💬☄🈁', '17:33:55', nan, 48]
['근데 남이사 ㄴㅇ 불매를 하든말든', 'http://www.ddanzi.com/index.php?mid=free&document_srl=572537008', '아이사타', '17:33:47', nan, 15]
['남양 F&B에서 환타도 만들었다면서요~~~~???', 'http://www.ddanzi.com/index.php?mid=free&document_srl=572537000', '사소함의소중함', '17:33:45', nan, 16]
['북한 철도는 정비할곳이 한두곳이 아니라서...', 'http://www.ddanzi.com/index.php?mid=free&document_srl=572536989', '▶◀친절한밀덕후™', '17:33:43', nan, 20]
'''





db = pymysql.connect(host='192.168.100.210', port=3306, user='root', passwd='pwd123', use_unicode=True, db='HELLO_WORLD', charset='utf8mb4', autocommit=False)
cursor = db.cursor()
sql = """
insert into crawl2(DT, title, writer, like_cnt, view_cnt, url) values (%s, %s, %s, %s, %s, %s)
"""

print("START!!", datetime.datetime.now())
cnt = 0
now = datetime.datetime.now()
for line in list:
    #line = line.replace("\n", "")
    values = line

    if not values[3].startswith('2'):
        values[3] = '{}-{}-{}'.format(now.year, str(now.month).zfill(2), now.day)

    if values[4] == 'nan' or values[4] == '':
        values[4] = 0

    if values[5] == 'nan' or values[5] == '':
        values[5] = 0

    if len(values) > 6:
        print("PASS!!!!!!!!!!!", values)
        continue

    print(line)

    cursor.execute(sql, (values[3], values[0], values[2], values[4], values[5], values[1]))
    cnt += 1
    if cnt % 100 == 0:
        db.commit()

db.commit()
db.close()
print("END!!", datetime.datetime.now())






