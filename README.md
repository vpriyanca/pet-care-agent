🐾 Pet Care Agent
A calm, multi‑agent pet‑care assistant that onboards cats and dogs, manages feeding, grooming, playtime, and mood detection, with both CLI and Streamlit UI.

✨ Features
Onboard multiple pets (cats and dogs)
Store detailed pet profiles (name, species, breed, age, weight, notes)
Species‑aware feeding, grooming, and activity actions
Mood detection from natural‑language behavior descriptions
Voice guidance using macOS say
Activity logging to data/log.txt
Clean Streamlit UI with Dogs, Cats, and Onboarding tabs
Modular multi‑agent architecture (Care, Mood, Activity, Session)
JSON‑driven data for pet profiles and breed‑specific care

🧠 Architecture Overview
The Pet Care Agent uses a multi‑agent design:
PetCareAgent — feeding & grooming
PetMoodAgent — mood detection
PetActivityAgent — play sessions
PetSessionAgent — orchestrates all agents

Tools used:
TextToSpeechTool — macOS voice output
LogTool — event logging
PetDataTool — breed‑specific care data

#Run the UI
streamlit run ui/app.py

#Run the CLI
python cli/main.py

#Project Structure
pet-care-agent/
│
├── agents/
│   ├── pet_care_agent.py
│   ├── pet_mood_agent.py
│   ├── pet_activity_agent.py
│   └── pet_session_agent.py
│
├── mcp_server/
│   ├── server.py
│   └── tools/
│
├── ui/
│   └── app.py
│
├── data/
│   ├── pet_profiles.json
│   └── pet_data.json
│
└── README.md

#Optional: Run Inside Antigravity Sandbox
from antigravity import Sandbox
from agents.pet_session_agent import PetSessionAgent
from mcp_server.server import TextToSpeechTool, LogTool, PetDataTool

sandbox = Sandbox()
sandbox.register_agent("pet_session", PetSessionAgent("dogs", 0))
sandbox.register_tool("tts", TextToSpeechTool())
sandbox.register_tool("log", LogTool())
sandbox.register_tool("pet_data", PetDataTool())

sandbox.run("pet_session", "run_feeding")
sandbox.run("pet_session", "run_grooming")
sandbox.run("pet_session", "run_play")
sandbox.run("pet_session", "check_mood", "hiding and anxious")

#Installation
git clone https://github.com/YOURNAME/pet-care-agent.git
cd pet-care-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#Data Files
pet_profiles.json — user‑added pet profiles

pet_data.json — breed‑specific feeding, grooming, and activity guidance

#Demo Video
YouTube: uploaded.

#🙌 Acknowledgements
Built as part of the Kaggle Multi‑Agent Systems track, using MCP tools and Streamlit.

