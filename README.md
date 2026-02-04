# 🤖 JARVIS – AI Voice Assistant (Python + Gemini)

JARVIS is a smart, voice-controlled **AI assistant** built using **Python**, **Google Gemini AI**, and **Text-to-Speech** technology.  
It listens to your voice, understands commands, controls your system, browses the web, and answers questions intelligently — all in one seamless flow.

No modes. No switches.  
Just speak, and JARVIS does the rest.

---

## ✨ Features

- 🎙️ **Voice Input** using Speech Recognition  
- 🔊 **Natural Voice Output** using Edge TTS (Indian English voice)  
- 🧠 **AI Intelligence** powered by **Google Gemini**  
- 🖥️ **System Control**
  - Open applications (Chrome, Notepad, Word, etc.)
  - Type text automatically
  - Scroll up / down
  - Save files
- 🌐 **Web Actions**
  - Google search
  - Open YouTube, Gmail, Wikipedia, StackOverflow, etc.
- 📄 **Terminal Output**
  - AI responses displayed clearly in the terminal
- 🧹 **Clean Voice Responses**
  - Removes `*`, `_`, and markdown symbols while speaking
- 🔁 **Single Unified Flow**
  - No “AI mode on/off”
  - No “command/chat mode”
  - System commands first, AI as fallback (like real assistants)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini API**
- `speechrecognition`
- `edge-tts`
- `playsound`
- `pyautogui`
- `selenium`
- `webdriver-manager`
- `beautifulsoup4`

---

## 📁 Project Structure

```text
JARVIS/
│
├── Jarvis.py # Main AI assistant
├── config.py # Gemini API key
│
├── ai/ # (Optional) saved AI outputs
├── pycache/ # Auto-generated (safe to delete)
│
└── README.md
```
---


## 🔑 Setup Instructions


### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShivaniKendre/JARVIS.git
cd JARVIS
```
---

### 2️⃣ Install Required Libraries
```bash
pip install google-generativeai speechrecognition edge-tts playsound pyautogui selenium webdriver-manager beautifulsoup4
```
---
### 3️⃣ Get Gemini API Key
```bash
Visit 👉 https://aistudio.google.com/app/apikey
Create a Gemini API key
Copy the generated key
```
---
### 4️⃣ Configure API Key
```bash
Create or edit config.py:
apikey = "YOUR_GEMINI_API_KEY"
```
---
### ▶️ Run JARVIS
```bash
python Jarvis.py
After starting:
JARVIS will greet you
Speak any command or question

🗣️ Example Commands
System Commands
Open Chrome
Type Hello world
Scroll down
Save file as notes

Web Commands
Search Python AI projects
Open YouTube
Open Wikipedia

AI Questions
Who is Shah Rukh Khan?
Explain artificial intelligence
Write an email to my teacher

🧠 How JARVIS Works
User Voice
   ↓
Speech Recognition
   ↓
Is it a system command?
   ├─ Yes → Execute command
   └─ No  → Ask Gemini AI
                ↓
         Show response in terminal
                ↓
           Speak clean response

🧹 Cleanup Notes
You can safely delete:
__pycache__/
.pyc files
Old test files

Do NOT delete:
Jarvis.py
config.py

🚀 Future Improvements
Wake word support (“Hey Jarvis”)
Streaming AI responses
Persistent memory
GUI version
Convert to .exe
Mobile app integration

🙌 Credits
Developed by Shivani Kendre
AI powered by Google Gemini
