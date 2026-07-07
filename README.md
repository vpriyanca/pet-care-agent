# 🐾 Pet Care Agent
A calm, multi-agent pet care assistant that onboards cats and dogs, manages feeding, grooming, playtime, and mood detection, with both CLI and Streamlit interfaces.
---
## ✨ Features
- Onboard multiple pets (cats and dogs)
- Store detailed pet profiles
  - Name
  - Species
  - Breed
  - Age
  - Weight
  - Notes
- Species-aware feeding, grooming, and activity recommendations
- Mood detection from natural-language behavior descriptions
- Voice guidance using macOS `say`
- Activity logging to `data/log.txt`
- Clean Streamlit UI with:
  - 🐶 Dogs
  - 🐱 Cats
  - ➕ Onboarding
- Modular multi-agent architecture
- JSON-driven pet profiles and breed-specific care guidance
---
## Architecture
The Pet Care Agent uses a modular multi-agent design.
### Agents
- **PetCareAgent** – Feeding and grooming
- **PetMoodAgent** – Mood detection
- **PetActivityAgent** – Play sessions
- **PetSessionAgent** – Orchestrates all agents
### Tools
- **TextToSpeechTool** – macOS voice output
- **LogTool** – Event logging
- **PetDataTool** – Breed-specific care data
---
## Installation
```bash
git clone https://github.com/YOURNAME/pet-care-agent.git
cd pet-care-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
---
## Running the Application
### Streamlit UI
```bash
streamlit run ui/app.py
```
### Command Line Interface
```bash
python cli/main.py
```
---
## Project Structure
```text
pet-care-agent/
│
├── agents/
│   ├── pet_care_agent.py
│   ├── pet_mood_agent.py
│   ├── pet_activity_agent.py
│   └── pet_session_agent.py
│
├── cli/
│   └── main.py
│
├── ui/
│   └── app.py
│
├── mcp_server/
│   ├── server.py
│   └── tools/
│
├── data/
│   ├── pet_profiles.json
│   ├── pet_data.json
│   └── log.txt
│
├── requirements.txt
└── README.md
```
---
##  Data Files
### `pet_profiles.json`
Stores user-created pet profiles.
### `pet_data.json`
Contains breed-specific information for:
- Feeding
- Grooming
- Activities
- Care recommendations
---
##  Optional: Run Inside Antigravity Sandbox
```python
from antigravity import Sandbox
from agents.pet_session_agent import PetSessionAgent
from mcp_server.server import (
    TextToSpeechTool,
    LogTool,
    PetDataTool,
)
sandbox = Sandbox()
sandbox.register_agent(
    "pet_session",
    PetSessionAgent("dogs", 0)
)
sandbox.register_tool("tts", TextToSpeechTool())
sandbox.register_tool("log", LogTool())
sandbox.register_tool("pet_data", PetDataTool())
sandbox.run("pet_session", "run_feeding")
sandbox.run("pet_session", "run_grooming")
sandbox.run("pet_session", "run_play")
sandbox.run("pet_session", "check_mood", "hiding and anxious")
```
---
## Demo Video
**YouTube:** https://youtu.be/Ja-cJDZ31ZI
---
## 🙌 Acknowledgements
Built as part of the **Kaggle Multi-Agent Systems Track**, using **MCP tools** and **Streamlit**.
