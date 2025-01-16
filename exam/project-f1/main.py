# Make sure to run this script from the project-f1 directory because it uses relative paths to access JSON files.
# Make sure you are on /project-f1 directory before running this script.

import json
import matplotlib.pyplot as plt
from tabulate import tabulate

# Function to load driver details from f1_drivers.json
def load_driver_details(file_name="f1_drivers.json"):
    try:
        with open(file_name, 'r') as file:
            drivers = json.load(file)
        return drivers
    except FileNotFoundError:
        print(f"Error: '{file_name}' not found. Driver details will not be displayed.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in '{file_name}'.")
        return {}

# Function to parse lap times from a JSON file
def parse_lap_times(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        
        grand_prix_location = data.get("grand_prix_location", "Unknown Location")
        lap_times = data.get("lap_times", {})
        
        return grand_prix_location, lap_times
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return "Unknown Location", {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in '{file_name}'.")
        return "Unknown Location", {}

# Function to analyze lap times
def analyze_lap_times(lap_times):
    fastest_time_overall = float('inf')
    fastest_driver_overall = None
    driver_metrics = []

    for driver, times in lap_times.items():
        fastest_time = min(times)
        average_time = sum(times) / len(times)

        driver_metrics.append({
            "driver": driver,
            "fastest_time": fastest_time,
            "average_time": average_time
        })

        if fastest_time < fastest_time_overall:
            fastest_time_overall = fastest_time
            fastest_driver_overall = driver

    return fastest_driver_overall, fastest_time_overall, driver_metrics

# Function to save results to a JSON log
def save_to_json_log(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, log_file):
    log_data = {
        "grand_prix_location": grand_prix_location,
        "fastest_driver": fastest_driver,
        "fastest_time": fastest_time,
        "driver_details": []
    }

    for d in driver_metrics:
        details = driver_details.get(d["driver"], {"name": "Unknown", "team": "Unknown"})
        log_data["driver_details"].append({
            "code": d["driver"],
            "name": details["name"],
            "team": details["team"],
            "fastest_time": d["fastest_time"],
            "average_time": d["average_time"]
        })

    with open(log_file, "w") as log_file:
        json.dump(log_data, log_file, indent=4)

    print(f"Results have been saved to '{log_file.name}'.")

# Function to display results
def display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details):
    print(f"Grand Prix Location: {grand_prix_location}\n")
    print(f"Fastest Driver Overall: {fastest_driver} with a time of {fastest_time:.3f} seconds\n")

    driver_metrics_sorted = sorted(driver_metrics, key=lambda x: x["fastest_time"])
    table = []

    for d in driver_metrics_sorted:
        details = driver_details.get(d["driver"], {"name": "Unknown", "team": "Unknown"})
        table.append([
            d["driver"],
            details["name"],
            details["team"],
            f"{d['fastest_time']:.3f}",
            f"{d['average_time']:.3f}"
        ])

    print(tabulate(table, headers=["Code", "Name", "Team", "Fastest Time", "Average Time"], tablefmt="grid"))

# Function to visualize lap times using Matplotlib
def visualize_lap_times(grand_prix_location, driver_metrics, driver_details):
    drivers = [d["driver"] for d in driver_metrics]
    fastest_times = [d["fastest_time"] for d in driver_metrics]
    average_times = [d["average_time"] for d in driver_metrics]

    # Creating subplots
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Bar Chart
    axes[0].bar(drivers, fastest_times, color='skyblue', edgecolor='black')
    axes[0].set_title(f"Fastest Lap Times - {grand_prix_location}", fontsize=14)
    axes[0].set_xlabel("Driver Code", fontsize=12)
    axes[0].set_ylabel("Fastest Time (seconds)", fontsize=12)
    axes[0].tick_params(axis='x', rotation=45)

    # Pie Chart
    axes[1].pie(fastest_times, labels=drivers, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    axes[1].set_title(f"Lap Time Distribution - {grand_prix_location}", fontsize=14)

    # Line Graph
    for i, driver in enumerate(drivers):
        axes[2].plot(["Fastest Time", "Average Time"], [fastest_times[i], average_times[i]], marker='o', label=driver)
    axes[2].set_title(f"Driver Performance - {grand_prix_location}", fontsize=14)
    axes[2].set_xlabel("Metric", fontsize=12)
    axes[2].set_ylabel("Time (seconds)", fontsize=12)
    axes[2].legend(title="Drivers", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

# Main function to process multiple files
def main():
    lap_times_files = ["lap_times_1.json", "lap_times_2.json", "lap_times_3.json"]
    driver_details = load_driver_details()  # Load driver details from f1_drivers.json

    for lap_times_file in lap_times_files:
        print(f"\nProcessing file: {lap_times_file}\n")
        
        # Parse lap times from JSON
        grand_prix_location, lap_times = parse_lap_times(lap_times_file)
        
        if not lap_times:  # Skip processing if no lap times found
            print(f"No data found in {lap_times_file}. Skipping...\n")
            continue
        
        # Analyze lap times
        fastest_driver, fastest_time, driver_metrics = analyze_lap_times(lap_times)
        
        # Display results on console
        display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details)
        
        # Save results to a JSON log
        log_file_name = f"{lap_times_file.split('.')[0]}_log.json"
        save_to_json_log(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, log_file_name)
        
        # Visualize results
        visualize_lap_times(grand_prix_location, driver_metrics, driver_details)

if __name__ == "__main__":
    main()
