import json
import os

# Get lenguaje output file's directory
file_dir = ""
for i in os.listdir(os.getcwd()):
    if "output-" in i and ".json" in i:
        file_dir = os.getcwd() + "/" + i

# Open original file
file = open(file_dir, encoding='utf-8')

# Make a python dictionary and close original file
y = json.load(file)
file.close()

# Change items and equipment's pickup descriptions
for i in y['strings'].keys():
    if "ITEM_" in i and "_PICKUP" in i:
        x = str(i[:]).replace("_PICKUP", "_DESC")
        try:
            u = y['strings'][x]
        except KeyError:
            pass
        else:
            y['strings'][x.replace("_DESC", "_PICKUP")] = u

    if "EQUIPMENT_" in i and "_PICKUP" in i:
        x = str(i[:]).replace("_PICKUP", "_DESC")
        try:
            u = y['strings'][x]
        except KeyError:
            pass
        else:
            y['strings'][x.replace("_DESC", "_PICKUP")] = u

# Update original file
with open(file_dir, 'w', encoding='utf-8') as f:
    json.dump(y, f, ensure_ascii=False, indent=4)
