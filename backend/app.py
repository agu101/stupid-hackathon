from fastapi import FastAPI

app = FastAPI()

REQUESTS = {}

# receive image, save to REQUESTS with unique ID, send email, and sends id back
@app.post("/send_image")
def read_root():
    return {"Hello": "World"}

# receives list of ids and returns answers if we have them or status
@app.get("/get_classification_status")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

