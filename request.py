import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'gre':337, 'toefl':118, 'rating':4, 'sop':4.5, 'lor':4.5, 'cgpa':9.65, 'research':1})

print(r.json())