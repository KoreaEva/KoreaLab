import requests

# Subscription key and endpoint
subscription_key = "3Yn3aK27bajcPjdcLlcNWPlVnlofzgk7iaW2KavQ3vbZB5q3kLQuJQQJ99BFACYeBjFXJ3w3AAAFACOGcULc"
endpoint = "https://labuser1-cv-0001.cognitiveservices.azure.com/"

def analyze_image(image_path):
    analyze_url = endpoint + "vision/v3.2/analyze"
    params = {"visualFeatures": "Categories,Description,Color"}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key,
               "Content-Type": "application/octet-stream"}
    
    # Open the image file in binary mode
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except Exception as e:
        print(f"Error reading image file: {e}")
        return None
    
    # Make the API request    
    response = requests.post(analyze_url, params=params, headers=headers, data=image_data)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
    # Parse the JSON response
    return response.json()

def main():
    image_path = input("Enter the path to the image: ")

    result = analyze_image(image_path)
    if result:
        print("Analysis Result:")
        print(result)
        # print(f"Categories: {result.get('categories', [])}")
        # print(f"Description: {result.get('description', {}).get('captions', [])}")
        # print(f"Color: {result.get('color', {})}")

if __name__ == "__main__":
    main()