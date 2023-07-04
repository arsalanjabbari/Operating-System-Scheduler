from Queue import Queue

def get_process_turnaround_time(self):
    return process.termination_time - process.arrival_time

def get_process_waiting_time(self, job_queue):
    queue_process = Queue.get_process_from_queue(process, job_queue)
    return get_process_turnaround_time(process) - (queue_process.CPU_burst_time_1 + queue_process.IO_burst_time +
                                                   queue_process.CPU_burst_time_2)

def analyze_processes(job_queue, terminated_queue, output_file):
    for i in range(terminated_queue.size):
        process = terminated_queue.array[i]
        output_file.write(f"Process {process.process_id}:\n")
        output_file.write(f"\tarrival time: {process.arrival_time}\n")
        output_file.write(f"\ttermination time: {process.termination_time}\n")
        output_file.write(f"\tresponse time: {process.response_time}\n")
        output_file.write(f"\tturnaround time: {get_process_turnaround_time(process)}\n")
        output_file.write(f"\twaiting time: {get_process_waiting_time(process, job_queue)}\n")
