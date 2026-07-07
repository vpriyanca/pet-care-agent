import json
import streamlit as st
from agents.pet_session_agent import PetSessionAgent
from mcp_server.server import PetDataTool

PROFILES_PATH = "data/pet_profiles.json"

def save_profiles(profiles):
    with open(PROFILES_PATH, "w") as f:
        json.dump(profiles, f, indent=2)

st.set_page_config(page_title="Pet Companion Agent", page_icon="🐾", layout="wide")

st.title("🐾 Pet Companion Agent")
st.write("Onboard your cats and dogs and manage their daily care, mood, and activities.")

# Load profiles directly from JSON
with open(PROFILES_PATH, "r") as f:
    profiles = json.load(f)

# Breed-specific care data
pet_data = PetDataTool().run()

# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------
tab_dogs, tab_cats, tab_onboard = st.tabs(["🐶 Dogs", "🐱 Cats", "➕ Onboard New Pet"])

# ---------------------------------------------------------
# DOGS TAB
# ---------------------------------------------------------
with tab_dogs:
    st.header("🐶 Dog Profiles")

    dog_names = [p["name"] for p in profiles["dogs"]]
    selected_dog = st.selectbox("Select a Dog", dog_names, key="dog_select")
    dog_index = dog_names.index(selected_dog)

    agent = PetSessionAgent("dogs", dog_index)

    st.subheader("Profile")
    st.markdown(f"## 🐶 {agent.profile.name}")

    st.write(f"**Breed:** {agent.profile.breed}")
    st.write(f"**Age:** {agent.profile.age} years")
    st.write(f"**Weight:** {agent.profile.weight} lbs")
    st.write(f"**Notes:** {agent.profile.notes}")

    st.write(f"**Personality:** {agent.profile.personality}")
    st.write(f"**Favorite Toy:** {agent.profile.favorite_toy}")
    st.write(f"**Favorite Food:** {agent.profile.favorite_food}")
    st.write(f"**Medical Condition:** {agent.profile.medical_condition}")
    st.write(f"**Vaccination Date:** {agent.profile.vaccination_date}")
    st.write(f"**Last Vet Visit:** {agent.profile.last_vet_visit}")
    st.write(f"**Grooming Frequency:** {agent.profile.grooming_frequency}")
    st.write(f"**Feeding Schedule:** {agent.profile.feeding_schedule}")
    st.write(f"**Adoption Date:** {agent.profile.adoption_date}")

    st.subheader("Breed‑Specific Care")
    breed_data = pet_data["dogs"].get(agent.profile.breed, {})

    st.write("### Feeding Recommendations:")
    for step in breed_data.get("feeding", []):
        st.write(f"- {step}")

    st.write("### Grooming Recommendations:")
    for step in breed_data.get("grooming", []):
        st.write(f"- {step}")

    st.write("### Activity Recommendations:")
    for step in breed_data.get("activity", []):
        st.write(f"- {step}")

    st.subheader("Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Feed Dog", key="feed_dog"):
            agent.run_feeding()
            st.success(f"Feeding routine completed for {agent.profile.name}.")
    with col2:
        if st.button("Groom Dog", key="groom_dog"):
            agent.run_grooming()
            st.success(f"Grooming routine completed for {agent.profile.name}.")
    with col3:
        if st.button("Play with Dog", key="play_dog"):
            agent.run_play()
            st.success(f"Playtime completed for {agent.profile.name}.")

    st.subheader("Health Alerts")
    behavior = st.text_input(
        "Describe behavior for health check",
        key="dog_health_input"
    )
    if st.button("Check Dog Health", key="check_dog_health"):
        agent.check_mood(behavior)

