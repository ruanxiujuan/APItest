"""数据库封装方法"""
import pymysql
from config import DB_API_TEST


def get_conn(db_conf=DB_API_TEST):
    conn = pymysql.connect(**db_conf)
    return conn


def query_db(conn,sql):
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def change_db(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as ex:
        conn.rollback()


if __name__ == "__main__":
    conn = get_conn()
    sql_query = "select * from user;"
    sql_insert = "INSERT INTO USER VALUES('20006','xuyq','123456');"
    query_db(conn, sql_query)
    change_db(conn, sql_insert)
    conn.close
