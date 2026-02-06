from fastapi import FastAPI
from pydantic import BaseModel
from resume_generator import generate_resume

app = FastAPI()

class ResumeInput(BaseModel):
    name: str
    title: str
    skills: str
    experience: str
    education: str

@app.post("/generate-resume")
def generate(data: ResumeInput):
    resume_text = generate_resume(data.dict())
    return {"resume_text": resume_text}

