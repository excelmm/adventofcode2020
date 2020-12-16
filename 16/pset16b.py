import re
import copy

with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()
    
# Initialise dictionary containing allowed ranges for each field
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

# Keep a list of all other people's tickets
tickets = []
for i in range(25, 260):
    line = rawinput[i].split(",")
    tickets.append(line)

# Remove completely invalid tickets
count = 0
databasekeys = list(database)
ticketstoremove = []
for i in tickets:
    for index, j in enumerate(i):
        found = 0
        for k in database.values():
            if int(j) in k:
                found = 1
                break
        if found == 0:
            if i not in ticketstoremove:
                ticketstoremove.append(i)

tickets = [item for item in tickets if item not in ticketstoremove]

# Determine which are impossible field types for each field
impossible_fields = []
for i in databasekeys:
    impossible_fields.append(set())

for i in tickets:
    for index, j in enumerate(i):
        for k in databasekeys:
            if int(j) not in database[k]:
                impossible_fields[index].add(k)

# From the impossible fields, deduce the possible fields
possible_fields = []
for i in range(20):
    possible_fields.append([item for item in databasekeys if item not in impossible_fields[i]])

# Get the 'key frequency': In how many possible fields a field type can be 
keyfrequency = {}

for i in databasekeys:
    count = 0
    for j in possible_fields:
        if i in j:
            count += 1
    keyfrequency[i] = count

# Sort the keyfrquency dict so we can work up from the least to get the final answer of which
# field belongs in which index
keyfrequency = dict(sorted(keyfrequency.items(), key=lambda item: item[1]))
final = []
found = []

for i in keyfrequency:
    for index, j in enumerate(possible_fields):
        if i in j:
            if index in found:
                continue
            found.append(index)
            final.append((i, index))
            break

# Get our ticket number
myticket = rawinput[22].split(",")

# Get which indexes the departure fields are
departurefields = []
for i in final:
    if 'departure' in i[0]:
        departurefields.append(i[1])

# Obtain the final answer
answer = 1
for index, i in enumerate(myticket):
    if index in departurefields:
        answer *= int(i)

print(answer)