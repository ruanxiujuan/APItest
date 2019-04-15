import requests


def todo_list():
    url = "http://115.28.108.130:5000/todos"
    res = requests.get(url=url)
    print(res.text)


def create_task():
    url = "http://115.28.108.130:5000/todos"
    data = {"task": "记得买菜"}
    res = requests.post(url=url, json=data)
    print(res.json()["task"])


if __name__ == "__main__":
    # todo_list()
    create_task()