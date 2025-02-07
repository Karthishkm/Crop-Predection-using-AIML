from flask import Flask, request, jsonify, render_template
import pandas as pd
import random
import aiml
import os
import joblib

app = Flask(__name__)

# Load the crop dataset
df = pd.read_csv('crop_data.csv')

# Load the trained model
model = joblib.load('models/crop_prediction_model.pkl')

# Set up AIML kernel
kernel = aiml.Kernel()
aiml_directory = os.path.join(os.path.dirname(__file__), 'aiml')
for filename in os.listdir(aiml_directory):
    if filename.endswith(".aiml"):
        kernel.learn(os.path.join(aiml_directory, filename))
kernel.respond("LOAD AIML B")

crop_data = {
    "Banana": {
        "prices": {"2021": 1200, "2022": 1400, "2023": 1600},
        "soil_type": "Loamy",
        "irrigation": "High",
        "rainfall": 1200,
        "season": "Kharif",
        "image_url": "/static/images/banana.jpg"
    },
    "Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },
    # Add more crops here...
    "Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },"Wheat": {
        "prices": {"2021": 1000, "2022": 1100, "2023": 1200},
        "soil_type": "Clay",
        "irrigation": "Medium",
        "rainfall": 500,
        "season": "Rabi",
        "image_url": "/static/images/wheat.jpg"
    },
}

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result')
def result():
    predicted_crop = request.args.get('predicted_crop')
    prices = eval(request.args.get('prices'))
    soil_type = request.args.get('soil_type')
    irrigation = request.args.get('irrigation')
    rainfall = request.args.get('rainfall')
    image_url = request.args.get('image_url')
    result = {
        'predicted_crop': predicted_crop,
        'prices': prices,
        'soil_type': soil_type,
        'irrigation': irrigation,
        'rainfall': rainfall,
        'image_url': image_url
    }
    return render_template('prediction_result.html', result=result)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        district = data['district']
        soil_type = data['soil_type']
        season = data['season']
        rainfall = data['rainfall']

        # Placeholder for the real prediction logic
        random_crop = df.sample().iloc[0]
        predicted_crop = random_crop['crop']
        prices = {
            '2021': int(random_crop['price_2021']),
            '2022': int(random_crop['price_2022']),
            '2023': int(random_crop['price_2023'])
        }
        result = {
            'predicted_crop': predicted_crop,
            'prices': prices,
            'soil_type': soil_type,
            'irrigation': 'Moderate',  # Example value
            'rainfall': rainfall,
            'image_url': '/static/images/crops/{}.jpg'.format(predicted_crop.lower())
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data['message']
        response = kernel.respond(message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
