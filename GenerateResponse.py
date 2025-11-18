from openai import OpenAI

client = OpenAI()


def generate_response(weather_data) -> str:
    startPrompt = "Based on provided weather data can you provide me with clothing items that would be suitable for the first days weather conditions. I want you to provide me a response with 3-5 bullet points, each bullet point should be a gender neutral option that suits the weather conditions. Those bullet points are the only response I want. The weather data: "
    finalPrompt = startPrompt + str(weather_data)
    response = client.responses.create(
    model="gpt-4",
    input=finalPrompt
    )
    return response.output_text

def generate_image(recomendation) -> str:
    
    startPrompt = "based on a description clothing items, can you generate an image of a clothing store mannequin wearing the recommend clothing items, in a cartoon style. The description: "
    finalPrompt = startPrompt + (recomendation)
    
    try:

    # Make the API call to generate an image
        response = client.images.generate(
            model="dall-e-3",
            prompt=finalPrompt,
            size="1024x1024", 
            quality="standard", 
            n=1, 
        )

    
        image_url = response.data[0].url
        return image_url



    

    except Exception as e:
        print(f"An error occurred: {e}")
