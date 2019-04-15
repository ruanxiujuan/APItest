import unittest
from common import login


class TestGetUserList(unittest.TestCase):
    def test_get_user_list(self):
        s = login("张三", "123456")
        url = "http://115.28.108.130:5000/api/user/getUserList/"
        res = s.get(url)
        self.assertIn("张三", res.text)



if __name__ == '__main__':
    unittest.main()
