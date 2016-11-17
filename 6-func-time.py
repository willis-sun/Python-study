#!/usr/bin/env python
#coding=utf-8

#使用装饰器计算函数的执行时间

import time
import datetime
import functools

def timeIt(func):
    @functools.wraps(func) #增加这一行，将原函数作为值传递进去，表示将原函数的__name__,__doc__等信息更新到装饰器里
    def warp(arg):
        start = datetime.datetime.now()
	func(arg)
	end = datetime.datetime.now()
	cost = end - start
	print "execute %s spend %s" %(func.__name__,cost.total_seconds())
    return warp

@timeIt    #这是python提供的语法糖
def func(arg):
    time.sleep(arg)

func(5)
print func.__name__
