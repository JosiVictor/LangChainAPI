from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate/")
async def translate(request: TranslationRequest):
    api_key = "OPENAI_API_KEY"

    template = ChatPromptTemplate.from_template(
        "You are an English to French translator. Translate this: {text}"
    )
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)
    response = llm.invoke(template.format_messages(text=request.text))
    return {"translated_text": response.content}
