from process import Process
from algorithms import fcfs, sjf, priority, round_robin
from tabulate import tabulate

def load_processes_from_file():
    """
    Reads process.txt and returns a list of Process instances.
    Format: <ID> <Arrival> <Burst> [Priority]
    """
    processes = []
    try:
        with open("process.txt", "r") as file:
            for line_num, line in enumerate(file, 1):
                parts = line.strip().split()
                if len(parts) < 3:
                    print(f"Skipping invalid line {line_num} in process.txt.")
                    continue

                process_id = int(parts[0])
                arrival_time = int(parts[1])
                burst_time = int(parts[2])
                priority = int(parts[3]) if len(parts) > 3 else None

                processes.append(Process(process_id, arrival_time, burst_time, priority))

    except FileNotFoundError:
        print("❌ process.txt not found. Make sure you have input data.")
    except ValueError:
        print("❌ Invalid data in process.txt. Ensure all fields are integers.")

    return processes


def run_simulation(algorithm_choice, quantum=None):
    """
    Runs the chosen algorithm.
    """
    processes = load_processes_from_file()
    if not processes:
        print("❌ No processes to simulate.")
        return None

    if algorithm_choice == 1:
        result = fcfs.run_fcfs(processes)
    elif algorithm_choice == 2:
        result = sjf.run_sjf(processes)
    elif algorithm_choice == 3:
        result = priority.run_priority(processes)
    elif algorithm_choice == 4:
        # Use default quantum if none provided
        result = round_robin.run_round_robin(processes, quantum=quantum or 2)
    else:
        print("❌ Invalid algorithm choice.")
        return None

    log_simulation_result(algorithm_choice, result, quantum)
    return result


def log_simulation_result(algorithm_choice, result, quantum=None):
    """
    Appends the results to simulations.txt.
    """
    algo_name = {
        1: "First-Come, First-Served (FCFS)",
        2: "Shortest Job First (SJF)",
        3: "Priority Scheduling",
        4: f"Round Robin (Quantum={quantum or 2})"
    }.get(algorithm_choice, "Unknown")

    with open("simulations.txt", "a") as f:
        f.write("\n===============================\n")
        f.write(f"Algorithm: {algo_name}\n")
        f.write(f"Average Waiting Time: {result['avg_waiting_time']:.2f}\n")
        f.write(f"Average Turnaround Time: {result['avg_turnaround_time']:.2f}\n")
        f.write(f"Context Switches: {result['context_switches']}\n")
        f.write("Gantt Chart:\n")
        f.write(generate_gantt_chart_string(result['gantt_chart']))
        f.write("\nProcesses:\n")

        # ✅ NEW: Format process table with tabulate
        table_data = [
            [
                p.process_id,
                p.arrival_time,
                p.burst_time,
                p.priority if p.priority is not None else "-",
                p.waiting_time,
                p.turnaround_time
            ]
            for p in result['processes']
        ]

        headers = ["ID", "Arrival", "Burst", "Priority", "Waiting", "Turnaround"]
        table = tabulate(table_data, headers, tablefmt="grid")

        f.write(table)
        f.write("\n")


def generate_gantt_chart_string(gantt_chart):
    """
    Converts gantt_chart list to a string for logging.
    Format: [P1 | P2 | ...] with time markers
    """
    chart = ""
    timeline = ""
    for pid, start, end in gantt_chart:
        chart += f"| P{pid} "
        timeline += f"{start}    "
    # Add last end time
    timeline += f"{gantt_chart[-1][2]}" if gantt_chart else ""

    return f"{chart}|\n{timeline}\n"