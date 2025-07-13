from process import Process
from collections import deque

def run_round_robin(process_list, quantum=2):
    """
    Round Robin Scheduling.
    Preemptive. Uses a fixed time quantum.
    """
    processes = sorted(process_list, key=lambda p: p.arrival_time)
    ready_queue = deque()
    time = 0
    context_switches = 0
    gantt_chart = []
    completed = []

    i = 0  # Index for processes list

    while ready_queue or i < len(processes):
        # Add new arrivals to ready queue
        while i < len(processes) and processes[i].arrival_time <= time:
            ready_queue.append(processes[i])
            i += 1

        if not ready_queue:
            time += 1
            continue

        current = ready_queue.popleft()

        if current.start_time is None:
            current.start_time = time

        exec_time = min(quantum, current.remaining_time)
        start_exec_time = time
        time += exec_time
        current.remaining_time -= exec_time

        gantt_chart.append((current.process_id, start_exec_time, time))
        context_switches += 1

        # Add any new arrivals that came during execution
        while i < len(processes) and processes[i].arrival_time <= time:
            ready_queue.append(processes[i])
            i += 1

        if current.remaining_time > 0:
            ready_queue.append(current)
        else:
            current.completion_time = time
            current.turnaround_time = current.completion_time - current.arrival_time
            current.waiting_time = current.turnaround_time - current.burst_time
            completed.append(current)

    avg_waiting_time = sum(p.waiting_time for p in completed) / len(completed)
    avg_turnaround_time = sum(p.turnaround_time for p in completed) / len(completed)

    return {
        "processes": completed,
        "avg_waiting_time": avg_waiting_time,
        "avg_turnaround_time": avg_turnaround_time,
        "context_switches": context_switches - 1,
        "gantt_chart": gantt_chart
    }