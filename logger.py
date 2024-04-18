# logs are ways u knw and track ur application, its more like a record, knw ur wen ur start ur server and end ur server

import logging
import sys

# create a logger instance
logger = logging.getLogger()

# create formater, its how ur logs sud appear
# so we want the time, levelname and message
formatter = logging.Formatter(
    fmt='%(asctime)s - %(levename)s - %(message)s'
)

#handler -- diff types of handlers, but we use sys.s stdout is our console
# stream wil log to console
# file wil log to app.log
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')


# set handlers
# stream formater
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# log handlers
# add handlers to logger
logger.handlers = [stream_handler, file_handler]

# set the logger, dere are diff level, we use info.
logger.setLevel(logging.INFO)
