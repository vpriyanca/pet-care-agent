class PetProfile:
    def __init__(
        self,
        name,
        breed,
        age,
        weight,
        notes="",
        personality="",
        favorite_toy="",
        favorite_food="",
        medical_condition="",
        vaccination_date="",
        last_vet_visit="",
        grooming_frequency="",
        feeding_schedule="",
        adoption_date="",
        photo_url=""
    ):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        self.notes = notes
        self.personality = personality
        self.favorite_toy = favorite_toy
        self.favorite_food = favorite_food
        self.medical_condition = medical_condition
        self.vaccination_date = vaccination_date
        self.last_vet_visit = last_vet_visit
        self.grooming_frequency = grooming_frequency
        self.feeding_schedule = feeding_schedule
        self.adoption_date = adoption_date
        self.photo_url = photo_url

    def short_description(self):
        return f"{self.name} ({self.breed}, {self.age} yrs, {self.weight} lbs)"
