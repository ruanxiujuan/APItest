import logging
import pymysql

from config import DB_CONFIG


class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)   # 初始化数据库连接
        self.cur = self.conn.cursor()

    def query(self, sql):
        logging.debug("查询SQL: {}".format(sql))
        self.cur.execute(sql)
        result = self.cur.fetchall()  # 嵌套元祖 ((1, ..., ...), (2, ..., 22))
        logging.debug("查询结果: {}".format(result))
        return result

    def execute(self, sql):
        logging.debug("执行SQL: {}".format(sql))
        try:
            self.cur.execute(sql)
        except Exception as ex:
            logging.debug(str(ex))  # 输出异常信息
            self.conn.rollback()

    def is_card_exist(self, card_number):   # 封装数据库操作方法
        logging.debug("查询卡: {} 是否存在".format(card_number))
        sql = "select cardNumber from cardinfo where cardNumber='{}'".format(card_number)
        result = self.query(sql)
        if result:   # 空返回() 非空: ((...),)
            logging.debug("该卡存在")
            return True
        else:
            logging.debug("该卡不存在")
            return False

    def del_card_if_exist(self, card_number):
        logging.debug("删除卡: {}".format(card_number))
        sql = "delete from cardinfo where cardNumber='{}'".format(card_number)
        if self.is_card_exist(card_number):
            self.execute(sql)
            logging.debug("删除成功")


if __name__ == '__main__':
    db = DB()
    db.is_card_exist("112233445566")