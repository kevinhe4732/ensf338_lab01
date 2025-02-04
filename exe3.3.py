import json
import os
import time
import timeit
import matplotlib.pyplot as plt
import numpy as np

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
    

def create_subset_json(full_data, size, subset_filename):
    """
    Writes the first `size` records of `full_data` (if it's a list) to subset_filename.
    """
    if isinstance(full_data, list):
        subset_data = full_data[:size]
    else:
        # If your JSON isn't a list, adjust how you create the subset here.
        subset_data = full_data

    with open(subset_filename, 'w', encoding='utf-8') as f:
        json.dump(subset_data, f)

# 1) Load all data once (so we can create subsets without altering the original code above)
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        all_data = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found. Cannot proceed with Part 3.2.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in input file. Cannot proceed with Part 3.2.")
    exit(1)

# 2) Define the sizes and where we'll store the average times
subset_sizes = [1000, 2000, 5000, 10000]
avg_times = []

# 3) For each subset size, create a smaller JSON, call process_json_file() 100 times, measure average
for size in subset_sizes:
    # Create a subset JSON file
    subset_file = os.path.join(script_dir, f"subset_{size}.json")
    create_subset_json(all_data, size, subset_file)

    # Run 100 trials
    times_for_size = []
    for _ in range(100):
        start_t = time.time()
        process_json_file(subset_file, output_file)
        run_t = time.time() - start_t
        times_for_size.append(run_t)

    # Compute average
    avg_t = sum(times_for_size) / len(times_for_size)
    avg_times.append(avg_t)
    print(f"\n[Part 3.2] For N={size}, average processing time over 100 runs: {avg_t:.5f} seconds\n")

# 4) Perform a simple linear regression using np.polyfit
slope, intercept = np.polyfit(subset_sizes, avg_times, 1)

# 5) Plot the data and the best-fit line
plt.figure(figsize=(8,6))
plt.scatter(subset_sizes, avg_times, color='blue', label='Data Points')

# Construct line values
x_vals = np.array(subset_sizes)
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, 'r-', label=f'Best Fit: time = {slope:.2e} * N + {intercept:.2e}')

plt.title("Number of Records vs. Average Processing Time")
plt.xlabel("Number of Records")
plt.ylabel("Time (seconds)")
plt.legend()
plt.tight_layout()

# 6) Save the plot
plot_file = os.path.join(script_dir, "output.3.2.png")
plt.savefig(plot_file, dpi=300)
plt.show()

print(f"[Part 3.2] Linear model: time = {slope:.2e} * N + {intercept:.2e}")
print(f"[Part 3.2] Plot saved to: {plot_file}")


if __name__ == "__main__":
    # 1) Create or reuse a 1000-record subset file (similar to how you did in 3.2).
    #    If you already created `subset_1000.json`, just reuse it. 
    #    Otherwise, create it now from the first 1000 records:
    
    subset_1000_file = os.path.join(script_dir, "subset_1000.json")
    
    # If you need to create it, do it here:
    # -------------------------------------------------------------------------
    #   with open(input_file, 'r', encoding='utf-8') as f:
    #       all_data = json.load(f)
    #   if isinstance(all_data, list):
    #       subset_data_1000 = all_data[:1000]
    #   else:
    #       subset_data_1000 = all_data  # Adjust if JSON is not a list
    #   with open(subset_1000_file, 'w', encoding='utf-8') as f:
    #       json.dump(subset_data_1000, f, indent=4)
    # -------------------------------------------------------------------------
    # (If your 3.2 code already created subset_1000.json, you can skip the above.)

    # 2) Use timeit.repeat to measure the processing time 1000 times
    #    Each repeat calls process_json_file(subset_1000_file, output_file) once.
    #    The resulting list will hold 1000 measured times.
    times = timeit.repeat(
        stmt="process_json_file(subset_1000_file, output_file)",
        setup="from __main__ import process_json_file, subset_1000_file, output_file",
        repeat=1000,  # how many times "stmt" is repeated
        number=1       # how many times to run 'stmt' per repeat
    )

    # 3) Plot the histogram of these measured times
    plt.figure(figsize=(8, 6))
    plt.hist(times, bins=30, color='skyblue', edgecolor='black')
    plt.title("Distribution of Processing Times for 1000 Records (1000 Repeats)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")

    # 4) Save the figure
    histogram_file = os.path.join(script_dir, "output.3.3.png")
    plt.savefig(histogram_file, dpi=300)
    plt.show()

    print(f"[Part 3.3] Histogram saved to: {histogram_file}")
    print("[Part 3.3] Done.")
