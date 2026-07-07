from mcp_server.server import TextToSpeechTool, LogTool

class PetMoodAgent:
    def __init__(self, profile):
        self.profile = profile
        self.tts = TextToSpeechTool()
        self.log = LogTool()

    def detect_mood(self, behavior_description):
        behavior = behavior_description.lower()

        if any(word in behavior for word in ["lethargic", "tired", "not eating", "weak"]):
            mood = "possibly unwell or low energy"
        elif any(word in behavior for word in ["hyper", "zoomies", "running", "excited"]):
            mood = "very energetic and playful"
        elif any(word in behavior for word in ["hiding", "anxious", "scared", "nervous"]):
            mood = "anxious or fearful"
        else:
            mood = "normal or unclear from description"

        message = (
            f"Mood check for {self.profile.name}: "
            f"Based on behavior, mood is {mood}."
        )

        self.tts.run(message)
        self.log.run(f"MOOD: {message}")
