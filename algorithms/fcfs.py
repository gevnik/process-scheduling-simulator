from process import Process

def run_fcfs(process_list):
    """
    First-Come, First-Served Scheduling.
    Non-preemptive. Processes run in order of arrival.
    """
    processes = sorted(process_list, key=lambda p: p.arrival_time)
    time = 0
    context_switches = 0
    gantt_chart = []

    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time

        process.start_time = time
        process.waiting_time = time - process.arrival_time
        process.completion_time = time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time

        time += process.burst_time
        context_switches += 1
        gantt_chart.append((process.process_id, process.start_time, process.completion_time))

    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)

    return {
        "processes": processes,
        "avg_waiting_time": avg_waiting_time,
        "avg_turnaround_time": avg_turnaround_time,
        "context_switches": context_switches - 1,  # no switch for first process
        "gantt_chart": gantt_chart
    }