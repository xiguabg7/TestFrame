# coding:utf-8
# Name:pandas_match1.py
# Author:nigo
# Time:2021/3/29 5:31 下午 
# Description:
import json

import numpy as np
import pandas as pd
from faker import Faker
import requests


def match_staff_name():
    # 读取目标表（workio内的人员名字）
    df1 = pd.read_excel(r'../test_data/1.xlsx', 'Sheet1')
    # 读取参考表（考勤机的人员3项信息）
    df2 = pd.read_excel(r'../test_data/2.xlsx', 'Sheet1')
    # 进行合并，重点看on参数，on参数指的是依据哪一列进行合并，当然也可以添加两列
    # 值得注意的是，此处无论依据哪一列或者哪几列进行合并，均需要尽量确保此列或者
    # 此几列中的值能够是唯一的，否则容易出错
    df = pd.merge(df1, df2, how='left', on=['name'])
    #导出到res（workio内的人员3项信息）
    df.to_excel(r'../test_data/res.xlsx', 'Sheet1', index=None)
    # df.stack()[lambda x: x != 0].rename('flow').rename_axis(("Origin", "Destination")).reset_index().to_dict("records")
    # str1 = df.to_json(orient='records')[1:-1].replace('},{', '} {')

    df_cardNo_New = df['cardNo']
    df_cardNo_New = df_cardNo_New.astype(np.str)
    df_code_New = df['code']
    df_name_New = df['name']

    # 读取数据库中已初始化的人员的考勤号
    df3 = pd.read_excel(r'../test_data/3.xlsx', 'Sheet1')
    df_cardNo_Old = df3['cardNo']
    # print(df_cardNo_Old)
    # 将要对比的两个dataframe格式数据先转为list
    df_cardNo_New = df_cardNo_New.tolist()
    df_cardNo_Old = df_cardNo_Old.tolist()

    # 找出在df_cardNo_New列表中但是不在df_cardNo_Old列表中的元素
    sameKey = [x for x in df_cardNo_New if x in df_cardNo_Old]
    sameKey = pd.Series(data=sameKey)
    df_cardNo_New1 = pd.Series(data=df_cardNo_New)
    # res中需要的关键数据保存在字典中
    dict_old = {'cardNo': df_cardNo_New}
    dict_new = {'name': df_name_New, 'code': df_code_New, 'cardNo': df_cardNo_New1}
    # 将sameKey不同的元素和字典中的cardNo列作对比，如果存在的话就删除，且同时将其他列的此行一并删除（否则会出现行数不一致，报错）

    for i in sameKey:
        if i in dict_old['cardNo']:
            # 找出不同元素的下标，
            index = dict_old['cardNo'].index(i)
            # print(index)
            dict_new['name'].pop(index)
            dict_new['code'].pop(index)

            dict_new['cardNo'].pop(index)
    # print(dict_new)

    # 将删除后的数据重组
    name_res = dict_new['name']
    code_res = dict_new['code']
    cardNo_res = dict_new['cardNo']
    cardNo_res = cardNo_res.astype(np.str)


    dict = {'name': name_res, 'code': code_res, 'cardNo': cardNo_res}
    df_res = pd.DataFrame.from_dict(dict, orient='columns', dtype=None, columns=None)
    # print(df_res)
    df_json = df_res.to_json(orient='records', force_ascii=False)
    # return json.loads(df_json)
    data = '{"deviceServiceCodeList":["WORKIO","ZK001"],' + '"personBOList":' + df_json + '}'
    print(data)

    # url = "https://dktest1-workio.bipocloud.com/services/dukang-cdm/api/person/init"
    # headers = {
    #     'X-DK-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6IjExMSIsImNyZWF0ZWRUaW1lIjoxNjE2NjU5NTg3OTc5LCJ0b2tlblR5cGUiOiJBQ0NFU1NUT0tFTiIsInVzZXJJZCI6IjUzNzIzNjg4MDI1MzUxNzgyNCIsImlhdCI6MTYxNjY1OTU4N30.oJiY3qRX67asrFdh_OaMV4VLFTjiIiCk7uwxQSdjuuE',
    #     'Content-Type': 'application/json'
    # }
    # response = requests.request("POST", url=url, headers=headers, data=data)
    # print(response.text)


if __name__ == '__main__':
    match_staff_name()
