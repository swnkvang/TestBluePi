import re
from config.lib import *
from config.db_mongo import *

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
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]

def cal_GlobalBestScore():
    try :
        GlobalBestScore = None
        result_query = col_transaction_game.find({
            "status_game": 'Win'
        },{"count_click": 1,"_id": 0}).sort("count_click", 1).limit(1)
        data = list(result_query)
        if len(list(data)) != 0 :
            GlobalBestScore = data[0]['count_click']
        return [True,GlobalBestScore]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]

def cal_BestScorePlayer(account_id):
    try :
        BestScorePlayer = None
        result_query = col_transaction_game.find({
            "account_id": account_id,
            "status_game": 'Win'
        },{"count_click": 1,"_id":0}).sort("count_click", 1).limit(1)
        data = list(result_query)
        if len(list(data)) != 0 :
            BestScorePlayer = data[0]['count_click']
        return [True,BestScorePlayer]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]
    
def cal_StatusGame(box):
    try :
        for i in range(len(box)):
            for j in range(len(box[i])):
                if box[i][j]['status_open'] == False:
                    return [True, 'Pending']
        return [True, 'Win']
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]

def calBoxGame(box,RowsOpenLatest,ColsOpenLatest,RowsClick,ColsClick):
    try :
        if RowsOpenLatest != None and ColsOpenLatest != None: 
            valueLatest = box[RowsOpenLatest][ColsOpenLatest]['value']
            valueNow = box[RowsClick][ColsClick]['value']
            if (valueLatest == valueNow):
                box[RowsOpenLatest][ColsOpenLatest]['status_open'] = True
                box[RowsClick][ColsClick]['status_open'] = True
                RowsOpenLatest = None
                ColsOpenLatest = None
            else :
                box[RowsOpenLatest][ColsOpenLatest]['status_open'] = False
                box[RowsClick][ColsClick]['status_open'] = False
                RowsOpenLatest = None
                ColsOpenLatest = None
        else :
            box[RowsClick][ColsClick]['status_open'] = True
            RowsOpenLatest = RowsClick
            ColsOpenLatest = ColsClick
        data_return = {
            "box": box,
            "RowsOpenLatest": RowsOpenLatest,
            "ColsOpenLatest": ColsOpenLatest
        }
        return [True,data_return]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]
