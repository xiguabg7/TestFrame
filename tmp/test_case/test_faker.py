# coding:utf-8
# Name:test_faker.py
# Author:nigo
# Time:2022/1/6 3:03 下午 
# Description:
import pymysql

from faker import Faker


class InsertData():
    def __init__(self, host, port, user, password, database):
        '''连接初始化'''
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                        database=self.database)
            self.cursor = self.conn.cursor()
            print("连接数据库成功...")
        except Exception as e:
            raise e

    def get_data(self, number):
        '''获取测试数据'''
        faker = Faker("zh_CN")  # 中文数据
        self.number = number
        person_data = []
        for i in range(self.number):
            person_info = (faker.name(), faker.address(), faker.date())
            person_data.append(person_info)
        # print(person_data)
        return person_data

    def execute(self, sql, data):
        '''执行sql,重复执行参数列表的参数'''
        self.cursor.executemany(sql, data)
        self.conn.commit()
        print("插入{}条数据完成...".format(self.number))

    def __del__(self):
        '''关闭连接资源'''
        self.cursor.close()
        self.conn.close()
        print('关闭数据库连接...')


if __name__ == '__main__':
    db = InsertData('rm-uf6p31b6r5763b09wko.mysql.rds.aliyuncs.com', 3306, 'iac_dev', 'B1p02017', 'school')
    sql = "INSERT INTO person(name,address,birthdate)VALUES (%s,%s,%s)"
    db.execute(sql, db.get_data(100))
