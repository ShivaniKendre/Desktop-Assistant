import asyncio
import edge_tts
import datetime
from playsound import playsound
import os
import speech_recognition as sr
import webbrowser
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


from google import genai
from config import apikey

client = genai.Client(api_key=apikey)

VOICE = "en-IN-NeerjaNeural"
FILE = "voice.mp3"


chatStr = ""

# ---------- SPEAK ----------
def speak(audio):
    async def _speak():
        communicate = edge_tts.Communicate(
            text=audio,
            voice=VOICE,
            rate="+5%",
            volume="+0%",
            pitch="+0Hz"
        )
        await communicate.save(FILE)
        playsound(FILE)
        if os.path.exists(FILE):
            os.remove(FILE)

    asyncio.run(_speak())

# ---------- WISH ----------
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good morning Shivani!")
    elif hour < 18:
        speak("Good afternoon Shivani!")
    else:
        speak("Good evening Shivani!")

    speak("How may I help you?")

# ---------- LISTEN ----------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"You said: {query}\n")
        return query
    except Exception:
        print("Say that again please...")
        return ""
    
import re

def clean_for_speech(text):
    # Remove markdown symbols
    text = re.sub(r'[*_`#>-]', '', text)
    # Extra spaces clean
    text = re.sub(r'\s+', ' ', text)
    return text.strip()  

# ---------- CHAT (GEMINI) ----------
def chat(query):
    global chatStr
    chatStr += f"You: {query}\nNova: "

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=chatStr
        )

        reply = response.text.strip()
        clean_reply = clean_for_speech(reply)

       
        print("\n================ AI RESPONSE ================\n")
        print(reply)
        print("\n============================================\n")

       
        speak(clean_reply)

    except Exception as e:
        print("GEMINI ERROR:", e)
        speak("My AI service is currently unavailable.")
        return ""

# ================= HANDS (PyAutoGUI) =================

def hand_open_app(app_name):
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.typewrite(app_name)
    time.sleep(0.5)
    pyautogui.press("enter")

def hand_type(text, speed=0.01):
    pyautogui.typewrite(text, interval=speed)

def hand_scroll_down(steps=2):
    for _ in range(steps):
        pyautogui.scroll(-500)
        time.sleep(0.7)

def hand_scroll_up(steps=2):
    for _ in range(steps):
        pyautogui.scroll(500)
        time.sleep(0.7)

def hand_save(filename):
    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    pyautogui.typewrite(filename)
    pyautogui.press("enter")

def execute_command(query):
    query = query.lower()

    if "open chrome" in query:
        hand_open_app("chrome")
    elif "open notepad" in query:
        hand_open_app("notepad")
    elif "open word" in query:
        hand_open_app("word")
    elif query.startswith("type"):
        hand_type(query.replace("type", "").strip())
    elif "scroll down" in query:
        hand_scroll_down()
    elif "scroll up" in query:
        hand_scroll_up()
    elif "save file as" in query:
        hand_save(query.replace("save file as", "").strip())
    elif "search" in query or "google" in query:
        text = query.replace("search", "").replace("google", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={text}")
    else:
        return False

    return True

browser_driver = None

def eyes_execute(action, value):
    global browser_driver

    if action == "web_search":
        service = Service(ChromeDriverManager().install())
        browser_driver = webdriver.Chrome(service=service)
        browser_driver.get("https://www.google.com")
        time.sleep(2)
        box = browser_driver.find_element(By.NAME, "q")
        box.send_keys(value)
        box.send_keys(Keys.RETURN)

    elif action == "read_headings":
        soup = BeautifulSoup(browser_driver.page_source, "html.parser")
        for h in soup.find_all("h3")[:int(value)]:
            speak(h.text)

    elif action == "read_paragraphs":
        soup = BeautifulSoup(browser_driver.page_source, "html.parser")
        for p in soup.find_all("p")[:int(value)]:
            speak(p.text[:200])

# ================= MAIN LOOP =================
if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()

        if not query:
            continue

        # 🔴 EXIT
        if "exit" in query or "quit" in query:
            speak("Goodbye Shivani")
            break

        # 🔁 RESET MEMORY
        if "reset chat" in query:
            chatStr = ""
            speak("Chat has been reset")
            continue

        # 🌐 OPEN SITES
        sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "stackoverflow": "https://stackoverflow.com",
            "gmail": "https://mail.google.com",
            "wikipedia": "https://www.wikipedia.org",
        }

        opened = False
        for name, url in sites.items():
            if f"open {name}" in query:
                speak(f"Opening {name}")
                webbrowser.open(url)
                opened = True
                break

        if opened:
            continue

        # 🎵 PLAY MUSIC
        if "play music" in query:
            speak("Playing music")
            os.startfile(r"D:\\Collage\\Namo Namo - Lyrical  Kedarnath  Sushant Rajput  Sara Ali Khan  Amit Trivedi  Amitabh B.mp3")
            continue

        # ⏰ TIME
        if "the time" in query:
            speak(datetime.datetime.now().strftime("The time is %H:%M:%S"))
            continue

        # 🖱 SYSTEM COMMANDS
        if execute_command(query):
            continue

        # 🤖 DEFAULT → AI
        chat(query)
        