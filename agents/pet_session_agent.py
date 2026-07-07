import json
from agents.pet_profile import PetProfile
from agents.pet_care_agent import PetCareAgent
from agents.pet_mood_agent import PetMoodAgent
from agents.pet_activity_agent import PetActivityAgent
from mcp_server.server import TextToSpeechTool, LogTool

class PetSessionAgent:
    def __init__(self, species, index):

        # Load profiles directly from JSON (NOT PetProfilesTool)
        with open("data/pet_profiles.json", "r") as f:
            profiles_data = json.load(f)

        raw = profiles_data[species][index]

        self.profile = PetProfile(
            name=raw["name"],
            breed=raw["breed"],
            age=raw["age"],
            weight=raw["weight"],
            notes=raw.get("notes", ""),
            personality=raw.get("personality", ""),
            favorite_toy=raw.get("favorite_toy", ""),
            favorite_food=raw.get("favorite_food", ""),
            medical_condition=raw.get("medical_condition", ""),
            vaccination_date=raw.get("vaccination_date", ""),
            last_vet_visit=raw.get("last_vet_visit", ""),
            grooming_frequency=raw.get("grooming_frequency", ""),
            feeding_schedule=raw.get("feeding_schedule", ""),
            adoption_date=raw.get("adoption_date", ""),
            photo_url=raw.get("photo_url", "")
        )

        self.care = PetCareAgent(self.profile)
        self.mood = PetMoodAgent(self.profile)
        self.activity = PetActivityAgent(self.profile)

        self.tts = TextToSpeechTool()
        self.log = LogTool()

    def run_feeding(self):
        self.care.feed()

    def run_grooming(self):
        self.care.groom()

    def run_play(self):
        self.activity.play()

    def check_mood(self, behavior):
        self.mood.detect_mood(behavior)
