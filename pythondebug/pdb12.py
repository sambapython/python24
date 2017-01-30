print "program started"
a=10
b=20
print a+b
def fun(a,b):
	print "a={0}, b={1}".format(a,b)
	print a+b
	print a-b
	print a*b
	return a/b
for i in [1,2,3,4,5,6]:
	print 10/i 

print "other statements in program "
fun(a,b)
print "program ended"