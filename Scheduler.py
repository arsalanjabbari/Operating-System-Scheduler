from Algo_Anal import *
from Queue import *
import os


ready_queue = None
running_process = None
waiting_queue = None
terminated_queue = None

# First Come, First Serve (FCFS) Scheduling Algorithm in Operating System
def FCFS_scheduling_algorithm(job_queue):
    def create_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def create_file(directory, filename, extension):
        file_path = os.path.join(directory, filename + extension)
        return open(file_path, "w")

    def copy_queue(queue):
        return copy_queue(queue)

    def is_full(queue):
        return len(queue) == queue.capacity

    def is_empty(queue):
        return len(queue) == 0

    def front(queue):
        return queue[0]

    def rear(queue):
        return queue[-1]

    def enqueue(queue, item):
        queue.append(item)

    def dequeue(queue):
        return queue.pop(0)

    def analyze_algorithm(job_queue_copy, terminated_queue, output_file):
        # Algorithm analysis logic
        pass

    def analyze_processes(job_queue_copy, terminated_queue, output_file):
        # Process analysis logic
        pass

    create_directory("./IO/output/FCFS")
    algorithm_procedure_output_file = create_file("./IO/output/FCFS/", "FCFS - Algorithm Procedure", ".log")
    algorithm_analysis_output_file = create_file("./IO/output/FCFS/", "FCFS - Algorithm Analysis", ".log")
    processes_analysis_output_file = create_file("./IO/output/FCFS/", "FCFS - Processes Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = []
    running_process = None
    waiting_queue = []
    terminated_queue = []

    current_time = 0

    algorithm_procedure_output_file.write("***First Come, First Serve (FCFS) Scheduling Algorithm in Operating System***\n\n")
    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))

        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            enqueue(ready_queue, dequeue(job_queue))
            algorithm_procedure_output_file.write("\tProcess-{} Moved From Job-Queue to Ready-Queue.\n".format(rear(ready_queue).process_id))

        if not is_empty(ready_queue) and running_process is None:
            running_process = dequeue(ready_queue)
            if running_process.response_time == -1:
                running_process.response_time = current_time
            algorithm_procedure_output_file.write("\tProcess-{} Moved From Ready-Queue to Running-State.\n".format(running_process.process_id))

        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write("\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))
            if front(waiting_queue).IO_burst_time == 0:
                enqueue(ready_queue, dequeue(waiting_queue))
                algorithm_procedure_output_file.write("\tProcess-{}'s I/O Waiting Time Was Finished and Was Moved From Waiting-Queue to Ready-Queue.\n".format(rear(ready_queue).process_id))

        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write("\tProcess-{}'s Second CPU Burst Was Executed for 1 Second (Remaining Second CPU Burst Time = {}).\n".format(running_process.process_id, running_process.CPU_burst_time_2))
                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - running_process.arrival_time
                        running_process.waiting_time = running_process.turn_around_time - (running_process.CPU_burst_time_1 + running_process.IO_burst_time + running_process.CPU_burst_time_2)
                        running_process = None
                        algorithm_procedure_output_file.write("\tProcess-{} Was Terminated (Moved From Running-State to Terminated-Queue).\n".format(rear(terminated_queue).process_id))
                else:
                    running_process.CPU_burst_time_1 -= 1
                    algorithm_procedure_output_file.write("\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {}).\n".format(running_process.process_id, running_process.CPU_burst_time_1))
                    if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                        enqueue(waiting_queue, running_process)
                        running_process = None
                        algorithm_procedure_output_file.write("\tProcess-{} Moved From Running-State to Waiting-Queue to Execute Its IO Burst.\n".format(rear(waiting_queue).process_id))

        current_time += 1

    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()
