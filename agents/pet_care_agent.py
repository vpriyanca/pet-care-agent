from mcp_server.server import TextToSpeechTool, LogTool

class PetCareAgent:
    def __init__(self, profile):
        self.profile = profile
        self.tts = TextToSpeechTool()
        self.log = LogTool()

    def feed(self):
        message = (
            f"Feeding {self.profile.name} ({self.profile.breed}). "
            f"Schedule: {self.profile.feeding_schedule}. "
            f"Favorite food: {self.profile.favorite_food}."
        )
        self.tts.run(message)
        self.log.run(f"FEED: {message}")

    def groom(self):
        message = (
            f"Grooming {self.profile.name} ({self.profile.breed}). "
            f"Grooming frequency: {self.profile.grooming_frequency}."
        )
        self.tts.run(message)
        self.log.run(f"GROOM: {message}")
