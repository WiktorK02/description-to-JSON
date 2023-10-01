import json
import re

description = """
kitchen: 2microwave,  2lights 
Livingroom: sssslight2, 2thermostatkkkkk
bedroom: elaseeethermostat light
LIBRARY: 5lights and microwave on
Garage: 1light
"""
categories = {}
def add_to_category(category, device, state, custom_name):
    if category not in categories:
        categories[category] = []
    device_info = {
        "name": custom_name,
        "type": device,
        "state": state
    }
    categories[category].append(device_info)
device_custom_names = {}
for line in description.strip().split("\n"):
    parts = line.strip().split(":")
    if len(parts) == 2:
        category = parts[0].strip().lower()
        devices = parts[1].strip().split()
        for device in devices:
            for keyword in ["light", "thermostat", "microwave"]:
                if keyword in device:
                    state = "on" if "on" in device else "off"
                    room = category.capitalize()  
                    device_name_parts = re.split(r'(\d+)', device)
                    num = [part for part in device_name_parts if part.isdigit()]
                    count = int(num[0]) if num else 1 
                    if (category, keyword) not in device_custom_names:
                        device_custom_names[(category, keyword)] = []

                    for _ in range(count):
                        custom_name = input(f"Enter a custom name for the {keyword} in the {room}: ")
                        device_custom_names[(category, keyword)].append(custom_name)
                        add_to_category(category, keyword, state, custom_name)

json_output = json.dumps(categories, indent=4)
print(json_output)
try:
    with open("smart_home_categories.json", "w") as json_file:
        json.dump(categories, json_file, indent=4)
except Exception as e:
    print("Error saving JSON data:", str(e))
