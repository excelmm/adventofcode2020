import re

with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()
    
database = {}

database["departure_location"] = []
database["departure_station"] = []
database["departure_platform"] = []
database["departure_track"] = []
database["departure_date"] = []
database["departure_time"] = []
database["arrival_location"] = []
database["arrival_station"] = []
database["arrival_platform"] = []
database["arrival_track"] = []
database["class_data"] = []
database["duration"] = []
database["price"] = []
database["route"] = []
database["row"] = []
database["seat"] = []
database["train"] = []
database["type_data"] = []
database["wagon"] = []
database["zone"] = []

for i, key in enumerate(database):
    pattern = re.compile(r"(\d+)-(\d+) or (\d+)-(\d+)")
    matches = pattern.search(rawinput[i])
    low1 = int(matches.group(1))
    high1 = int(matches.group(2))
    low2 = int(matches.group(3))
    high2 = int(matches.group(4))
    for i in range(low1, high1 + 1):
        database[key].append(i)
    for i in range(low2, high2 + 1):
        database[key].append(i)
    # print(database)

    if key == "zone":
        break

tickets = []
for i in range(25, 260):
    line = rawinput[i].split(",")
    tickets.append(line)

count = 0
databasekeys = list(database)
for i in tickets:
    for index, j in enumerate(i):
        found = 0
        for k in database.values():
            if int(j) in k:
                found = 1
                break
        if found == 0:
            count += (int(j))

print(count)