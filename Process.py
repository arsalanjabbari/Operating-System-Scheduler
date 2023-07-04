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

def create_new_process(process_id, arrival_time, CPU_burst_time_1, IO_burst_time, CPU_burst_time_2):
    process = Process(process_id, arrival_time, CPU_burst_time_1, IO_burst_time, CPU_burst_time_2)
    return process

def copy_process(process):
    new_process = Process(process.process_id, process.arrival_time, process.CPU_burst_time_1, process.IO_burst_time,
                          process.CPU_burst_time_2)
    new_process.response_time = process.response_time
    new_process.turn_around_time = process.turn_around_time
    new_process.waiting_time = process.waiting_time
    new_process.termination_time = process.termination_time
    return new_process

def print_process(process):
    print(f"Process ID: {process.process_id} | Arrival Time: {process.arrival_time} | CPU Burst Time 1: "
          f"{process.CPU_burst_time_1} | IO Burst Time: {process.IO_burst_time} | CPU Burst Time 2: "
          f"{process.CPU_burst_time_2} | Response Time: {process.response_time} | Turn Around Time: "
          f"{process.turn_around_time} | Waiting Time: {process.waiting_time} | Termination Time: "
          f"{process.termination_time}")
