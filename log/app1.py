import logging
logging.basicConfig(filename="f2.txt",
	level=logging.DEBUG,
	format="%(asctime)s->%(levelname)s->%(message)s")
import mod1
mod1.fun()
logging.info("###### program started###")
a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
if not a.isdigit():
	logging.warn("Expecting digit given {0}".format(a))
if not b.isdigit():
	logging.warn("Expecting digit given {0}".format(b))
try:
	a=int(a)
	b=int(b)

	res=a/b
	logging.debug("{0}".format(res))
except Exception as err:
	logging.exception(err)
logging.info("Program ended")