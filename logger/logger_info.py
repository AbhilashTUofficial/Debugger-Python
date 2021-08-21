import logging


infoLogger=logging.getLogger(__name__)
fileFormatter=logging.Formatter()
streamFormatter=logging.Formatter('%(asctime)s ~ %(message)s ~ ',datefmt='%m/%d/%Y %H:%M:%S')

streamHandler=logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
streamHandler.setFormatter(streamFormatter)
infoLogger.addHandler(streamHandler)