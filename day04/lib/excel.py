import os
import logging
import xlrd
from config import DATA_DIR


class Excel(object):
    def __init__(self, file_name):  # 只用传文件名
        data_file = os.path.join(DATA_DIR, file_name)  # 拼接上数据目录的路径
        logging.debug("打开Excel: {}".format(data_file))
        self.wb = xlrd.open_workbook(data_file)

    def get_data(self, sheet_name):
        logging.debug("获取工作表: '{}' 数据".format(sheet_name))
        sh = self.wb.sheet_by_name(sheet_name)
        title = sh.row_values(0)  # 标题行
        rows = sh.nrows
        data = {}   # 新建一个字典用来存放所有用例的数据
        for i in range(1, rows):
            row_data = sh.row_values(i)  # 当前行 []
            case_data = dict(zip(title, row_data))  # 一条用例的数据:当前行和标题组合为字典
            case_name = case_data["用例名称"]
            data[case_name] = case_data  # 把用例数据添加到data中,key为用例名
        logging.debug("工作表数据: {}".format(data))
        return data


if __name__ == '__main__':
    e = Excel("加油卡完整用例.xls")
    e.get_data("添加加油卡")
