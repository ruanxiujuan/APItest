import pymysql
from config import DB_API_TEST


def get_conn():
    conn = pymysql.connect(**DB_API_TEST)
    return conn


# 查询
def query_db(conn, sql):
    # 2. 建立游标
    cur = conn.cursor()
    # 3. 执行sql
    cur.execute(sql)
    # 4. 获取数据
    result = cur.fetchall()
    # result2 = cur.fetchmany(3)
    # result = cur.fetchone()
    # print(result[1])
    return result


def change_db(conn, sql):
    # 2. 建立游标
    cur = conn.cursor()
    # 3. 执行sql
    cur.execute(sql)

    # 4. 提交更改
    conn.commit()



if __name__ == "__main__":
    conn = get_conn()
    print(query_db(conn, "select * from user"))
    change_db(conn, 'insert into user VALUES(40013,"李靖","e10adc3949ba59abbe56e057f20f883e");')
    conn.close()