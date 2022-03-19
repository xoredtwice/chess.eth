from datetime import datetime
import logging
import os


def setup_logger(path, name):

    time_tag = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_level = logging.DEBUG

    log_path = os.path.join(path, name + "-" + time_tag + '.log')

    logger = logging.getLogger("LOGGER")
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_path, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.setLevel(log_level)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    logger.info("Logger started...")

def lprint(text):
    logger = logging.getLogger("LOGGER")
    logger.info(text)

def lsection(text, level = 0):
    indent = "    " * level
    if level == 0 :
        lprint("***********************************")
    else:
        lprint("")
        lprint("")
    lprint(f"{indent}{text}")
    if level == 0:
        lprint("***********************************")
#*******************************************************************************