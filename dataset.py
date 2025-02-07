import pandas as pd
import random

crops = [
    "Rice", "Wheat", "Maize", "Barley", "Sugarcane", "Pulses",
    "Cotton", "Sorghum", "Groundnut", "Millet", "Banana", "Potato",
    "Tomato", "Onion", "Soybean", "Sunflower", "Peanut", "Lentil",
    "Mustard", "Chickpea"
]

districts = ["Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum", "Gulbarga"]
soil_types = ["Loamy", "Clayey", "Sandy"]
seasons = ["Kharif", "Rabi", "Zaid"]

data = []

for district in districts:
    for crop in crops:
        soil_type = random.choice(soil_types)
        season = random.choice(seasons)
        rainfall = random.randint(200, 1200)
        price_2021 = random.randint(1000, 2000)
        price_2022 = random.randint(1000, 2000)
        price_2023 = random.randint(1000, 2000)
        data.append([district, soil_type, season, rainfall, price_2021, price_2022, price_2023, crop])

df = pd.DataFrame(data, columns=['district', 'soil_type', 'season', 'rainfall', 'price_2021', 'price_2022', 'price_2023', 'crop'])
df.to_csv('crop_data1.csv', index=False)
