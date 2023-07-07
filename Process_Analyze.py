from Queue import *

def get_process_turnaround_time(selected_process):
    return selected_process.termination_time - selected_process.arrival_time

def get_process_waiting_time(selected_process, job_queue):
    tat = get_process_turnaround_time(selected_process)
    process_temp = project_process_from_queue(job_queue, selected_process)
    return tat - (process_temp.CPU_burst_time_1 + process_temp.IO_burst_time + process_temp.CPU_burst_time_2)

def analyze_processes_of_queue(job_queue, terminated_queue, output_file):
    for i in range(terminated_queue.size):
        selected_process = terminated_queue.array[i]
        output_file.write(f"Process {selected_process.process_id}:\n")
        output_file.write(f"\tarrival time: {selected_process.arrival_time}\n")
        output_file.write(f"\ttermination time: {selected_process.termination_time}\n")
        output_file.write(f"\tresponse time: {selected_process.response_time}\n")
        output_file.write(f"\tturnaround time: {get_process_turnaround_time(selected_process)}\n")
        output_file.write(f"\twaiting time: {get_process_waiting_time(selected_process, job_queue)}\n")
