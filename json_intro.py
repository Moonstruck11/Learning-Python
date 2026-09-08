import json
hike1 = {"name": "Tiger Leaping Gorge",
         "location": "China",
         "distance_km": 22,
         "elevation_gain": 1200,
         "days": 2,
         "difficulty": "moderate"}
with open("hike1.json", "w") as file:
    json.dump(hike1, file)
with open("hike1.json", "r") as file:
    hike1_info = json.load(file)
print(hike1_info)









