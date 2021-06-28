from config.lib import *
from config.db_mongo import *
from function.cal_Game import *

def new_game(username):
    try :
        best_score = None
        globalBest_Score = None
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
                "username": username, 
                "box": box_game,
                "count_click": count_click,
                "RowsOpenLatest": None,
                "ColsOpenLatest": None,
                "status_game": StatusGame,
                "time_create" : datetime.utcnow(),
                "time_update": datetime.utcnow()
            }
        resultNewGame = col_transaction_game.insert_one(mydict)
        result_calGlobalBestScore= cal_GlobalBestScore()
        if result_calGlobalBestScore[0] == True:
            globalBest_Score = result_calGlobalBestScore[1]
        result_calScorePlayer = cal_BestScorePlayer(username)
        if result_calScorePlayer[0] == True:
            best_score = result_calScorePlayer[1]
        data_return = {
            "id_game": str(resultNewGame.inserted_id),
            "count_click": count_click,
            "best_score": best_score,
            "globalBest_Score": globalBest_Score
        }
        return[True, data_return]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]

def play_game(username,id_game,RowsClick,ColsClick):
    try:
        best_score = None
        globalBest_Score = None
        result_game = col_transaction_game.find_one({
            "_id": ObjectId(id_game),
            "username": username
        })
        if (result_game == None) :
            return [False, 'This token is not your game']
        boxOpenNow = (result_game['box'][RowsClick][ColsClick]['value'])
        box = result_game['box']
        count_click = result_game['count_click']
        RowsOpenLatest = result_game['RowsOpenLatest']
        ColsOpenLatest = result_game['ColsOpenLatest']
        StatusGame = result_game['status_game']
        if (StatusGame == 'Win') :
            return [False,'End Game !']
        if box[RowsClick][ColsClick]['status_open'] != True:
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
                        "status_game": StatusGame,
                        "time_update": datetime.utcnow()
                        } }
            col_transaction_game.update_one(myquery, newvalue) 

            result_calScorePlayer = cal_BestScorePlayer(username)
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
            "box": box,
            "count_click": count_click,
            "best_score": best_score,
            "globalBest_Score": globalBest_Score,
            "StatusGame": StatusGame,
            "boxOpenNow": boxOpenNow
        }
        return [True,data_return]
    except IndexError as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,'Rows or Cols is Incorrect']
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]