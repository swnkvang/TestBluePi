from typing import Optional
from fastapi import FastAPI
app = FastAPI()
from fastapi import BackgroundTasks,FastAPI, Form, Request, Header, Response, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time
import asyncio
import uvicorn
import random
import mariadb
import pymongo
import uuid
import jwt
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import json
import psycopg2
import sys, os
from bson.objectid import ObjectId



