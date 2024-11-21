from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import FakeListLLM

app = FastAPI()

fake_llm = FakeListLLM(responses=["Olá!", 
                                  "Estou bem e você?",
                                  "Bom dia!",
                                  "Boa noite!"
                                  ])

class InputData(BaseModel):
    question: str

@app.post("/chatbot/")
async def chatbot(input_data: InputData):
    response = fake_llm.invoke(input_data.question)
    return {"response": response}
