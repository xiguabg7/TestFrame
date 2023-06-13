# coding:utf-8
# Name:test_cal.py
# Author:nigo
# Time:2021/3/19 5:12 下午 
# Description:
import pytest
import yaml

from tmp.calc import Calc


class YamlData:
    def __init__(self, data_path):
        with open(data_path) as f:
            self.data = yaml.safe_load(f)

    def get_data(self, name):
        return self.data[name]


add_data = YamlData('../test_data/add.yaml')
print(add_data)


# div_data = YamlData('../test_data/div.yaml')


class Test_Cal:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('test_data', add_data.get_data("normal"))
    def calc_add(self, test_data):
        print(test_data)
        res = self.calc.add(test_data['a'], test_data['b'])
        print(res)
        assert res == test_data['c']



if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_cal.py"])
