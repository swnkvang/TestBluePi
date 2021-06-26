from re import T

from pydantic.errors import NumberNotMultipleError
from config.lib import *
from config.db_mongo import *
from function.cal_Game import *

def cal_num(list_number):
    value_return = list_number[0]
    list_number.pop(0)
    return value_return,list_number

def createGame():
    try :
        list_number_A = [1,2,3,4,5,6,1,2,3,4,5,6]
        rows, cols = (3, 4)
        random.shuffle(list_number_A)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                result = cal_num(list_number_A)
                arr[i][j] = result[0]
                list_number_A = result[1]
        return [True,arr]
    except Exception as e:
        print(str(e))
        return [False,str(e)]

def new_game(account_id):
    try :
        result_game = createGame()
        if result_game[0] == False :
            return [False,result_game[1]]
        box_game = result_game[1]
        count_click = 0
        StatusGame = 'Pending'
        for i in range(len(box_game)):
            for j in range(len(box_game[i])):
                val = box_game[i][j]
                status_open = False
                box_game[i][j] = {
                    "value" : val,
                    "status_open": status_open
                }
        mydict = {
                "account_id": account_id, 
                "box": box_game,
                "count_click": count_click,
                "RowsOpenLatest": None,
                "ColsOpenLatest": None,
                "status_game": StatusGame
            }
        resultNewGame = col_transaction_game.insert_one(mydict)
        data_return = {
            "id_game": str(resultNewGame.inserted_id)
        }
        return[True, data_return]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]

def play_game(account_id,id_game,RowsClick,ColsClick):
    try:
       best_score = None
       globalBest_Score = None
       result_game = col_transaction_game.find_one({"_id": ObjectId(id_game)})
       box = result_game['box']
       count_click = result_game['count_click']
       RowsOpenLatest = result_game['RowsOpenLatest']
       ColsOpenLatest = result_game['ColsOpenLatest']
       StatusGame = result_game['status_game']
       if (StatusGame == 'Win') :
           return [False,'End Game !']
       count_click += 1 
       result_calBoxGame = calBoxGame(box,RowsOpenLatest,ColsOpenLatest,RowsClick,ColsClick)
       if result_calBoxGame[0] == True :
           box = result_calBoxGame[1]['box']
           RowsOpenLatest = result_calBoxGame[1]['RowsOpenLatest']
           ColsOpenLatest = result_calBoxGame[1]['ColsOpenLatest']
       else :
            return [False,result_calBoxGame[1]]
       result_calStatusGame = cal_StatusGame(box)
       if result_calStatusGame[0] == True:
           StatusGame = result_calStatusGame[1]
       else :
            return [False,result_calStatusGame[1]]
       myquery = {"_id": ObjectId(id_game)}
       newvalue = { "$set": { 
                "RowsOpenLatest": RowsOpenLatest ,
                "ColsOpenLatest": ColsOpenLatest ,
                "box": box,
                "count_click": count_click,
                "status_game": StatusGame
                } }
       col_transaction_game.update_one(myquery, newvalue) 
       result_calScorePlayer = cal_BestScorePlayer(account_id)
       if result_calScorePlayer[0] == True:
           best_score = result_calScorePlayer[1]
       result_calGlobalBestScore = cal_GlobalBestScore()
       if result_calGlobalBestScore[0] == True:
           globalBest_Score = result_calGlobalBestScore[1]
       boxClose = box
       for i in range(len(boxClose)):
            for j in range(len(boxClose[i])):
                if boxClose[i][j]['status_open'] == False:
                    boxClose[i][j]['value'] = None
       data_return = {
           "id_game": id_game,
           "box": boxClose,
           "count_click": count_click,
           "best_score": best_score,
           "globalBest_Score": globalBest_Score,
           "StatusGame": StatusGame
       }
       return [True,data_return]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]