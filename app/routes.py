from fastapi import APIRouter, UploadFile, File
from app.schemas import QuestionRequest

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return {"message": "Document received", "filename": file.filename}

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": "This is a placeholder answer"
    }
