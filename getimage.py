import os
from openai import OpenAI

client = OpenAI()

try:
    print("Generating your image... 🎨")

    # Make the API call to generate an image
    response = client.images.generate(
      model="dall-e-3",
      prompt="a cartoon rain boots",
      size="1024x1024", 
      quality="standard", 
      n=1, 
    )

    # Get the URL of the generated image
    image_url = response.data[0].url

    print(f"Success! ✨ Your image is ready.")
    print(f"Image URL: {image_url}")
    print("You can open this URL in your browser to view and download the image.")

except Exception as e:
    print(f"An error occurred: {e}")
