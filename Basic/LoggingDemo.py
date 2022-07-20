import logging

#zwykle slashe linijke nizej
logging.basicConfig(filename = "C://Users//Young Stachu//Desktop//Python//miejsce na syf//test.log",
                    format= '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level= logging.DEBUG
                    )

logging.debug("This is debug message")
logging.info("This is info message")

logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")




