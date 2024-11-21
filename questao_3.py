from fastapi import FastAPI
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEndpoint
import os

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate_to_german/")
async def translate_to_german(request: TranslationRequest):
    llm = HuggingFaceEndpoint(
        repo_id="Helsinki-NLP/opus-mt-en-de",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )
    response = llm.invoke(request.text)
    return {"translated_text": response}
