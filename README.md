# Process Scheduling Algorithm Simulator

A simple, modular CLI-based simulator to compare classical CPU scheduling algorithms:\
**First-Come, First-Served (FCFS)**, **Shortest Job First (SJF)**, **Priority Scheduling**, and **Round Robin**.

---

## 📍 Project Description

This project simulates how an operating system schedules processes for CPU execution.\
It allows you to:

- Input processes manually or from a file.
- Run different scheduling algorithms on the same input.
- View key performance metrics: average waiting time, average turnaround time, context switches.
- Visualize a textual Gantt chart.
- Compare results across multiple runs saved in `simulations.txt`.

---

## ✅ Features

- Command-line interface for easy interaction.
- Supports up to 100 processes.
- Modular code structure: each algorithm in its own file.
- Clear error messages for invalid input.
- Works on Linux or Mac (tested on Ubuntu 22.04 / macOS).

---

## 📂 Project Structure

```
scheduling_simulator/
│
├── main.py                 # Entry point for the CLI
├── input_handler.py        # Manual & file input with validation
├── simulation.py           # Runs selected algorithm & logs results
├── results_display.py      # Displays past simulation runs
├── utils.py                # Helper functions (e.g., Gantt chart)
│
├── algorithms/             # All scheduling algorithms
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   ├── round_robin.py
│
├── process.py              # Process data class
├── instructions.txt        # Static CLI instructions
├── process.txt             # Stores current process input
├── simulations.txt         # Stores all simulation results
│
├── requirements.txt        # Any Python dependencies
├── README.md               # This file
├── .gitignore              # Ignores venv, __pycache__, etc.
├── venv/                   # Virtual environment (not committed)
```

---

## ⚙️ Requirements

- Python 3.x
- Works in a virtual environment (recommended)

---

## 🚀 How to Run

1. **Clone the repo & activate your environment**

   ```bash
   git clone https://github.com/gevnik/scheduling_simulator.git
   cd scheduling_simulator
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install any dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program**

   ```bash
   python main.py
   ```

4. **Follow the CLI prompts**

   - Read the instructions.
   - Choose manual input or file input.
   - Enter your processes: `ProcessID ArrivalTime BurstTime [Priority]`
   - Select an algorithm.
   - View results and Gantt chart.
   - Optionally run another algorithm on the same input.

---

## 📥 Example Input File

For **file input**, use a text file like `example_input.txt`:

```
1 0 5 2
2 2 3 1
3 4 6 3
```

Format:

```
<ProcessID> <ArrivalTime> <BurstTime> [Priority]
```

Priority is optional and only used for Priority Scheduling.

---

## 📊 Example Output

After running FCFS:

```
✅ Simulation Complete!
Average Waiting Time: 2.00
Average Turnaround Time: 6.00
Context Switches: 2

Gantt Chart:
| P1 | P2 | P3 |
0    5    8    14

Processes:
ID=1 Arrival=0 Burst=5 Waiting=0 Turnaround=5
ID=2 Arrival=2 Burst=3 Waiting=3 Turnaround=6
ID=3 Arrival=4 Burst=6 Waiting=6 Turnaround=10
```

All results are saved in `simulations.txt`.

---

## 🗑️ Clearing Input

After you’re done, you can choose to clear `process.txt` for the next run.

---

## 💡 Tips

- Always validate your input: unique IDs, non-negative arrival time, positive burst time.
- Run multiple algorithms on the same input for comparative analysis.
- Check `simulations.txt` to review all past runs.

---

## 👨‍💼 Authors

Mikhail Nozhkin\
Sudhan Shrestha\
Abhishek Mishra\
Vitor Takao Kihara

Fairleigh Dickinson University, Vancouver, Canada

---

## 📜 License

For academic use only.