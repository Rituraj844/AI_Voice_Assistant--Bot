import os
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
import shutil

app = FastAPI()

# --- API KEY SETTING ---
# আপনার OpenAI API Key এখানে বসান
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"
client = OpenAI(api_key=OPENAI_API_KEY)

# 'static' ফোল্ডার চেক ও মাউন্ট করা
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Error: index.html not found!</h1>", status_code=404)

@app.post("/process-voice")
async def process_voice(file: UploadFile = File(...)):
    if "YOUR_OPENAI_API_KEY" in OPENAI_API_KEY:
        return {"error": "API Key বসানো হয়নি।"}

    # ভয়েস ফাইল সেভ করা
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # ১. Speech to Text (Whisper)
        audio_file = open(temp_filename, "rb")
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        user_text = transcript.text

        # ২. AI response (GPT-4o)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful and sweet voice assistant. Answer in the language user speaks (Bangla/English)."},
                {"role": "user", "content": user_text}
            ]
        )
        ai_message = response.choices[0].message.content

        # ৩. Text to Speech (TTS)
        # এখানে আমরা টেক্সট হিসেবে ফেরত দিচ্ছি ফ্রন্টএন্ডে বাজানোর জন্য
        return {"user_text": user_text, "ai_response": ai_message}

    except Exception as e:
        return {"error": str(e)}
    finally:
        audio_file.close()
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)