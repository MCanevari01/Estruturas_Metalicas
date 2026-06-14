from fastapi import FastAPI
from database import inicializar_banco_de_dados


app = FastAPI(
    title= "ERP Estruturas Metálicas",
    description= "Mini ERP para empresa de Estruturas Metálicas",
    version= "1.0.0"
)


@app.on_event ("startup")
def inicializar_sistema():
    inicializar_banco_de_dados()
    print("Sistema inicializado com sucesso!")

@app.get("/")
def pagina_inicial():
    return {"status": "Online", "mensagem": "Bem-vindo ao Backend Seguro do miniERP!"}