from fastapi import FastAPI 
from pydantic import BaseModel #se utiliza para definir una entidad, que nos sirva para definir a los usuarios

app = FastAPI()

#Definimos la entidad user
class User(BaseModel):
    name: str
    surname: str
    age: int
    id: int

users_list = [User(name= "Luciano", surname="Aquino", age = 21, id = 1),
User(name= "Ignacio", surname="Aquino", age = 6, id = 2),
User(name= "Pepe", surname="Aquino", age =22, id = 3)]

#iniciar el servidor con el comando uvicorn users:app --reload
@app.get("/users")
async def users():
    return users_list
#capturamos el id del usuario y llamamos por patg
@app.get("/user/{id}")
async def user_id(id:int):
    #filtes es una funcion pre cargada de python, es de orden superior porque se encaga de hacer operaciones complejas y devolvernos un resultado
    users = filter (lambda user: user.id == id, users_list)
    #Ocupamos try para devolver un mensaje de error cuando no se encuentra el id del user
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}

#Llamar por query
@app.get("/userquery/")
async def user_id(id:int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}
   