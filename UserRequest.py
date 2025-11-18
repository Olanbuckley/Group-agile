from firebase_admin import firestore
from typing import Optional, Dict, Any

class UserRequest:

 
    


    def __init__(self, document_id: str, location: str, llm_response: str = "NA",  
                 location_latitude: str = "NA", location_longitude: str = "NA", 
                 weather_api_response: str = "NA", generated_image: str = "NA"):
        self.document_id = document_id
        self.llm_response = llm_response
        self.location = location
        self.location_latitude = location_latitude
        self.location_longitude = location_longitude
        self.weather_api_response = weather_api_response
        self.generated_image = generated_image

    
    @staticmethod
    
    def from_snapshot(document_id, source) -> 'UserRequest':
        
        
        if not source:
            return None
        try:
            return UserRequest(
                document_id=document_id,
                location= source['location'],
                llm_response=source.get('llm_response', 'NA'),
                location_latitude= source.get('location_latitude', 'NA'),
                location_longitude= source.get('location_longitude', 'NA'),
                weather_api_response= source.get('weather_api_response', 'NA'),
                generated_image= source.get('generated_image', 'NA')
            )
            
        except Exception as e:
            print(e)
    
    def to_dic(self) -> dict:
        return{
            'document_id': self.document_id,
            'llm_response': self.llm_response,
            'location': self.location,
            'location_latitude': self.location_latitude,
            'location_longitude': self.location_longitude,
            'weather_api_response': self.weather_api_response,
            'generated_image': self.generated_image
        }
    
    def __repr__(self):
        return(f"Request(ID='{self.document_id}')",
               f"Location='{self.location}'",
               f"Location_latitude='{self.location_latitude}'",
               f"Location_longitude='{self.location_longitude}'",
               f"weather_api_response='{self.weather_api_response}'",
               f"generated_image_url='{self.generated_image}'")
    
    
