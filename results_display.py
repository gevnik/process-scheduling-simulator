import os

def display_simulation_results():
    """
    Reads and prints all simulation runs stored in simulations.txt.
    """
    file_path = "simulations.txt"

    if not os.path.exists(file_path):
        print("❌ No simulations found yet. Run a simulation first!")
        return

    with open(file_path, "r") as f:
        content = f.read()

        if not content.strip():
            print("❌ simulations.txt is empty. No results to display.")
            return

        print("\n===============================")
        print("📊 All Simulation Results")
        print("===============================\n")
        print(content)


def display_latest_simulation():
    """
    Shows only the most recent simulation result.
    Useful if you want to highlight the latest run.
    """
    file_path = "simulations.txt"

    if not os.path.exists(file_path):
        print("❌ No simulations found yet. Run a simulation first!")
        return

    with open(file_path, "r") as f:
        lines = f.readlines()

    if not lines:
        print("❌ simulations.txt is empty.")
        return

    # Find last simulation separator line
    separator = "==============================="
    last_index = None
    for i in reversed(range(len(lines))):
        if separator in lines[i]:
            last_index = i
            break

    if last_index is None:
        print("❌ Could not find last simulation entry.")
        return

    print("\n===============================")
    print("📊 Latest Simulation Result")
    print("===============================\n")
    for line in lines[last_index:]:
        print(line.strip())