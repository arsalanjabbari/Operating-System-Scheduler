from Process_Analyze import *

def get_terminate_time(terminated_queue):
    finish_time = terminated_queue.array[0].termination_time
    for i in range(1, terminated_queue.size):
        if terminated_queue.array[i].termination_time > finish_time:
            finish_time = terminated_queue.array[i].termination_time
    return finish_time

def get_CPU_execution_time(job_queue):
    CPU_execution_time = 0
    for i in range(job_queue.size):
        CPU_execution_time += job_queue.array[i].CPU_burst_time_1 + job_queue.array[i].CPU_burst_time_2
    return CPU_execution_time

def get_CPU_utilization_percent(job_queue, terminated_queue):
    CPU_execution_time = get_CPU_execution_time(job_queue)
    finish_time = get_terminate_time(terminated_queue)
    return (CPU_execution_time / finish_time) * 100

def get_CPU_idle_time(job_queue, terminated_queue):
    finish_time = get_terminate_time(terminated_queue)
    CPU_execution_time = get_CPU_execution_time(job_queue)
    return finish_time - CPU_execution_time

def get_throughput(terminated_queue):
    finish_time = get_terminate_time(terminated_queue)
    return finish_time / float(terminated_queue.size)

def get_average_turnaround_time(terminated_queue):
    average_turnaround_time = 0
    for i in range(terminated_queue.size):
        average_turnaround_time += get_process_turnaround_time(terminated_queue.array[i])
    return average_turnaround_time / terminated_queue.size

def get_average_waiting_time(terminated_queue, job_queue):
    average_waiting_time = 0
    for i in range(terminated_queue.size):
        average_waiting_time += get_process_waiting_time(terminated_queue.array[i], job_queue)
    return average_waiting_time / terminated_queue.size

def get_average_response_time(terminated_queue):
    average_response_time = 0
    for i in range(terminated_queue.size):
        average_response_time += terminated_queue.array[i].response_time
    return average_response_time / terminated_queue.size

def analyze_algorithm(job_queue, terminated_queue, output_file):
    CPU_execution_time = get_CPU_execution_time(job_queue)
    CPU_idle_time = get_CPU_idle_time(job_queue, terminated_queue)
    CPU_utilization = get_CPU_utilization_percent(job_queue, terminated_queue)
    throughput = get_throughput(terminated_queue)
    average_turnaround_time = get_average_turnaround_time(terminated_queue)
    average_waiting_time = get_average_waiting_time(terminated_queue, job_queue)
    average_response_time = get_average_response_time(terminated_queue)

    output_file.write("*****\nAlgorithm Analysis:")
    output_file.write(f"*\nCPU execution time: {CPU_execution_time}\n")
    output_file.write(f"*\nCPU idle time: {CPU_idle_time}\n")
    output_file.write(f"*\nCPU utilization: {CPU_utilization:.2f}%\n")
    output_file.write(f"*\nThroughput: {throughput:.2f}\n")
    output_file.write(f"*\nAverage turnaround time: {average_turnaround_time:.2f}\n")
    output_file.write(f"*\nAverage waiting time: {average_waiting_time:.2f}\n")
    output_file.write(f"*\nAverage response time: {average_response_time:.2f}\n")
