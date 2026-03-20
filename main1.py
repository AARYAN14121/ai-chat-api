from fastapi import FastAPI
from pydantic import BaseModel
import os
from google import genai

app = FastAPI()

# Initialize client
client = genai.Client(api_key=os.getenv("AIzaSyCSXaGBhgDM7x3Wy5_ayXguh_z4b9xBHOY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=req.message
        )

        reply = response.text if hasattr(response, "text") else str(response)

        return {
            "reply": reply
        }

    except Exception as e:
        return {
            "reply": "Gemini error occurred",
            "error": str(e)
        }