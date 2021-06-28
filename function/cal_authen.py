from pydantic.tools import T
from config.lib import *
from config.db_maria import *

def AuthLogin(username,password):
    try :
        sql_select = "SELECT * FROM tb_player_account WHERE username = ?"
        value = [username]
        resultSelect = selectSQL(sql_select,value)
        if resultSelect[0] == True:
            if len(resultSelect[1]) == 0 :
                return[False,'username or password Incorrect']
            passInDB = resultSelect[1][0]['password']
            secret_key = resultSelect[1][0]['secret_key']
            bytePass = bytes(passInDB, 'utf-8')
            fernet = Fernet(secret_key)
            decPass = fernet.decrypt(bytePass).decode()
            if password == decPass :
                return[True,'login success']
            else :
                return[False,'username or password Incorrect']
        else :
            return[False,'username or password Incorrect']
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return[False,str(e)]


def GenToken(username):
    try:
        time_expire = datetime.today() + timedelta(days=1)
        # account_id = uuid.uuid4()
        hash_username = str(username)
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encUsername = fernet.encrypt(hash_username.encode())
        token = encUsername.decode("utf-8")
        data_return = {
            "token": token,
            "key": key,
            "time_expire": time_expire
        }
        return [True,data_return]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return[False,str(e)]