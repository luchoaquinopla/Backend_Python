from fastapi import FastAPI 

app = FastAPI()

@app.get("/")

async def root():
    return "Hello world"

@app.get("/url")      
async def url():
    return{"url":"https://luchito.com/python"}
    