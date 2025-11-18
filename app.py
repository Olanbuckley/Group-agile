from flask import Flask, jsonify, request
import FireStore
import WeatherRetrieve
import GenerateResponse

app = Flask(__name__)

def get_location_details(document_id, location):
    location_data = WeatherRetrieve.geocode_location(location)
    latitude = FireStore.set_latitude(document_id, location_data['lat'])
    longitude = FireStore.set_longitude(document_id, location_data['lon'])
    weather_data = WeatherRetrieve.fetch_forecast(latitude, longitude)
    FireStore.set_weather_api_response(document_id, str(weather_data))
    llm_response = GenerateResponse.generate_response(weather_data)
    FireStore.set_llm_response(document_id, llm_response)
    generated_image = GenerateResponse.generate_image(llm_response)
    FireStore.set_generated_image(document_id, generated_image)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/request/<location>')
def make_request(location):
    document_id = FireStore.createRequest(location)
    get_location_details(document_id, location)

    return document_id

@app.route('/image/<document_id>')
def get_image(document_id):
    url = FireStore.get_generated_image(document_id)
    return url

@app.route('/response/<document_id>')
def get_response(document_id):
    text = FireStore.get_llm_response(document_id)
    return text

if __name__ == '__main__':
    app.run()