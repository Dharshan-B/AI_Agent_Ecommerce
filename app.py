from fastapi import FastAPI
from pydantic import BaseModel
from utils.llm_handler import question_to_sql
from utils.sql_runner import run_query

app = FastAPI()

#Model Adding
class Question(BaseModel):
    question: str

# endpoint
@app.post("/ask")
async def ask_question(input: Question):
    user_question = input.question
    sql = question_to_sql(user_question)
    db_response = run_query(sql)

    return {
        "question": user_question,
        "sql_query": sql,
        "response": db_response
    }
