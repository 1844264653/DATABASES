#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 21:17
# @Author  : sakura
# @Site    : 
# @File    : models.py
# @Software: PyCharm

"""对数据库的一些操作"""

import pymysql


class MySQLClient(object):
    CACHE_CLIENT = {}

    def __init__(self, host, database=None, mysql_port=3306, password="123456", refresh=True):
        """
        initialize client to use 'self.conn' and 'self.cursor' for operating mysql
        :param host: ip of the host
        :param mysql_port: port of the mysql, default is 3306
        :param ssh_port: port of the ssh, default is 22
        :param ssh_user: user of the ssh, default is "root"
        :param ssh_password: password of the ssh, default is "admin"
        """
        self.host = host
        if self.host in self.CACHE_CLIENT and database in self.CACHE_CLIENT[self.host] \
                and not refresh:
            self.conn = self.CACHE_CLIENT[host][database]["conn"]
            self.cursor = self.CACHE_CLIENT[host][database]["cursor"]
            # self.conn.ping()

        else:

            config = {
                "host": host,
                "port": mysql_port,
                "password": password,
                "user": "root",
                "database": database,
                "charset": "utf8"
            }
            self.conn = pymysql.connect(**config)
            self.conn.autocommit(1)
            self.cursor = self.conn.cursor()
            temp = {
                database: {
                    "conn": self.conn,
                    "cursor": self.cursor,
                }
            }
            if self.host in self.CACHE_CLIENT:
                self.CACHE_CLIENT[self.host].update(temp)
            else:
                self.CACHE_CLIENT[self.host] = temp


if __name__ == '__main__':
    client = MySQLClient(host="localhost", database="test")
    # create_sql = """CREATE TABLE t (
    # id int(11) NOT NULL primary key auto_increment,
    # a int(11) default null ,
    # b int(11) default null ,
    # key a (a),
    # key b (b)
    # )ENGINE=InnoDB"""
    # client.cursor.execute(create_sql)
    # client.conn.commit()
    # client.conn.close()
    #

    insert_sql = "insert into t(a,b) values (%s, %s)"
    for i in range(100000):
        client.cursor.execute(insert_sql, args=[i,i])
    client.conn.commit()
    client.cursor.close()
    client.conn.close()
