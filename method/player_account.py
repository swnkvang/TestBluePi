from config.lib import *
from config.db_maria import *

def create_account():
    try :
        createAt = datetime.today()
        time_expire = datetime.today() + timedelta(days=1)
        account_id = uuid.uuid4()
        message = str(account_id)
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())
        token = encMessage.decode("utf-8")
        # decMessage = fernet.decrypt(encMessage).decode()
        # print("decrypted string: ", decMessage)
        sql_insert = "INSERT INTO player_account (token,time_expire,key_decode,createAt) VALUES (%s,%s,%s,%s)"
        value = (token,time_expire,key,createAt)
        insertSQL(sql_insert,value)
        return [True,token]
    except Exception as e:
        print(str(e))
        return[False,str(e)]

def authen_account(token):
    try :
        datetime_now = datetime.today()
        sql = "SELECT key_decode FROM player_account WHERE token = %s and time_expire > %s"
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
        print(str(e))
        return [False,str(e)]