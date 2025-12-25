🎙️ Smart AI Voice Assistant - Next-Gen Interaction

**Smart AI Voice Assistant** is an advanced AI-powered application that allows users to interact with artificial intelligence using their voice. It seamlessly converts speech to text, processes the intent using high-level LLMs, and provides human-like responses. This project showcases the integration of **FastAPI**, **Web Speech API**, and **OpenAI's Whisper & GPT models**.

---

## ❓ Key Project Objectives
During the development of this AI Assistant, the following core challenges and queries were addressed:
* **Real-time Speech Recognition:** How to accurately capture and transcribe human voice in various languages?
* **Intelligent Conversation:** How to maintain context and provide meaningful AI responses via voice commands?
* **Audio Visualizing:** How to create a dynamic UI that reacts to the user's voice input (Waveform Animation)?
* **Seamless Integration:** How to bridge the gap between frontend audio recording and backend AI processing?

---

## ✨ Features & Capabilities
This project is designed with a premium focus on user experience and technical efficiency:
* **Interactive UI/UX:** Features a sleek Glassmorphism design with a futuristic voice waveform that animates during listening.
* **Whisper AI Integration:** Uses OpenAI's Whisper model for highly accurate speech-to-text transcription.
* **Contextual Intelligence:** Powered by GPT-4o to provide smart, helpful, and natural-sounding answers.
* **Bilingual Support:** Capable of understanding and responding in both **Bangla** and **English**.
* **Instant Voice Feedback:** Converts AI text responses back into speech for a complete hands-free experience.

---

## 🛠 Tech Stack
* **Backend:** Python, FastAPI
* **Frontend:** Tailwind CSS, JavaScript (MediaRecorder API)
* **AI Engine:** OpenAI API (Whisper-1 & GPT-4o)
* **Speech Synthesis:** Web Speech Synthesis API
* **Server:** Uvicorn

---

## 🚀 Installation & Setup

Follow these steps to run the AI Voice Assistant on your local machine or Replit:

### 1. Install Dependencies
Run the following command in your terminal to install necessary packages:
```bash
pip install fastapi uvicorn openai python-multipart


2. Configure API Key
​Open main.py and navigate to line 11. Insert your OpenAI API Key:
OPENAI_API_KEY = "your_openai_api_key_here"


3. Project Structure
​Ensure your files are organized as follows:
​main.py (The backend logic)
​static/ (Folder)
​index.html (The frontend UI)
​requirements.txt


4. Run the Application
​Start the server with:
python main.py

Open your browser and go to http://localhost:8080. Don't forget to Allow Microphone Access!
