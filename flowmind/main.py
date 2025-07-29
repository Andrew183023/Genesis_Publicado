from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# ✅ CORS liberado pra acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque por seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API KEY OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class Prompt(BaseModel):
    prompt: str

@app.post("/api/ia/processar")
def processar_ia(dados: Prompt):
    pensamento = dados.prompt

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é a FlowMind, a mente estratégica do Flow Core Group."},
                {"role": "user", "content": pensamento}
            ],
            max_tokens=200
        )

        mensagem = resposta.get("choices", [{}])[0].get("message", {}).get("content", "")

        if not mensagem:
            return {"erro": "Sem resposta da IA."}

        return {"resposta": mensagem}

    except Exception as e:
        return {"erro": str(e)}



