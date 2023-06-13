# coding:utf-8
# Name:pandas_excel.py
# Author:nigo
# Time:2021/3/24 7:54 下午 
# Description:
import json
import pandas as pd
import requests


# class Match_Name():
def match_staff_name(self, targetfile, reffile):
    # 读取目标表
    df1 = pd.read_excel(targetfile, 'Sheet1')
    # 读取参考表
    df2 = pd.read_excel(reffile, 'Sheet1')
    # 进行合并，重点看on参数，on参数指的是依据哪一列进行合并，当然也可以添加两列
    # 值得注意的是，此处无论依据哪一列或者哪几列进行合并，均需要尽量确保此列或者
    # 此几列中的值能够是唯一的，否则容易出错
    df = pd.merge(df1, df2, how='left', on=['Name'])
    df.to_excel(r'../test_data/res.xlsx', 'Sheet1', index=None)
    # df.stack()[lambda x: x != 0].rename('flow').rename_axis(("Origin", "Destination")).reset_index().to_dict("records")
    # str1 = df.to_json(orient='records')[1:-1].replace('},{', '} {')
    df_json = df.to_json(orient='records', force_ascii=False)
    # return json.loads(df_json)
    data = '{"deviceServiceCodeList":["WORKIO","ZK001"],' + '"personBOList":' + df_json + '}'
    print(data)

# def send_request1(self, targetfile, reffile):
#     url = 'https://dktest1-workio.bipocloud.com/services/dukang-cdm/api/person/init'
#     dt = match_staff_name(targetfile, reffile)
#     print(dt)
#     r = requests.post(url, data=dt)
#     return r


match_staff_name(r'../test_data/1.xlsx', r'../test_data/2.xlsx')

