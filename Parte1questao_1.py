from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import HuggingFaceHub
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API de Geração de Texto!"}

def get_gpt2_model():
    return HuggingFaceHub(
        repo_id="gpt2",
        huggingfacehub_api_token="HUGGINGFACEHUB_API_TOKEN",
        model_kwargs={"temperature": 0.7, "max_length": 150}
    )

class TextoEntrada(BaseModel):
    texto: str

# Rota para gerar texto com o modelo GPT-2
@app.post("/gerar-texto/")
async def gerar_texto(entrada: TextoEntrada):
    llm = get_gpt2_model()
    output = llm.generate([entrada.texto])
    texto_gerado = output.generations[0][0].text
    return {"texto_gerado": texto_gerado}
