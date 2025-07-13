from tabulate import tabulate
import input_handler
import simulation
import results_display
import utils

def main():
    """
    CLI flow for Process Scheduling Simulator.
    """
    utils.print_separator()
    input_handler.display_instructions()
    utils.print_separator()

    # Step 1: Get input mode
    while True:
        print("\nChoose input mode:")
        print("[1] Manual Input")
        print("[2] File Input")
        input_mode = input("Enter choice (1 or 2): ").strip()

        if input_mode == "1":
            input_handler.manual_input()
            break
        elif input_mode == "2":
            input_handler.file_input()
            break
        else:
            print("❌ Invalid input mode. Please enter 1 or 2.")

    # Step 2: Run simulations loop
    while True:
        utils.print_separator()
        print("\nSelect Scheduling Algorithm:")
        print("[1] First-Come, First-Served (FCFS)")
        print("[2] Shortest Job First (SJF)")
        print("[3] Priority Scheduling")
        print("[4] Round Robin")

        try:
            choice = int(input("Enter your choice (1-4): ").strip())

            quantum = None
            if choice == 4:
                quantum = int(input("Enter quantum time (int > 0): "))
                if quantum <= 0:
                    print("❌ Quantum must be > 0. Using default quantum = 2.")
                    quantum = 2

            result = simulation.run_simulation(choice, quantum)

            if result:
                utils.print_separator()
                print(f"\n✅ Simulation Complete!")
                print(f"Average Waiting Time: {result['avg_waiting_time']:.2f}")
                print(f"Average Turnaround Time: {result['avg_turnaround_time']:.2f}")
                print(f"Context Switches: {result['context_switches']}")
                print("\nGantt Chart:")
                utils.print_gantt_chart(result['gantt_chart'])

                # ✅ NEW: Pretty table with tabulate
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

                print("\nProcesses:")
                print(tabulate(table_data, headers, tablefmt="grid"))

                print("\nFull simulation result saved to simulations.txt.")
                show_latest = input("Show latest simulation from file? (y/n): ").lower()
                if show_latest == "y":
                    results_display.display_latest_simulation()

            else:
                print("❌ Simulation failed. Please check your process input.")

        except ValueError:
            print("❌ Invalid input. Please enter integers only.")
            continue

        # Run another?
        run_again = input("\nRun another algorithm on the same input? (y/n): ").lower()
        if run_again != "y":
            break

    # Final step: Optionally clear process.txt
    clear_file = input("\nDo you want to clear process.txt? (y/n): ").lower()
    if clear_file == "y":
        utils.clear_process_file()
        print("✅ process.txt cleared.")

    utils.print_separator()
    print("🎉 Thank you for using the Process Scheduling Simulator!")
    utils.print_separator()

if __name__ == "__main__":
    main()