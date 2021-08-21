import logging
from logging.handlers import RotatingFileHandler


errorLogger=logging.getLogger(__name__);

def fetchPreviousRes():
    errorNo()
    return "x"

def errorNo():
    return 0
# Stream 
streamFormatter=logging.Formatter('%(message)s ~ %(filename)s ~ line no: %(lineno)s');
streamHandler=logging.StreamHandler();
streamHandler.setLevel(logging.ERROR);
streamHandler.setFormatter(streamFormatter);
errorLogger.addHandler(streamHandler);

# File
contexSpr='---------------------------------------------------------------------\n'
logDetails=f'{fetchPreviousRes()}{contexSpr}%(levelname)s! %(message)s ~ File: %(filename)s ~ Line no: %(lineno)s \nPath: %(pathname)s\nFunction: %(funcName)s ~ Time & Date: %(asctime)s'
timeAndDate=f'%H:%M:%S %d/%m/%y\n{contexSpr}'
fileFormatter=logging.Formatter(logDetails, datefmt=timeAndDate);
rotatingFileHandler=RotatingFileHandler('logs/errors.log',maxBytes=2000,backupCount=0);
rotatingFileHandler.setLevel(logging.ERROR);
rotatingFileHandler.setFormatter(fileFormatter);
errorLogger.addHandler(rotatingFileHandler);