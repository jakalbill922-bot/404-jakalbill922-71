import requests

url = "http://localhost:10006/generate"

response = requests.post(url, files={"prompt_image_file": open("cr7.png", "rb")})

print(response.json())