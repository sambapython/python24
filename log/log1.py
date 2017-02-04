import logging
logging.basicConfig(filename="f1.txt",level=logging.DEBUG,format="%(asctime)s->%(levelname)s->%(message)s")
logging.info("**********This is info message*************")
logging.debug("This id debug message")
logging.warn("this is warn message")
logging.exception("This is exception message")
logging.error("eroor message")