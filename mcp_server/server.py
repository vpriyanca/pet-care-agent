import json
import subprocess
import datetime

# ---------------------------------------------------------
# PetProfilesTool — DISABLED to prevent duplicate UI
# ---------------------------------------------------------
class PetProfilesTool:
    def run(self):
        # Your app.py loads pet_profiles.json directly.
        # Returning an empty structure prevents Streamlit from rendering UI twice.
        return {"dogs": [], "cats": []}


# ---------------------------------------------------------
# PetDataTool — still needed for breed-specific care
# ---------------------------------------------------------
class PetDataTool:
    def run(self):
        with open("data/pet_data.json", "r") as f:
            return json.load(f)


# ---------------------------------------------------------
# TextToSpeechTool — macOS 'say' command
# ---------------------------------------------------------
class TextToSpeechTool:
    def run(self, text):
        subprocess.run(["say", text])


# ---------------------------------------------------------
# LogTool — simple timestamped event logger
# ---------------------------------------------------------
class LogTool:
    def run(self, event):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("data/log.txt", "a") as f:
            f.write(f"[{timestamp}] {event}\n")
