import pandas as pd
import numpy as np

# Generate synthetic crop data
np.random.seed(0)
districts = ['Bangalore', 'Mysore', 'Mangalore', 'Hubli', 'Belgaum', 'Gulbarga']
soil_types = ['Loamy', 'Sandy', 'Clay', 'Silt']
seasons = ['Kharif', 'Rabi', 'Zaid']
crops = ['Rice', 'Wheat', 'Maize', 'Sorghum', 'Pulses', 'Cotton', 'Sugarcane', 'Barley', 'Millet', 'Soybean']

data = []

for district in districts:
    for soil in soil_types:
        for season in seasons:
            for crop in crops:
                rainfall = np.random.randint(200, 1500)
                price_2021 = np.random.randint(1000, 5000)
                price_2022 = np.random.randint(1000, 5000)
                price_2023 = np.random.randint(1000, 5000)
                data.append([district, soil, season, rainfall, crop, price_2021, price_2022, price_2023])

df = pd.DataFrame(data, columns=['district', 'soil_type', 'season', 'rainfall', 'crop', 'price_2021', 'price_2022', 'price_2023'])
df.to_csv('crop_data.csv', index=False)
print("Dataset created successfully!")
