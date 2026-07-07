import json
import random
from datetime import datetime, timedelta

DOG_BREEDS = [
    "Golden Retriever", "Labrador", "German Shepherd", "Poodle",
    "Bulldog", "Beagle", "Rottweiler", "Boxer", "Husky"
]

CAT_BREEDS = [
    "Domestic Shorthair", "Siamese", "Persian", "Maine Coon",
    "Bengal", "Sphynx", "Ragdoll", "British Shorthair"
]

PERSONALITIES = [
    "playful", "shy", "energetic", "lazy", "curious",
    "affectionate", "independent", "protective"
]

TOYS = ["ball", "rope", "laser pointer", "feather wand", "squeaky toy", "plush mouse"]
FOODS = ["chicken", "salmon", "beef", "tuna", "turkey", "lamb"]

MEDICAL_CONDITIONS = ["none", "allergies", "arthritis", "anxiety", "skin sensitivity"]

# Cute random names
PET_NAMES = [
    "Mimi", "Gogo", "Lulu", "Koko", "Toto", "Nini", "Bibi", "Zuzu", "Pipi", "Riri",
    "Momo", "Fifi", "Dodo", "Soso", "Lala", "Coco", "Pupu", "Gigi", "Titi", "Kiki"
]

def random_date(start_year=2015):
    start = datetime(start_year, 1, 1)
    end = datetime.now()
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).strftime("%Y-%m-%d")

def generate_pet(species):
    breed = random.choice(DOG_BREEDS if species == "dogs" else CAT_BREEDS)
    age = round(random.uniform(0.5, 15), 1)
    weight = round(random.uniform(5, 120), 1) if species == "dogs" else round(random.uniform(4, 20), 1)

    return {
        "name": random.choice(PET_NAMES),
        "breed": breed,
        "age": age,
        "weight": weight,
        "notes": random.choice(["friendly", "needs training", "calm", "nervous"]),
        "personality": random.choice(PERSONALITIES),
        "favorite_toy": random.choice(TOYS),
        "favorite_food": random.choice(FOODS),
        "medical_condition": random.choice(MEDICAL_CONDITIONS),
        "vaccination_date": random_date(),
        "last_vet_visit": random_date(),
        "feeding_schedule": random.choice(["morning", "evening", "twice daily"]),
        "grooming_frequency": random.choice(["weekly", "monthly", "rare"]),
        "adoption_date": random_date(),

        # Removed picture/avatar completely
        "photo_url": ""
    }

def generate_dataset(count=500):
    dogs = [generate_pet("dogs") for _ in range(count // 2)]
    cats = [generate_pet("cats") for _ in range(count // 2)]
    return {"dogs": dogs, "cats": cats}

if __name__ == "__main__":
    data = generate_dataset()
    with open("data/pet_profiles.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Generated 500 pet profiles!")
