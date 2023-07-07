class Process:
    def __init__(self, process_id, arrival_time, CPU_burst_time_1, CPU_burst_time_2, IO_burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.CPU_burst_time_1 = CPU_burst_time_1
        self.CPU_burst_time_2 = CPU_burst_time_2
        self.IO_burst_time = IO_burst_time
        self.response_time = -1
        self.turn_around_time = -1
        self.waiting_time = -1
        self.termination_time = -1

def print_process(selected_process):
    print(f"Process ID: {selected_process.process_id} |"
          f"Arrival Time: {selected_process.arrival_time} | "
          f"CPU Burst Time 1: {selected_process.CPU_burst_time_1} |"
          f"IO Burst Time: {selected_process.IO_burst_time} | "
          f"CPU Burst Time 2: {selected_process.CPU_burst_time_2} |"
          f"Response Time: {selected_process.response_time} | "
          f"Turn Around Time: {selected_process.turn_around_time} |"
          f"Waiting Time: {selected_process.waiting_time} | "
          f"Termination Time: {selected_process.termination_time}")

def copy_process(selected_process):
    new_process = Process(selected_process.process_id,
                          selected_process.arrival_time,
                          selected_process.CPU_burst_time_1,
                          selected_process.IO_burst_time,
                          selected_process.CPU_burst_time_2)
    new_process.response_time = selected_process.response_time
    new_process.turn_around_time = selected_process.turn_around_time
    new_process.waiting_time = selected_process.waiting_time
    new_process.termination_time = selected_process.termination_time
    return new_process