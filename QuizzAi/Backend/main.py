from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from crewai import Crew, Task, Agent
from config import Config
from utils.crew import agent_maneger
from utils.pdf_parser import extract_text
from utils.sessions import session_manager
import os
import json
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

@app.get("/session/{chat_id}")
def get_session_info(chat_id:str):
    session = session_manager.get_session(chat_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    else:
        return session
    
@app.delete("/session/{chat_id}")
def delte_session(chat_id:str):
    session = session_manager.get_session(chat_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    agent_maneger.clean_session(session["crew_session_id"])
    session_manager.delete_session(chat_id)
    return {"message":"session deleted!!"}

@app.post("/api/pdf/upload/{chat_id}")
async def upload(chat_id:str , file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")


    session = session_manager.get_session(chat_id)
    if not session:
        return{"error": "Invalid session"}
    
    file_path = f"temp_{chat_id}.pdf"
    with open(file_path,"wb") as f:
        f.write(file.file.read())

    text = extract_text(file_path)    
 
    session["pdf_text"]=text
    session["processed"]=True

    agent_maneger.add_to_memory(session["crew_session_id"],text)
    os.remove(file_path)
    return {"message": "PDF processed & memory updated",
            "text": text,
            "filename":file.filename
            }
@app.post("/upload/{chat_id}")
async def upload_pdf_to_session(chat_id:str, file:UploadFile=File(...)):
    session = session_manager.get_session(chat_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    temp_path = f"temp_{chat_id}.pdf"
    try:
        
        with open(temp_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        pdf_text = extract_text(temp_path)
        
       
        session_manager.update_session(chat_id, {
            "pdf_text": pdf_text,
            "pdf_filename": file.filename,
            "processed": True
        })
        agent_maneger.add_to_memory(session["crew_session_id"],pdf_text)
        return {
            "message": "PDF processed and memory updated",
            "filename": file.filename
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(ex)}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.post("/generate/{chat_id}")
def generate(chat_id:str ,typeof:str,count:int ):

    session = session_manager.get_session(chat_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if not session["processed"]:
        raise HTTPException(status_code=400, detail="No PDF uploaded for this session")


    crew_id = session["crew_session_id"]

    prompt=""
    if typeof=="mcq":
        prompt = f"Generate {count} Mcqs from the stored pdf content and given them in a json file with question,answer,correct answer,explanation why it is correct"
    elif typeof=="short":
        prompt = f"Generate {count} short questions from the stored pdf content and given them in a json file with question,answer,correct answer,explanation why it is correct"
    elif typeof=="long":
        prompt = f"Generate {count} long questions from the stored pdf content and given them in a json file with question,answer,ypecorrect answer,explanation why it is correct"
    elif typeof=="chat":
        prompt=f"reply according to asked quesion and return the answer in the form of a json file with the asked question and its respective answer"
    else :
        raise HTTPException(status_code=400, detail="Invalid question type. Use: mcq, short, or long")
    
    result = agent_maneger.run_agent(prompt,crew_id)
    try:
        questions = json.loads(result)  
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error generating questions: {str(ex)}")
    session_manager.add_message(chat_id,{
            "type": "generation",
            "question_type": typeof,
            "count": count,
            "result": questions
    })
    return{
        "type":typeof,
        "count":count,
        "questions":questions

    }




        






    