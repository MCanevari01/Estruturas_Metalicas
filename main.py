from fastapi import FastAPI
from database import inicializar_banco_de_dados
from routers import categoria
from routers import material


app = FastAPI(
    title= "ERP Estruturas Metálicas",
    description= "Mini ERP para empresa de Estruturas Metálicas",
    version= "0.3.1"
)


@app.on_event ("startup")
def inicializar_sistema():
    inicializar_banco_de_dados()
    print("Sistema inicializado com sucesso!")

@app.get("/")
def pagina_inicial():
    return {"status": "Online", "mensagem": "Bem-vindo ao Sistema do miniERP!"}

app.include_router(categoria.router)
app.include_router(material.router)
    