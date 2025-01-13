import requests
import random

# Function to download the image and save it with a unique name
def download_image(image_url, model, image_num):
    response = requests.get(image_url)
    filename = f'{model}-image-{image_num}.jpg'  # Unique filename for each image
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'Download Completed: {filename}')

# User input for prompt
promptz = input("Enter your prompt: ")

# Image models to use
models = ['flux', 'flux-realism', 'flux-cablyai', 'flux-anime', 'flux-3d', 'any-dark', 'flux-pro', 'turbo']

# Image dimensions
width = 768
height = 768

# Generate images for each model (2 images per model with random seeds)
for model in models:
    for i in range(1, 5):  # Generate 2 images per model
        seed = random.randint(1, 100000)  # Use a random seed for each image
        image_url = f"https://pollinations.ai/p/{promptz}?width={width}&height={height}&seed={seed}&model={model}"
        download_image(image_url, model, i)  # Download the image with a unique filename
