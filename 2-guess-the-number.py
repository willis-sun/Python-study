#!/usr/bin/env python
#coding=utf-8

#Create by willis 2016.9.21
#Email willis_sun@163.com

#随机产生要猜的数字(1-100)
#输入,用于接收用户输入的数字
#循环,如果没有猜对则循环接收输入,并打出提示信息
#猜到数字或猜测次数达到一定次数后(6次)打印失败并退出

import random

secret = random.randint(1,100)
guess,tries = 0,0

print "你好，我们来做个游戏，请输入1-99的数字，实一下你的运气如何，只有6次机会哦"

while tries < 6 :
	print "请输入你猜的数字："
	guess_str = raw_input()
	
	g = int(guess_str)

	if g == secret:
		print "可以呀 ，这都被你猜中了，运气不错。"
		break
	elif g < secret:
		print str(g),"Are you a pig?太小了。"
	elif g > secret:
		print str(g),"Are you a pig?太大了。"
	
	tries +=1
else:
	print "都猜了6次了，你行不行。换个姿势再来一次。"
	print "哥来告诉你答案吧：",str(secret)
