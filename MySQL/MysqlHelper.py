# coding=utf-8
import pymysql


class MysqlHelper:
    def __init__(self, host='localhost', port=3306, db='test2', user='root', passwd='mysql',
                 charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd,
                                    charset=charset)

    def insert(self, sql, params):
        return self.__cud(sql, params)

    def update(self, sql, params):
        return self.__cud(sql, params)

    def delete(self, sql, params):
        return self.__cud(sql, params)

    def __cud(self, sql, params=[]):
        try:
            cs1 = self.conn.cursor()
            rows = cs1.execute(sql, params)
            self.conn.commit()
            cs1.close()
            self.conn.close()
            return rows
        except Exception as e:
            print(e)
        if self.conn is not None:
            self.conn.rollback()

    def fetchone(self, sql, params=[]):
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            row = cs1.fetchone()
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print(e)
            if self.conn is not None:
                self.conn.rollback()

    def fetchall(self, sql, params):
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            rows = cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print(e)
        if self.conn is not None:
            self.conn.rollback()