import logging

#zwykle slashe linijke nizej
logging.basicConfig(filename = "C://Users//Young Stachu//Desktop//Python//miejsce na syf//test.log",
                    format= '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p'
                    )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")

logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")




