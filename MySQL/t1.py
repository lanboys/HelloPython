# coding=utf-8
import pymysql

conn = None

try:
    conn = pymysql.connect(host='localhost', port=3306, db='python', user='root', passwd='admin',
                           charset='utf8')
    cs1 = conn.cursor()

    # uname = input("请输入用户名：")
    # ubirthday = input("请输入生日：")
    # ugender = input("请输入性别：")
    # params = [uname, ubirthday, int(ugender), 1]
    params = ["111", "323", int("2"), 1]

    sql = "update stu set name=%s,birthday=%s,gender=%s where id=%s"
    cs1.execute(sql, params)

    # insert

    # delete
    conn.commit()
    cs1.close()
    conn.close()
    print("ok")
except Exception as e:
    print(e)
    if conn is not None:
        conn.rollback()
