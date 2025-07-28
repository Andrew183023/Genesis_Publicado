from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Pegando a chave da OpenAI do ambiente
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

        # Aqui é onde normalmente dá problema:
        mensagem = resposta["choices"][0]["message"]["content"]

        return {"resposta": mensagem}

    except Exception as e:
        return {"erro": str(e)}


