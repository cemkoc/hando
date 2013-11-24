import pymongo

USERNAME = 'hando'
PASSWORD = 'y311cXwpwIHdX0ukNCSF'

db = pymongo.MongoClient('mongodb://{}:{}@dharma.mongohq.com:10084/hando'
    .format(USERNAME, PASSWORD)).db
