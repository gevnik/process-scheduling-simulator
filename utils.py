def print_separator():
    """
    Prints a nice separator line for CLI output.
    """
    print("=" * 40)


def print_gantt_chart(gantt_chart):
    """
    Displays a clear textual Gantt chart in CLI.
    Format: | P1 | P2 | P3 | ...
            0    3    7    10
    """
    if not gantt_chart:
        print("No Gantt chart data to display.")
        return

    chart_line = ""
    timeline = ""

    for pid, start, end in gantt_chart:
        chart_line += f"| P{pid} "
        timeline += f"{start:<5}"

    timeline += f"{gantt_chart[-1][2]}"  # Add final end time

    print(chart_line + "|")
    print(timeline)


def clear_process_file():
    """
    Clears the contents of process.txt.
    """
    with open("process.txt", "w") as f:
        pass