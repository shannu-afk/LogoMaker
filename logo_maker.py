import os
import requests
from PIL import Image
from io import BytesIO

# Unsplash Access Key (replace with your actual key)
ACCESS_KEY = 'API key' # Replace this with your actual access key

# Function to fetch image URL based on a prompt
def fetch_image(prompt):
    # Unsplash API URL
    url = f'https://api.unsplash.com/search/photos?query={prompt}&client_id={ACCESS_KEY}'

    # Make the API request
    response = requests.get(url)

    # Check if the request is successful
    if response.status_code == 200:
        data = response.json()

        # If images are found
        if data['total'] > 0:
            # Fetch the first image from the search results
            image_url = data['results'][0]['urls']['regular']
            print(f"Image URL: {image_url}")
            return image_url
        else:
            print("No results found for the prompt.")
            return None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to download and save the image
def save_image(image_url, folder_name="logos", file_name="logo_image"):
    try:
        # Create folder if not exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Get the image from the URL
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))

        # Define the image path
        image_path = os.path.join(folder_name, f"{file_name}.jpg")

        # Save the image
        image.save(image_path)
        print(f"Image saved at {image_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

# Example usage
if __name__ == "__main__":
    prompt = input("Enter logo prompt (e.g., government logo, nature, etc.): ")
    image_url = fetch_image(prompt)

    if image_url:
        save_image(image_url)
