import os
import json

# Create a folder named "Final Items" if it doesn't exist
folder_name = "Final Items"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Read the original JSON data from output.json
with open("output.json", "r") as file:
    original_json_list = json.load(file)

# Helper function to determine the type of the value
def get_attribute_value(value):
    if value is None:
        return "Non Specified"
    elif isinstance(value, (int, float)):
        return value
    else:
        return str(value)

# Iterate over each item in the original JSON list
for index, original_json in enumerate(original_json_list):
    # Rename "ReferenceNo." to "ReferenceNo" if "ReferenceNo." exists
    if "ReferenceNo." in original_json:
        original_json["ReferenceNo"] = original_json.pop("ReferenceNo.")
        
    # Transform the current item to the desired format
    transformed_item = {}
    for key, value in original_json.items():
        transformed_item[key] = get_attribute_value(value)

    # Create a sanitized filename based on the item's ReferenceNo
    reference_no = original_json['ReferenceNo'].replace('/', '_').replace('-', '_')  # Replace / and - with _
    filename = os.path.join(folder_name, f"item_{reference_no}.json")

    # Write the transformed JSON to a new file
    with open(filename, "w") as file:
        json.dump(transformed_item, file, indent=4)






