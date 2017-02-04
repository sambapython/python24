from time import sleep
from threading import Thread
def fun1():
	for i in range(10):
		sleep(1)
		print i
		print "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
def fun2():
	for i in range(100,110):
		sleep(1)
		print i
		print "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ"
'''
fun1()
fun2()
'''
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()
while True:
	if not t1.isAlive():
		break
while True:
	if not t2.isAlive():
		break

print "main is closed"
