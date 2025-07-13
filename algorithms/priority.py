from process import Process

def run_priority(process_list):
    """
    Priority Scheduling.
    Non-preemptive. Lower priority number = higher priority.
    """
    processes = sorted(process_list, key=lambda p: (p.arrival_time, p.priority))
    completed = []
    time = 0
    context_switches = 0
    gantt_chart = []

    ready_queue = []

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= time:
            ready_queue.append(processes.pop(0))

        if ready_queue:
            ready_queue.sort(key=lambda p: (p.priority, p.arrival_time))
            current = ready_queue.pop(0)

            if time < current.arrival_time:
                time = current.arrival_time

            current.start_time = time
            current.waiting_time = time - current.arrival_time
            current.completion_time = time + current.burst_time
            current.turnaround_time = current.completion_time - current.arrival_time

            time += current.burst_time
            context_switches += 1
            gantt_chart.append((current.process_id, current.start_time, current.completion_time))

            completed.append(current)
        else:
            time += 1

    avg_waiting_time = sum(p.waiting_time for p in completed) / len(completed)
    avg_turnaround_time = sum(p.turnaround_time for p in completed) / len(completed)

    return {
        "processes": completed,
        "avg_waiting_time": avg_waiting_time,
        "avg_turnaround_time": avg_turnaround_time,
        "context_switches": context_switches - 1,
        "gantt_chart": gantt_chart
    }