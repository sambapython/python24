import logging
def fun():
	logging.info("Fucition started")
	logging.warn("function body")
	a=10
	b=20
	logging.debug("RESULT:{0}".format(a+b))
	logging.info("function ended")