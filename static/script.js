document.getElementById('predictForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const district = document.getElementById('district').value;
    const soil_type = document.getElementById('soil_type').value;
    const season = document.getElementById('season').value;
    const rainfall = document.getElementById('rainfall').value;

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ district, soil_type, season, rainfall })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('result').innerHTML = `
                <h3>Predicted Crop: ${data.predicted_crop}</h3>
                <p>Prices: 2021: ${data.prices['2021']}, 2022: ${data.prices['2022']}, 2023: ${data.prices['2023']}</p>
            `;
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = `Fetch error: ${error}`;
    });
});

document.getElementById('chatForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const message = document.getElementById('chatMessage').value;

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chatResult').innerText = data.response;
    })
    .catch(error => {
        document.getElementById('chatResult').innerText = `Fetch error: ${error}`;
    });
});
