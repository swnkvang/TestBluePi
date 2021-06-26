from config.db_mongo import *

def findOne_transaction_game(id_game):
    print()

def update_transaction_game():
    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }
    col_transaction_game.update_one(myquery, newvalues)    
