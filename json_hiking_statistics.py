import json
hikes = [{"name": "tiger leaping gorge",
         "location": "china",
         "distance_km": 22,
         "elevation_gain": 1200,
         "days": 2,
         "difficulty": "moderate"},
         {"name": "shika snow mountain",
          "location": "china",
          "distance_km": 8,
          "elevation_gain": 1200,
          "days": 1,
          "difficulty": "advanced"},
         {"name": "dragon's back",
          "location": "hong kong",
          "distance_km": 8,
          "elevation_gain": 300,
          "days": 1,
          "difficulty": "easy"}]
with open("hikes.json", "w") as file:
    json.dump(hikes, file)
with open("hikes.json", "r") as file:
    hikes = json.load(file)
print("===== HIKE STATISTICS =====")
number_of_hikes = 0
for hike in hikes:
    number_of_hikes += 1
total_distance = 0
for hike in hikes:
    total_distance += hike["distance_km"]
average_distance = total_distance / number_of_hikes
longest_so_far = hikes[0]["distance_km"]
longest_hike = hikes[0]["name"]
for hike in hikes:
    if hike["distance_km"] > longest_so_far:
        longest_so_far = hike["distance_km"]
        longest_hike = hike["name"]
print("Number of hikes: ", number_of_hikes)
print("Total distance: ", total_distance)
print("Average distance: ", average_distance)
print("Longest hike: ", longest_hike)












