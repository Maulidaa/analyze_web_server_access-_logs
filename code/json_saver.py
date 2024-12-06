import json

def save_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data has been saved to {file_name}")
