from typing import Union
from fastapi import FastAPI
from clientes import router as clientes_router
from contas import router as contas_router

app = FastAPI( 
    title="Lincoln Portfolio",
    description="Portfolio de projetos desenvolvidos por Lincoln",
    version="1.0.0")

@app.get("/")
def welcome_lincoln_portfolio():
    return {"Lincoln Portfolio": "Servidor Rodando"}

app.include_router(clientes_router, prefix="/api")
app.include_router(contas_router, prefix="/api")