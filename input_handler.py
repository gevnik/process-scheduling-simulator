from process import Process
import os


def display_instructions():
    """
    Reads and prints instructions from instructions.txt.
    """
    if not os.path.exists("instructions.txt"):
        print("Instructions file not found.")
        return

    with open("instructions.txt", "r") as file:
        instructions = file.read()
        print(instructions)


def manual_input():
    """
    Handles manual process entry via CLI.
    Requires at least one valid process.
    Saves validated processes to process.txt.
    """
    process_list = []
    process_ids = set()

    print("\n=== Manual Input Mode ===\n")
    print("Refer to the instructions above for the expected format.")

    while True:
        try:
            process_id = int(input("Enter Process ID: "))
            if process_id in process_ids:
                print("❌ Process ID must be unique. Try again.")
                continue

            arrival_time = int(input("Enter Arrival Time: "))
            burst_time = int(input("Enter Burst Time: "))
            priority_input = input("Enter Priority (optional, press Enter to skip): ")
            priority = int(priority_input) if priority_input.strip() else None

            if arrival_time < 0 or burst_time <= 0:
                print("❌ Arrival time must be >= 0 and burst time must be > 0.")
                continue

            process = Process(process_id, arrival_time, burst_time, priority)
            process_list.append(process)
            process_ids.add(process_id)

            another = input("Add another process? (y/n): ").strip().lower()
            if another != 'y':
                break

        except ValueError:
            print("❌ Invalid input. Please enter integers where required.")

    if not process_list:
        print("❌ No valid processes entered. Please try again.")
        return manual_input()

    write_processes_to_file(process_list)
    print(f"\n✅ {len(process_list)} processes saved to process.txt.\n")


def file_input():
    """
    Loads process data from a file.
    Validates and saves the data to process.txt.
    Keeps prompting until a valid file is found.
    """
    print("\n=== File Input Mode ===\n")
    print("Refer to the instructions above for the expected file format.\n")

    while True:
        file_path = input("Enter path to your input file: ").strip()

        if not os.path.exists(file_path):
            print("❌ File not found. Please check the path and try again.\n")
            continue

        process_list = []
        process_ids = set()

        try:
            with open(file_path, "r") as file:
                for line_num, line in enumerate(file, 1):
                    if not line.strip():
                        continue
                    parts = line.strip().split()
                    if len(parts) < 3:
                        print(f"❌ Invalid format on line {line_num}. Skipping.")
                        continue

                    process_id = int(parts[0])
                    arrival_time = int(parts[1])
                    burst_time = int(parts[2])
                    priority = int(parts[3]) if len(parts) > 3 else None

                    if process_id in process_ids:
                        print(f"❌ Duplicate Process ID {process_id} on line {line_num}. Skipping.")
                        continue

                    if arrival_time < 0 or burst_time <= 0:
                        print(f"❌ Invalid arrival/burst time on line {line_num}. Skipping.")
                        continue

                    process = Process(process_id, arrival_time, burst_time, priority)
                    process_list.append(process)
                    process_ids.add(process_id)

        except ValueError:
            print("❌ Non-integer value found in input file. Please fix and retry.")
            continue

        if process_list:
            write_processes_to_file(process_list)
            print(f"\n✅ {len(process_list)} valid processes saved to process.txt.\n")
            break
        else:
            print("❌ No valid processes found in this file. Please try again.\n")


def write_processes_to_file(process_list):
    """
    Saves processes to process.txt in standard format.
    Format: ID Arrival Burst [Priority]
    """
    with open("process.txt", "w") as file:
        for p in process_list:
            line = f"{p.process_id} {p.arrival_time} {p.burst_time}"
            if p.priority is not None:
                line += f" {p.priority}"
            file.write(line + "\n")