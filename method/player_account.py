from config.lib import *
from config.db_maria import *
from function.cal_authen import *

def create_account(username,password):
    try : 
        sql_select = "SELECT * FROM tb_player_account WHERE username = ?"
        value = [username]
        resultSelect = selectSQL(sql_select,value)
        if (resultSelect[0] != True):
            return [False,resultSelect[1]]
        if len(resultSelect[1]) != 0 :
            return [False,'This name cannot be used because the user already has it.']
        hash_password = str(password)
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encPass = fernet.encrypt(hash_password.encode())
        StrEncPass = encPass.decode("utf-8")
        sql_insert = "INSERT INTO tb_player_account (username, password, secret_key) VALUES (%s,%s,%s)"
        value = (username,StrEncPass,key)
        resultInsert = insertSQL(sql_insert,value)
        if resultInsert[0] != True:
            return [False, resultInsert[1]]
        elif resultInsert[0] == True :
            data_return = {
                "message": "create account player success",
                "username": username
            }
            return [True,data_return]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return[False,str(e)]

def login(username,password):
    try :
        ResLogin = AuthLogin(username,password)
        if ResLogin[0] == True:
            ResGenToken = GenToken(username)
            if ResGenToken[0] != True :
                return [False,ResGenToken[1]]
            else :
                token = ResGenToken[1]['token']
                time_expire = ResGenToken[1]['time_expire']
                key = ResGenToken[1]['key']
                sql_insert = "INSERT INTO tb_token_player (token,time_expire,key_decode) VALUES (%s,%s,%s)"
                value = (token,time_expire,key)
                ResInsert = insertSQL(sql_insert,value)
                if ResInsert[0] == True :
                    data_return = {
                        "token": token
                    }
                    return [True,data_return]
                else :
                    return [False,ResInsert[1]]

        else :
            return [False,ResLogin[1]]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return[False,str(e)]

def authen_account(token):
    try :
        datetime_now = datetime.today()
        sql = "SELECT key_decode FROM tb_token_player WHERE token = %s and time_expire > %s"
        value = (token,datetime_now)
        result = selectSQL(sql,value)
        if result[0] == False or len(result[1]) == 0:
            return [False,'Unauthorized']
        query = result[1]
        key = query[0]['key_decode']
        byte_token = bytes(token, 'utf-8')
        fernet = Fernet(key)
        decMessage = fernet.decrypt(byte_token).decode()
        return [True,decMessage]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return [False,str(e)]