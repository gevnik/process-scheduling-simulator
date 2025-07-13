class Process:
    """
    Represents a single process in the scheduling simulator.
    """

    def __init__(self, process_id: int, arrival_time: int, burst_time: int, priority: int = None):
        self.process_id = process_id               # Unique ID for the process
        self.arrival_time = arrival_time           # Time at which the process arrives
        self.burst_time = burst_time               # Total CPU time required
        self.priority = priority                   # Optional, only for priority scheduling

        # Runtime/computed attributes:
        self.remaining_time = burst_time           # Used for Round Robin/preemptive versions
        self.start_time = None                     # When the process starts execution
        self.completion_time = None                # When the process finishes execution
        self.waiting_time = 0                      # Total time process has waited in the queue
        self.turnaround_time = 0                   # Total turnaround time
        self.response_time = None                  # Time from arrival to first execution

    def __repr__(self):
        """
        For easy debugging when printing lists of processes.
        """
        return (f"Process(ID={self.process_id}, Arrival={self.arrival_time}, "
                f"Burst={self.burst_time}, Priority={self.priority}, "
                f"Waiting={self.waiting_time}, Turnaround={self.turnaround_time})")

    def to_dict(self):
        """
        Helper method to convert process data to a dictionary.
        Useful for logging to simulations.txt or JSON.
        """
        return {
            "process_id": self.process_id,
            "arrival_time": self.arrival_time,
            "burst_time": self.burst_time,
            "priority": self.priority,
            "start_time": self.start_time,
            "completion_time": self.completion_time,
            "waiting_time": self.waiting_time,
            "turnaround_time": self.turnaround_time,
            "response_time": self.response_time,
        }