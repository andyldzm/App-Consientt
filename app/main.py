from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(title="API Consientt")

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "API de servicios podológicos Consientt funcionando"}
