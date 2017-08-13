import logging

LOG_FORMAT = '%(asctime)s %(levelname)-6s %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt='%d-%m-%y %H:%M:%S')

logger = logging.getLogger()