from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from crewai import Crew, Task, Agent
from config import Config
from utils.crew import run_agent,add_to_memory
from utils.pdf_parser import extract_text
from utils.sessions import session_manager
import os
app = FastAPI(
    title=Config.APP_NAME,
    description="AI-powered question generation from PDFs",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
API_BASE_URL = "http://127.0.0.1:5503"


@app.post("/session")
def new_session():
    chat_id,data = session_manager.create_session()
    return { "chatId":chat_id , 
            "crewSessionId": data["create_session_id"],
            "created_at": data["created_at"]
            }

@app.post("/upload/{chat_id}")
async def upload(chat_id:str , file: UploadFile = File(...)):
    session = session_manager.get_session(chat_id)
    if not session:
        return{"error": "Invalid session"}
    
    file_path = f"temp_{chat_id}.pdf"
    with open(file_path,"wb") as f:
        f.write(file.file.read())

    text = extract_text(file_path)    
 
    session["pdf_text"]=text
    session["processed"]=True

    add_to_memory(session["crew_session_id"],text)
    os.remove(file_path)
    return {"message": "PDF processed & memory updated"}

@app.post("/generate/{chat_id}")
def generate(chat_id:str ,type:str,count:int):
    session = session_manager.get_session(chat_id)
    if not session:
        return {"error": "Invalid session"}
    crew_id = session["crew_session_id"]
    prompt=""
    if type=="mcq":
        prompt = f"Generate {count} Mcqs from the stored pdf content and given them in a json file with question,answer,correct answer,explanation why it is correct"
    elif type=="short":
        prompt = f"Generate {count} short questions from the stored pdf content and given them in a json file with question,answer,correct answer,explanation why it is correct"
    elif type=="long":
        prompt = f"Generate {count} long questions from the stored pdf content and given them in a json file with question,answer,correct answer,explanation why it is correct"
    result = run_agent(crew_id,prompt)    
    return {"result":result}

@app.get("/session/{chat_id}")
def get_session_info(chat_id:str):
    session = session_manager.get_session(chat_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    else:
        return session
    
    





    