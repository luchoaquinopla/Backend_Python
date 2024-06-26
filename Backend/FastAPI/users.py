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

#capturamos el id del usuario y llamamos por path
@app.get("/user/{id}")
async def user_id(id:int):
    #filter es una funcion pre cargada de python, es de orden superior porque se encaga de hacer operaciones complejas y devolvernos un resultado
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
    
#con Post agregamos el usuario a la falsa base de datos
@app.post("/user/")
async def user(user:User):
    #Con este if comprobamos que el usuario sea unico a traves de la funcion search_user
    if type(search_user(user.id)) == User:
        return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)

#con Put actualizamos el objeto completo
@app.put("/user/")
async def user(user:User):
    found = False
    #este for recorre los elementos de la lista 
    for index, saved_user in enumerate(users_list):
        #Este if verifica si el id del usuario guardado (saved_user.id) es igual al id del usuario proporcionado en la solicitud (user.id).
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    #Después de recorrer toda la lista, si la variable found sigue siendo False, significa que no se encontró ningún usuario con el id proporcionado.
    if not found:
        return {"error":"no se ha encontrado el usuario"}

#ocupamos delete para eliminar un objeto
@app.delete("/user/{id}")
async def user(id:int):
    found = False
    #este for recorre los elementos de la lista 
    for saved_user in users_list:
        if saved_user.id == id:
            users_list.remove(saved_user)
            found = True
    #Después de recorrer toda la lista, si la variable found sigue siendo False, significa que no se encontró ningún usuario con el id proporcionado.
    if not found:
        return {"error":"no se ha encontrado el usuario"}
        

#funcion que filtra los ususarios por sus ids
def search_user(id:int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}


        
        
    
   