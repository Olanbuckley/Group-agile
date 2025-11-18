import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from UserRequest import UserRequest
import random


cred = credentials.Certificate("agilegroup-971f8-firebase-adminsdk-fbsvc-a862def2da.json")


app = firebase_admin.initialize_app(cred)

db = firestore.client()

collection = db.collection("Requests")


def get_document(document_id) -> 'UserRequest':
    request = collection.document(document_id)
    doc = request.get()
    theUserRequest = UserRequest.from_snapshot(document_id, doc.to_dict())
    return theUserRequest


def get_location(document_id) -> str:
    return get_document(document_id).location

def get_llm_response(document_id) -> str:
    return get_document(document_id).llm_response

def get_location_latitude(document_id) -> str:
    return get_document(document_id).location_latitude

def get_location_longitude(document_id) -> str:
    return get_document(document_id).location_longitude

def get_weather_api_response(document_id) -> str:
    return get_document(document_id).weather_api_response

def get_generated_image(document_id) -> str:
    return get_document(document_id).generated_image

def createRequest(locationName):
    document_id = str(random.randrange(1, 1000000))
    location = {
        "location": locationName
    }
    collection.document(document_id).set(location)
    ###print(get_location(document_id))
    return document_id

def set_latitude(document_id, latitude) -> float:
    location_latitude = {
        "location_latitude": latitude
    }
    collection.document(document_id).set(location_latitude, merge=True)
    return latitude

def set_longitude(document_id, longitude) -> float:
    location_longitude = {
        "location_longitude": longitude
    }
    collection.document(document_id).set(location_longitude, merge=True)
    return longitude

def set_llm_response(document_id, response):
    llm_response = {
        "llm_response": response
    }
    collection.document(document_id).set(llm_response, merge=True)

def set_weather_api_response(document_id, response):
    weather_api_response = {
        "weather_api_response": response
    }
    collection.document(document_id).set(weather_api_response, merge=True)


def set_generated_image(document_id, response):
    generated_image = {
        "generated_image": response
    }
    collection.document(document_id).set(generated_image, merge=True)




###def test_case():
###    document_id = createRequest("cork")
###    set_llm_response(document_id, "RainCoat, Boats, Sheild")
###    print(document_id)
###    print(get_location(document_id))
###    print(get_llm_response(document_id))

