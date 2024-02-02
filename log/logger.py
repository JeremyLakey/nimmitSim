
logger = None


def open_log(file):
    global logger
    logger = open(file, 'w')


def close_log():
    global logger
    if logger is not None:
        logger.close()


def log(message):
    global logger
    if logger is not None:
        logger.write(message + '\n')

