# Crop Prediction and Information System

## Overview
This project is a **Crop Prediction and Information System** designed to help farmers determine the best crops to cultivate based on various factors such as **rainfall, soil type, season, and district**. The system also provides AI-based responses to queries related to crops and irrigation.

## Features
- **Crop Prediction**: Suggests the best crops to grow for the next three months.
- **Weather & Price Analysis**: Uses historical price data (last 3 years) and current weather conditions.
- **AI Chatbot**: Provides information about irrigation, soil types, and crop recommendations.
- **User-Friendly Web Interface**: Designed with **HTML, CSS, and JavaScript**.
- **Flask Backend**: Manages API requests and prediction models.
- **Machine Learning Model**: Predicts suitable crops based on user inputs.
- **No External APIs**: Works independently with a predefined dataset.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: CSV/Dataset files for training
- **ML Model**: Scikit-learn, Pandas, NumPy
- **Chatbot**: python-aiml (AI for answering crop-related queries)

## Installation
### Prerequisites
- Python 3.8+
- Flask
- Pandas, NumPy, Scikit-learn
- AIML library for chatbot

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Karthishkm/Crop-Predection-using-AIML.git
   cd crop-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## Dataset
The dataset contains columns:
- `district`, `soil_type`, `season`, `rainfall`, `price_2021`, `price_2022`, `price_2023`, `crop`
- Includes data for Bangalore, Mysore, Mangalore, Hubli, Belgaum, Gulbarga, etc.

## Usage
1. Enter **district, soil type, season, and rainfall** to get crop predictions.
2. Use the chatbot to ask **crop-related questions**.
3. View **historical crop price trends**.

## Future Enhancements
- **More districts & crop data**
- **Mobile-friendly UI**
- **Advanced AI chatbot using Rasa**
- **Better ML model for prediction**

## Contributing
Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries, contact [your email or GitHub profile link].

