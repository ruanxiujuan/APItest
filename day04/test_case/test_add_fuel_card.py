import json

from test_case.basecase import BaseCase


class TestAddFuelCard(BaseCase):
    def test_add_fuel_card(self):
        self.get_case_data("添加加油卡", "接口、参数正确")
        card_number = json.loads(self.case_data["入参"])["CardInfo"]["cardNumber"]
        self.db.del_card_if_exist(card_number)  # 环境准备
        self.run_case()  # 执行测试
        self.assertTrue(self.db.is_card_exist(card_number))  #数据库断言
        self.db.del_card_if_exist(card_number)  # 环境清理

    def test_add_exist_fuel_card(self):
        self.get_case_data("添加加油卡", "参数相同，重复添加")
        self.run_case()

    def test_add_two_fuel_card(self):
        self.get_case_data("添加加油卡", "同一账号添加第2个加油卡")
        card_number = json.loads(self.case_data["入参"])["CardInfo"]["cardNumber"]
        self.db.del_card_if_exist(card_number)  # 环境准备
        self.run_case()
        card_number = json.loads(self.case_data["入参"])["CardInfo"]["cardNumber"]
        self.db.del_card_if_exist(card_number)  # 环境准备