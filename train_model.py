import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
df = pd.read_csv('crop_data.csv')

# Convert categorical variables to dummy/indicator variables
df = pd.get_dummies(df, columns=['district', 'soil_type', 'season'])

# Split data into features and target variable
X = df.drop('crop', axis=1)
y = df['crop']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'models/crop_prediction_model.pkl')
print("Model trained and saved successfully!")
