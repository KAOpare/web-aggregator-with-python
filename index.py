import requests

webpage_response = requests.get("https://en.wikipedia.org/wiki/Extract,_transform,_load")

webpage = webpage_response.content
print(webpage)