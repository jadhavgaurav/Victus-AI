import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from victus_ai.core.logging_config import configure_logging

load_dotenv()
configure_logging()

app = FastAPI(title="Victus AI")

@app.get("/")
async def root():
    return {"message": "Victus AI backend is running."}

if __name__ == "__main__":
    uvicorn.run("victus_ai.main:app", host="0.0.0.0", port=8000, reload=True)
