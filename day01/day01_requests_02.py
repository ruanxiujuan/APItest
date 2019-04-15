import json

import requests



def get_01():
    url = "http://115.28.108.130:5000/add/?a=13&b=5"
    res = requests.get(url=url)
    print(res.text)


def get_02():
    url = "http://115.28.108.130:5000/add/"
    params = {"a": 13, "b": 5}
    res = requests.get(url=url, params=params)
    print(res.text)


def post_form():
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": "张三", "password": "123456"}
    res = requests.post(url=url, data=data)
    print(res.text)


def post_json_01():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三", "password": "123456"}
    res = requests.post(url=url, json=data)  # json=....
    print(res.json().get("msg"))  # 响应的字典格式, 响应不是json会报错


def post_json_02():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = '''{
        "name":"张三",
        "password": "123456"
    }
    '''
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url, data=data.encode('utf-8'), headers=headers)  # json=....
    print(res.json().get("msg"))  # 响应的字典格式, 响应不是json会报错


def post_json_03():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三", "password": "123456"}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url, data=json.dumps(data),headers=headers)  # json=....
    res_dict = res.json()   # 字典格式
    print(json.dumps(res_dict, indent=2, ensure_ascii=False, sort_keys=True))


def post_xml():
    url = "http://httpbin.org/post"
    data = '''<xml><name>Lily</name></xml>'''
    headers = {"Content-Type": "application/xml"}
    res = requests.post(url=url, data=data, headers=headers)
    print(res.text)


def post_file():
    url = "http://115.28.108.130:5000/api/user/uploadImage/"
    files = {"file": open("1.txt", "rb")}   # 二进制格式打开
    res = requests.post(url=url, files=files)
    print(res.text)


def get_basic_auth():
    url = "http://115.28.108.130:5000/api/user/login2/"
    res = requests.get(url=url, auth=("admin", "secret"))
    print(res.text)


def get_user_list_1():
    url1 = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": "张三", "password": "123456"}
    res1 = requests.post(url=url1, data=data)

    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res2 = requests.get(url=url2, cookies=res1.cookies)
    print(res2.text)


def get_user_list_2():
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    # 1. cookies 拆分成字典格式
    # cookies = {"JSESSIONID": "ED53A56D99DB0EF7A7894964DBAFB83A",
    #            "PYSESSID": "84fd4272-37d8-11e9-99c1-00163e06e52c",
    #            "session": ".eJxtzLkNgDAMAMBdUmPJT-LEbJPHDICgQuyOEJTpT3cFbaZUqYNwyUDkBoVjA0RScVRP3MN67KcvocRtRM4Mkkf5rFmnqW3CSbPU96X_RRsTez-yryHl.D1ONLQ.SXCk1Fr86kYYpjx3DoFDN5AIIIQ"}
    # res2 = requests.get(url=url2, cookies=cookies)

    # 2. cookie作为headers的一项 没有s, 不用拆分
    headers = {"Cookie": "JSESSIONID=ED53A56D99DB0EF7A7894964DBAFB83A; PYSESSID=84fd4272-37d8-11e9-99c1-00163e06e52c; session=.eJxtzLkNgDAMAMBdUmPJT-LEbJPHDICgQuyOEJTpT3cFbaZUqYNwyUDkBoVjA0RScVRP3MN67KcvocRtRM4Mkkf5rFmnqW3CSbPU96X_RRsTez-yryHl.D1ONLQ.SXCk1Fr86kYYpjx3DoFDN5AIIIQ"}
    res2 = requests.get(url=url2, headers=headers)
    print(res2.text)


def get_user_list_3():
    session = requests.session()  # 新建一个会话
    url1 = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": "张三", "password": "123456"}
    session.post(url=url1, data=data)

    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res2 = session.get(url=url2)
    print(res2.text)


def login(username, password):
    session = requests.session()  # 新建一个会话
    url1 = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": username, "password": password}
    session.post(url=url1, data=data)
    return session


def get_user_list_3():
    s = login("张三", "123456")
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res2 = s.get(url=url2)
    print(res2.text)


def get_token():
    url = "http://115.28.108.130:5000/api/user/getToken/?appid=136425"
    res = requests.get(url=url)
    print(res.text)
    token = res.text.split("=")[1]
    return token


def update_user():
    token = get_token()
    url = "http://115.28.108.130:5000/api/user/updateUser/?token={}".format(token)
    print(url)
    res = requests.post(url=url, json={"name": "李六", "password": "123456"})
    print(res.json())


def batch_reg():
    users = ["爱新觉罗01", "爱新觉罗02", "爱新觉罗03", "爱新觉罗04"]
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三", "password": "123456"}
    for user in users:
        data["name"] = user
        res = requests.post(url=url, json=data)  # json=....
        print(res.json())  # 响应的字典格式, 响应不是json会报错


if __name__ == "__main__":   # 只有本模块自己运行时才会执行的代码,通常用来调试
    # get_01()
    # get_02()
    # post_form()
    # post_json_01()
    # post_json_02()
    # post_json_03()
    # post_xml()
    # post_file()
    # get_basic_auth()
    # get_user_list_1()
    # get_user_list_2()
    # get_user_list_3()
    # update_user()
    batch_reg()




