from config.lib import *
from method.player_account import *

class Item_DataPlayer(BaseModel):
    username: str
    password: str
   

@app.post("/game/createplayer")
def createplayer(body: Item_DataPlayer):
    username = body.username
    password = body.password
    result = create_account(username,password)
    if result[0] == True:
        return {"result": "OK", "data": result[1], "messageER": None}
    else :
        return {"result": "ER", "data": None, "messageER": result[1]}

@app.post("/game/login")
def playerlogin(body: Item_DataPlayer, response: Response):
    try :
        username = body.username
        password = body.password
        result = login(username,password)
        if result[0] == True:
            return {"result": "OK", "data": result[1], "messageER": None}
        else :
            response.status_code = 401
            return {"result": "ER", "data": None, "messageER": result[1]}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return {"result": "ER", "data": None, "messageER": str(e)}