# ---------------------------------------------------------
# CATS TAB
# ---------------------------------------------------------
with tab_cats:
    st.header("🐱 Cat Profiles")

    cat_names = [p["name"] for p in profiles["cats"]]
    selected_cat = st.selectbox("Select a Cat", cat_names, key="cat_select")
    cat_index = cat_names.index(selected_cat)

    agent = PetSessionAgent("cats", cat_index)

    st.subheader("Profile")
    st.markdown(f"## 🐱 {agent.profile.name}")

    st.write(f"**Breed:** {agent.profile.breed}")
    st.write(f"**Age:** {agent.profile.age} years")
    st.write(f"**Weight:** {agent.profile.weight} lbs")
    st.write(f"**Notes:** {agent.profile.notes}")

    st.write(f"**Personality:** {agent.profile.personality}")
    st.write(f"**Favorite Toy:** {agent.profile.favorite_toy}")
    st.write(f"**Favorite Food:** {agent.profile.favorite_food}")
    st.write(f"**Medical Condition:** {agent.profile.medical_condition}")
    st.write(f"**Vaccination Date:** {agent.profile.vaccination_date}")
    st.write(f"**Last Vet Visit:** {agent.profile.last_vet_visit}")
    st.write(f"**Grooming Frequency:** {agent.profile.grooming_frequency}")
    st.write(f"**Feeding Schedule:** {agent.profile.feeding_schedule}")
    st.write(f"**Adoption Date:** {agent.profile.adoption_date}")

    st.subheader("Breed‑Specific Care")
    breed_data = pet_data["cats"].get(agent.profile.breed, {})

    st.write("### Feeding Recommendations:")
    for step in breed_data.get("feeding", []):
        st.write(f"- {step}")

    st.write("### Grooming Recommendations:")
    for step in breed_data.get("grooming", []):
        st.write(f"- {step}")

    st.write("### Activity Recommendations:")
    for step in breed_data.get("activity", []):
        st.write(f"- {step}")

    st.subheader("Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Feed Cat", key="feed_cat"):
            agent.run_feeding()
            st.success(f"Feeding routine completed for {agent.profile.name}.")
    with col2:
        if st.button("Groom Cat", key="groom_cat"):
            agent.run_grooming()
            st.success(f"Grooming routine completed for {agent.profile.name}.")
    with col3:
        if st.button("Play with Cat", key="play_cat"):
            agent.run_play()
            st.success(f"Playtime completed for {agent.profile.name}.")

    st.subheader("Health Alerts")
    behavior = st.text_input(
        "Describe behavior for health check",
        key="cat_health_input"
    )
    if st.button("Check Cat Health", key="check_cat_health"):
        agent.check_mood(behavior)

# ---------------------------------------------------------
# ONBOARDING TAB
# ---------------------------------------------------------
with tab_onboard:
    st.header("➕ Onboard a New Pet")

    with st.form("new_pet_form"):
        species = st.selectbox("Species", ["dogs", "cats"], key="onboard_species")
        name = st.text_input("Name", key="onboard_name")
        breed = st.text_input("Breed", key="onboard_breed")
        age = st.number_input("Age (years)", min_value=0.0, step=0.5, key="onboard_age")
        weight = st.number_input("Weight (lbs)", min_value=0.0, step=0.5, key="onboard_weight")
        personality = st.text_input("Personality", key="onboard_personality")
        favorite_toy = st.text_input("Favorite Toy", key="onboard_toy")
        favorite_food = st.text_input("Favorite Food", key="onboard_food")
        medical_condition = st.text_input("Medical Condition", key="onboard_medical")
        notes = st.text_area("Notes", key="onboard_notes")
        submitted = st.form_submit_button("Add Pet", key="onboard_submit")

        if submitted:
            if not name or not breed:
                st.error("Name and breed are required.")
            else:
                profiles[species].append({
                    "name": name,
                    "breed": breed,
                    "age": age,
                    "weight": weight,
                    "notes": notes,
                    "personality": personality,
                    "favorite_toy": favorite_toy,
                    "favorite_food": favorite_food,
                    "medical_condition": medical_condition,
                    "vaccination_date": "2024-01-01",
                    "last_vet_visit": "2024-01-01",
                    "feeding_schedule": "twice daily",
                    "grooming_frequency": "monthly",
                    "adoption_date": "2024-01-01",
                    "photo_url": ""
                })
                save_profiles(profiles)
                st.success(f"{name} added to {species}! Refresh to see it.")
