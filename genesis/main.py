from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Ativar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Você pode restringir depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
FLOWMIND_URL = "http://flowmind:8001/api/ia/processar"

@app.post("/genesis/comando")
def comando_geral(payload: dict):
    prompt = payload.get("prompt", "Nenhum prompt recebido")

    try:
        resposta = requests.post(FLOWMIND_URL, json={"prompt": prompt})
        resposta_json = resposta.json()
        return {"resposta_da_flowmind": resposta_json["resposta"]}

    except Exception as e:
        return {"erro": str(e)}
