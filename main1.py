from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

api_key = os.getenv("Gemini_key_here")

client = genai.Client(
    api_key=api_key
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=req.message
        )

        return {
            "reply": getattr(response, "text", str(response))
        }

    except Exception as e:
        return {
            "reply": "Gemini error occurred",
            "error": str(e)
        }
