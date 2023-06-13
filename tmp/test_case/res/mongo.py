# coding:utf-8
# Name:mongo.py
# Author:nigo
# Time:2021/12/9 6:13 下午 
# Description:
import pymongo
from datetime import date

from dateutil import parser
from datetime import datetime

# dateStr = '2021-12-27T01:58:33.000Z'
# myDatetime = parser.parse(dateStr)
# print(myDatetime)

# myclient = pymongo.MongoClient(
#     'mongodb://root:wTGucEb5gyM3rGiS@dds-uf6801b7014281841601-pub.mongodb.rds.aliyuncs.com:3717,dds-uf6801b7014281842872-pub.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-58136126')
# db = myclient['dukang_tna_dktest1']
# col = db.rests
# col.insert_one({
#     "_id": "923948417211111111",
#     "companyId": "2323",
#     "name": "rest_namne_01",
#     "code": "rest_namne_01",
#     "period": {
#         "start": {
#             "offset": "THE_DAY",
#             "time": "15:00"
#         },
#         "end": {
#             "offset": "THE_DAY",
#             "time": "16:00"
#         }
#     },
#     "createTime": {
#         "dateTime": datetime.strptime("2020-02-06 16:11:18","%Y-%m-%d %H:%M:%S"),
#         "zone": "Asia/Shanghai"
#     },
#     "deleted": False,
#     "_class": "com.bipocloud.dukang.tna.config.domain.Rest"
# })

# date.string_toDatetime
a = datetime.strptime("2020-02-06 16:11:18","%Y-%m-%d %H:%M:%S")

b = datetime.today()
# print(a)
# print(type(a))
print(b)
print(type(b))
