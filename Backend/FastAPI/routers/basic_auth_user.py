from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User):
    password:str

user_db = {
    "lucho":{
        "username": "lucho",
        "full_name": "luciano Aquino",
        "email": "lucho@gmail.com",
        "disable": False,
        "password": "123456"
        
    },
     "lucho1":{
        "username": "lucho1",
        "full_name": "luciano Aquino1",
        "email": "lucho@gmail.com1",
        "disable": True,
        "password": "654321"
        
    }
    
}
def search_user(username:str):
    if username in user_db:
        return UserDB(user_db[username])

@app.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    }
    
