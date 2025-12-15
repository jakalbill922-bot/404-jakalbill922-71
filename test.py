import requests

url = "http://localhost:10006/generate"

response = requests.post(url, files={"prompt_image_file": open("cr7.png", "rb")})

# save the response content to ply file
with open("response.ply", "wb") as f:
    f.write(response.content)