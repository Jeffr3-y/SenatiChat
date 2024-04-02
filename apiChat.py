from fastapi import FastAPI, Request, Form
import mysql.connector
from mensaje import mensaje
#from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

obj_Mensaje = mensaje("bienvenido")
app = FastAPI()
#templates = Jinja2Templates(directory="Pagina")

mi_Conexion = mysql.connector.connect(
    host = "172.60.10.212",
    user = "usr_chat",
    passwd = "Aa123456",
    db = "chat")

app.mount("/home", StaticFiles(directory = "Pagina"), name="index")

#@app.get("/")
#def index(request: Request):
#    return templates.TemplateResponse("/index.html",{"request": request})
@app.get("/enviar_Mensaje")
def enviar_Mensaje(mensaje: str):
    cursor = mi_Conexion.cursor()
    mensaje_Encriptado = obj_Mensaje.codificar(mensaje)
    cursor.execute("insert into mensajes (Mensaje, Usuario) values('"+mensaje+"','Jeffrey')")
    mi_Conexion.commit()
    return "Jeffrey: " + mensaje 
@app.get("/listar_Mensajes")
def listar_Mensajes():
    cursor = mi_Conexion.cursor()
    cursor.execute("select * from mensajes")
    result = cursor.fetchall()
    return result
@app.get("/listar_Mensajes_De_Un_Usuario")
def listar_Mensajes_De_Un_Usuario(user1: str, user2: str):
    cursor = mi_Conexion.cursor()
    cursor.execute("select * from mensajes where Usuario in ('"+user1+"','"+user2+"')")
    result = cursor.fetchall()
    return result