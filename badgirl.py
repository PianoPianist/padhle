import psutil
import ctypes 
import requests
import json
from playsound import playsound

def is_discord_running():
    for process in psutil.process_iter(['pid', 'name']):

        try:
    
            if process.info['name'].lower() == "discord.exe":
                return True
            elif process.info['name'].lower() == "chrome.exe":
                return True
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

CHUNK_SIZE = 1024 
XI_API_KEY = "sk_7d159f022247b8622f7509de1a37eb2f3f97ff47f0bc3cad" 
VOICE_ID = "IKne3meq5aSn9XLyUdCD" 
TEXT_TO_SPEAK = "behen ke lode. tujhe fir samjhana padhega kya" 
OUTPUT_PATH = "output.mp3" 

tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY
}

data = {
    "text": TEXT_TO_SPEAK,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8,
        "style": 0.0,
        "use_speaker_boost": True
    }
}

response = requests.post(tts_url, headers=headers, json=data, stream=True)

if response.ok:

    with open(OUTPUT_PATH, "wb") as f:
    
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)

else:

    print(response.text)


while True:
    if is_discord_running():
        ctypes.windll.user32.LockWorkStation()
    
        playsound('output.mp3')
        print('badgirl')
        break