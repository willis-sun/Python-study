#!/var/bin/env python
#coding=utf-8
#本脚本功能为读取系统负载信息
# 通过读取/proc/loadavg文件监控系统的平均负荷
# “watch python 读取负载信息.py” 命令可实时监控系统平均负荷

def load_avg():
	loadavg = {}
	with open('/proc/loadavg') as f:
		avg = f.read().split()   #将本行内容以空格分隔为列表
		loadavg['avg_1'] = avg[0]
		loadavg['avg_2'] = avg[1]
		loadavg['avg_3'] = avg[2]
	return loadavg

if __name__ == '__main__':
	for k,v in load_avg().items():
		print k,v
