from mcp_server.server import TextToSpeechTool, LogTool

class PetHealthAgent:
    def __init__(self, profile):
        self.profile = profile
        self.tts = TextToSpeechTool()
        self.log = LogTool()

    def generate_alert(self, behavior, mood):
        breed = self.profile.breed
        personality = self.profile.personality
        medical = self.profile.medical_condition

        alerts = []

        # -----------------------------
        # Immediate Medical Alerts
        # -----------------------------
        if any(x in behavior for x in ["vomit", "diarrhea", "limp", "refusal", "cough"]):
            alerts.append("Possible illness detected. Monitor closely and consider contacting a vet.")

        # -----------------------------
        # Behavioral Alerts
        # -----------------------------
        if mood in ["anxious", "restless", "high anxiety"]:
            alerts.append("Your pet may be stressed. Provide a calm environment and reassurance.")

        # -----------------------------
        # Breed-Specific Alerts
        # -----------------------------
        if breed == "Bulldog" and "pant" in behavior:
            alerts.append("Bulldogs are prone to overheating. Ensure a cool environment.")

        if breed == "Husky" and mood == "restless":
            alerts.append("Huskies need high activity. Consider a long walk or run.")

        if breed == "Beagle" and mood == "restless":
            alerts.append("Beagles get bored easily. Provide sniffing or puzzle activities.")

        if breed == "Persian" and "eye" in behavior:
            alerts.append("Persians often have eye discharge. Clean gently if needed.")

        if breed == "Sphynx" and "scratch" in behavior:
            alerts.append("Sphynx cats have sensitive skin. Check for irritation.")

        # -----------------------------
        # Personality Alerts
        # -----------------------------
        if personality == "shy" and mood == "fearful":
            alerts.append("Your shy pet may be overwhelmed. Reduce noise and stimuli.")

        if personality == "energetic" and mood == "tired":
            alerts.append("Unusual tiredness in an energetic pet may indicate fatigue or illness.")

        # -----------------------------
        # Medical Condition Alerts
        # -----------------------------
        if medical == "arthritis" and mood == "pain":
            alerts.append("Arthritis pain flare detected. Avoid strenuous activity.")

        if medical == "allergies" and "lick" in behavior:
            alerts.append("Allergy irritation detected. Check skin and consider antihistamines.")

        if medical == "anxiety" and mood == "high anxiety":
            alerts.append("High anxiety episode detected. Provide comfort and reduce triggers.")

        # -----------------------------
        # Output
        # -----------------------------
        if alerts:
            for alert in alerts:
                self.tts.run(alert)
                self.log.run(f"Health alert for {self.profile.name}: {alert}")
        else:
            self.tts.run("No health concerns detected.")
            self.log.run(f"No health alerts for {self.profile.name}.")
