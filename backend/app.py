from enum import Enum
from fastapi import FastAPI, HTTPException, UploadFile
from pydantic import BaseModel
import uuid
from uuid import UUID

app = FastAPI()

CLASSIFICATION_REQUESTS = {}

def send_email(request_id: str, image_data: UploadFile) -> None:
    pass

@app.post("/uploadimage/")
def upload_image(image_file: UploadFile):
    request_id: str = str(uuid.uuid4())
    CLASSIFICATION_REQUESTS[request_id] = None
    send_email(request_id, image_file)
    return {"request_id": request_id}


@app.get("/classification/{request_id}")
def get_classification_status(request_id: str):
    if request_id not in CLASSIFICATION_REQUESTS:
        raise HTTPException(status_code=404, detail="Request not found")
    
    result = CLASSIFICATION_REQUESTS[request_id]
    status = "complete" if result else "pending"
    
    return {"status": status, "result": result}

@app.patch("/updateclassification/{request_id}")
def update_classification(request_id: str, email_reply: str):
    CLASSIFICATION_REQUESTS[request_id] = email_reply
    return "success"
