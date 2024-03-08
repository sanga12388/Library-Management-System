import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)

def warning(message):
    logging.warning(message)