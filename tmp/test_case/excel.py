# coding:utf-8
# Name:excel.py.py
# Author:nigo
# Time:2021/3/26 11:39 上午 
# Description:
import xlrd, re

class ReadExcel:

    def __init__(self, fileName, sheetName):
        """
        new_data是最后返回的值
        :param fileName: excel文件名
        :param sheetName: sheet名称
        """
        self.fileName = fileName
        self.sheetName = sheetName
        # 读取excel
        self.book = xlrd.open_workbook(self.fileName)
        self.sheet0 = self.book.sheet_by_name(self.sheetName)
        # 获取第一列数据
        self.col_value = self.sheet0.col_values(0)  # 第一列
        self.new_data = {}

    def data_type(self, test_type, test_value):
        """
        判断从excel单元格中获取的数据类型
        1 string（text）, 2 number, 3 date, 4 boolean
        :param test_type: 类型
        :param test_value: 值
        :return:
        """
        if test_type == 1:
            """字符串"""
            return test_value

        elif test_type == 2:
            if '.0' in str(test_value):
                """整数"""
                return int(test_value)
            else:
                """浮点"""
                return test_value

        elif test_type == 3:
            """日期"""
            date = xlrd.xldate_as_datetime(test_value, 0).strftime('%Y-%m-%d')
            return date

        elif test_type == 4:
            """布尔类型"""
            if test_value == 1:
                return True
            elif test_value == 0:
                return False

    def write_list(self, value):
        """
        取出某一行的值，将其写入一个新的字典
        :param value:   self.col_value.index 是一个列表（第一列的值），self.col_value.index(value)是判断value这个值是在列表中的第几位
        :return: 新建的字典
        """
        test_data = {}
        for j in range(1, self.sheet0.ncols):
            test_type = self.sheet0.cell_type(self.col_value.index(value), j)  # 单元格数据类型
            test_value = self.sheet0.cell_value(self.col_value.index(value), j)  # 单元格数据值
            result = self.data_type(test_type, test_value)
            test_data[self.sheet0.row_values(0)[j]] = result
        return test_data

    def read_excel(self):
        """
        读取excel表中数据
        :return: 字典格式
        """
        # 遍历将相同类型的用例分在一起
        for i in self.col_value[1:]:
            m = re.findall("_\d+_", i)  # 按照固定格式匹配，用于判断用例是否是相同的类型
            if len(m) == 0:
                test_data = self.write_list(i)
                self.new_data[i] = test_data
            else:
                n = re.findall("(.+_\d+?)_\d+", i)[-1]  # 按照固定格式匹配，提取相同的字符
                if n not in self.new_data.keys():
                    test_data = self.write_list(i)
                    self.new_data[n] = [test_data]
                else:
                    test_data = self.write_list(i)
                    self.new_data[n].append(test_data)
        return self.new_data


if __name__ == '__main__':
    x = ReadExcel(r"F:\workspace\selenium_demo\data\data.xlsx", "添加用户").read_excel()
    print(x)


# def match(file, sheetnames, reffile, refsheet, targetsegs, matchseg):  # 文件名 sheet列表 参考文件名 参考sheet 目标字段列表 参考字段
#     alldata = pd.read_excel(file, None)
#     refdata = pd.read_excel(reffile, refsheet)
#     # 获取映射字典
#     maps = {}
#     for i in refdata.index:
#         MatchSeg = refdata.loc[i, matchseg]
#         maps[MatchSeg] = {}
#         for seg in targetsegs:
#             maps[MatchSeg][seg] = refdata.loc[i, seg]
#     # 匹配数据
#     for sheet in sheetnames:
#         if (isinstance(sheet, int)):
#             sheet = list(alldata.keys())[sheet]
#
#         data = alldata[sheet].fillna('-')
#         for i in data.index:
#             MatchSeg = data.loc[i, matchseg]
#             for seg in targetsegs:
#                 try:
#                     data.loc[i, seg] = map[MatchSeg][seg]
#                 except Exception as e:
#                     pass
#
#         alldata[sheet] = data
#     # 导出
#     with pd.ExcelWriter(file) as writer:
#         for sheet in alldata.keys():
#             alldata[sheet].to_excel(writer, sheet, index=False)
#
# match('要匹配的表.xlsx', [0, 1], '参考表.xlsx', '参考页', ['要匹配的字段1,字段2'], '参考字段')
