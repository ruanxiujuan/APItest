"""用例辅助方法"""
import requests
from db import query_db, change_db


def get_user_data(conn, name):
    result = query_db(conn, "select * from user where name='{}'".format(name))
    return result

# delete from user where name="{}".format(name)
def del_user(conn, name):
    change_db(conn, 'delete from user where name="{}"'.format(name))


def login(name, password):
    s = requests.session()
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": name, "password": password}
    s.post(url=url, data=data)
    return s

if __name__ == "__main__":
    from db import get_conn
    conn = get_conn()
    print(get_user_data(conn, "张三"))
    conn.close()

