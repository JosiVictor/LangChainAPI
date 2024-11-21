from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import HuggingFaceHub
import os

app = FastAPI()

def get_translation_model():
    huggingfacehub_api_token = "HUGGINGFACEHUB_API_TOKEN"
    
    return HuggingFaceHub(
        repo_id="Helsinki-NLP/opus-mt-en-fr",
        huggingfacehub_api_token=huggingfacehub_api_token,
        model_kwargs={"temperature": 0.5}
    )

class TextoEntrada(BaseModel):
    texto: str

# Rota para traduzir o texto de inglês para francês
@app.post("/traduzir/")
async def traduzir_texto(entrada: TextoEntrada):
    llm = get_translation_model()
    output = llm.invoke(entrada.texto)
    return {"texto_traduzido": output}
