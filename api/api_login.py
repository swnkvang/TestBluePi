from config.lib import *
from method.player_account import *

@app.post("/game/login")
def login():
    result = create_account()
    if result[0] == True:
        data = {
            "token" : result[1]
        }
        return {"result": "OK", "data": data, "messageER": None}
    else :
        return {"result": "ER", "data": None, "messageER": result[1]}
