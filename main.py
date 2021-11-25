from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/contacto_nuevo/")
async def create_item(nombre: str,telefono:str):
    return guarda_datos(nombre=nombre,telefono=telefono)
     

def guarda_datos(nombre,telefono):
    f = open('contactos.txt', 'a')
    with open('contactos.txt', 'a') as f:
        # Procesamiento del fichero
        data_set = {"nombre": nombre, "telefono": telefono}
        json_dump = json.dumps(data_set)
        f.write(json_dump)

    f.close()
        
@app.get("/listar_contactos/")
def read():
    
    f = open('contactos.txt', 'r')
    with open('contactos.txt', 'r') as f:
        json_object = json. loads(f.read())
        
    return json_object

@app.get("/borrar_contactos/")
def borrar():
    
    
    f = open('contactos.txt', 'w')
    with open('contactos.txt', 'w') as f:
        f.write("")
        
    return ""
