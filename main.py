from config.env import *
from config.lib import *
from api.api_game import * 
from api.api_login import *


if __name__ == "__main__":
    if type_product == 'uat':
        uvicorn.run("main:app", host="0.0.0.0", port=8500, log_level="info",reload=True,workers=4)
    elif type_product == 'prd':
        uvicorn.run("main:app", host="0.0.0.0", port=8502, log_level="info",reload=True,workers=4)
