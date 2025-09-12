import os
import requests
from urllib.parse import urlparse

def fetch_image():
    print("🌍 Ubuntu Image Fetcher")
    print('"I am because we are" – Let us fetch and share images with respect.\n')

    # Prompt user for the image URL
    url = input("Enter the URL of the image: ").strip()

    # Create the directory if it does not exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Request the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Extract filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename is found, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        file_path = os.path.join(folder_name, filename)

        # Save the image in binary mode
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"✅ Image successfully fetched and saved as: {file_path}")

    except requests.exceptions.MissingSchema:
        print("❌ Error: The URL seems invalid. Please provide a valid URL.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not connect to the server.")
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The request took too long.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
