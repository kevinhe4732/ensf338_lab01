import json
import os
import time

def update_size_recursively(data):
    """
    Recursively update all 'size' values to 42 in nested dictionaries
    """
    if isinstance(data, dict):
        for key, value in list(data.items()):
            if key == 'size':
                data[key] = 42
            elif isinstance(value, (dict, list)):
                update_size_recursively(value)
    elif isinstance(data, list):
        for item in data:
            update_size_recursively(item)

def process_json_file(input_filename, output_filename):
    try:
        # Load the JSON file
        with open(input_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Time the modification of size values
        start_time = time.time()
        update_size_recursively(data)
        total_time = time.time() - start_time

        # Reverse the order if it's a list
        if isinstance(data, list):
            data = list(reversed(data))

        # Write modified data to output file
        with open(output_filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        print(f"Successfully processed JSON data and wrote to {output_filename}")
        print(f"Average time to modify size values: {total_time / 10:.5f} seconds")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input file")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "large-file.json")
    output_file = os.path.join(script_dir, "output.2.3.json")

    # Run the code 10 times and calculate the average time
    total_time = 0
    for _ in range(10):
        process_json_file(input_file, output_file)
    print(f"Average time to modify size values: {total_time / 10:.5f} seconds")