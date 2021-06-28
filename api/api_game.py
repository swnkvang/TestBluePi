
from config.lib import *
from method.rungame import *
from method.player_account import *

class Item_RunGame(BaseModel):
    id_game: str
    RowsClick: int
    ColsClick: int

@app.post("/game/start")
def newgame(request: Request, response: Response):
    try :
        token = request.headers['authorization']
        token = token.split(' ')[1]
        result_authen = authen_account(token)
        if result_authen[0] == True :
            username = result_authen[1]
            result_createGame = new_game(username)
            if result_createGame[0] == True :
                return {"result": "OK", "data": result_createGame[1], "messageER": None}
            else :
                return {"result": "ER", "data": None, "messageER": result_createGame[1]}
        else :
            response.status_code = 401
            return {"result": "ER", "data": None, "messageER": result_authen[1]}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        response.status_code = 401
        return {"result": "ER", "data": None, "messageER": 'Unauthorized'}

@app.post("/game/run")
def rungame(request: Request, body: Item_RunGame, response: Response):
    try :
        token = request.headers['authorization']
        token = token.split(' ')[1]
        result_authen = authen_account(token)
        if result_authen[0] == True :
            username = result_authen[1]
            id_game = body.id_game
            RowsClick = body.RowsClick
            ColsClick = body.ColsClick
            if (id_game == '' or id_game == None) :
                return {"result": "ER", "data": None, "messageER": 'please enter id_game'}
            result_playGame= play_game(username,id_game,RowsClick,ColsClick)
            if result_playGame[0] == True :
                return {"result": "OK", "data": result_playGame[1], "messageER": None}
            else :
                return {"result": "ER", "data": None, "messageER": result_playGame[1]}
        else :
            response.status_code = 401
            return {"result": "ER", "data": None, "messageER": result_authen[1]}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return {"result": "ER", "data": None, "messageER": str(e)}