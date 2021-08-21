import logging

debugLogger=logging.getLogger(__name__)
# fileFormatter=logging.Formatter('%(asctime)s  %(message)s  ',datefmt='%m/%d/%Y %H:%M:%S')

# fileHandler=logging.FileHandler('logs/debug.log',mode='w')
# fileHandler.setLevel(logging.ERROR)
# fileHandler.setFormatter(fileFormatter)
# debugLogger.addHandler(fileHandler)

debugLogger=logging.basicConfig(
    filename= 'logs/debug.log', 
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - %(message)s - line : %(lineno)s',
    datefmt='%m/%d/%Y %H:%M:%S');