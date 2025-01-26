import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WeatherRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    date_range = db.Column(db.String(50), nullable=False)
    weather_data = db.Column(db.Text, nullable=False)

def get_weather_data(location):
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form.get('location')
    if location:
        # Redirect to OpenWeatherMap with the location as part of the query
        return redirect(f'https://openweathermap.org/find?q={location}')
    else:
        return jsonify({"error": "Invalid location."}), 400

@app.route('/create', methods=['POST'])
def create_record():
    location = request.json.get('location')
    date_range = request.json.get('date_range')
    weather_data = get_weather_data(location)

    if not weather_data:
        return jsonify({"error": "Invalid location or API error."}), 400

    record = WeatherRecord(location=location, date_range=date_range, weather_data=str(weather_data))
    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Record created successfully!"})

@app.route('/read', methods=['GET'])
def read_records():
    records = WeatherRecord.query.all()
    results = [
        {
            "id": record.id,
            "location": record.location,
            "date_range": record.date_range,
            "weather_data": record.weather_data
        } for record in records
    ]
    return jsonify(results)

@app.route('/update/<int:id>', methods=['PUT'])
def update_record(id):
    record = WeatherRecord.query.get_or_404(id)
    location = request.json.get('location')
    date_range = request.json.get('date_range')

    if location:
        weather_data = get_weather_data(location)
        if not weather_data:
            return jsonify({"error": "Invalid location or API error."}), 400
        record.location = location
        record.weather_data = str(weather_data)

    if date_range:
        record.date_range = date_range

    db.session.commit()
    return jsonify({"message": "Record updated successfully!"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = WeatherRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Record deleted successfully!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)

