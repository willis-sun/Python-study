#!/usr/bin/python
# coding=utf-8
#此脚本为连接mysql数据库脚本

import MySQLdb
conn=MySQLdb.connect(user='root',passwd='willis',host='127.0.0.1',db='test',charset='utf8')
cur=conn.cursor()
#cur.execute("delete from user")
cur.execute("insert into user value ('小明',10)")
result=cur.fetchmany(cur.execute("select * from user"))
for i in result:
    print i[0],i[1]
cur.close()
conn.close()
