from mcp_server.server import TextToSpeechTool, LogTool

class PetActivityAgent:
    def __init__(self, profile):
        self.profile = profile
        self.tts = TextToSpeechTool()
        self.log = LogTool()

    def play(self):
        message = (
            f"Play session started with {self.profile.name}. "
            f"Favorite toy: {self.profile.favorite_toy}. "
            f"Personality: {self.profile.personality}."
        )
        self.tts.run(message)
        self.log.run(f"PLAY: {message}")
