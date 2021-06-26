from config.lib import *

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["game_match"]
col_transaction_game = mydb["transaction_game"]
