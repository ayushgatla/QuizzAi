from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from crewai import Crew, Task, Agent
from config import Config
from utils.crew import get_mcq_agent
from utils.pdf_parser import extract_text_from_pdf, validate_pdf_file, get_pdf_preview

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

@app.post("/api/pdf/upload")
async def upload(file: UploadFile = File(...)):
    pdf_text = extract_text_from_pdf(file)
    agent = get_mcq_agent(pdf_text)
    task = Task(
        name="Generate MCQs",
        description="Generate MCQs from the given PDF text",
        expected_output="JSON structured data containing question,options,answers,difficulty level,topic,and question type",
        agent = agent,
    )
    crew = Crew(agents=[agent],tasks=[task])
    result = crew.run()
    return {"mcqs":result}