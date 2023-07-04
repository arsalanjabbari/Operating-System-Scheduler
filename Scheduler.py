from Algo_Anal import analyze_algorithm
from Process_Anal import analyze_processes
from Queue import *
from Test_Section import create_directory, create_file


def FCFS_scheduling_algorithm(job_queue):

    create_directory("./output/FCFS")
    algorithm_procedure_output_file = create_file("./output/FCFS/", "FCFS - Algorithm Procedure", ".log")
    algorithm_analysis_output_file = create_file("./output/FCFS/", "FCFS - Algorithm Analysis", ".log")
    processes_analysis_output_file = create_file("./output/FCFS/", "FCFS - Processes Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)

    current_time = 0

    algorithm_procedure_output_file.write("***First Come, First Serve (FCFS) Scheduling Algorithm in Operating System"
                                          "***\n\n")
    print_queue(job_queue)
    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write(f"Time = {current_time}-{current_time + 1}:\n")

        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            enqueue(ready_queue, dequeue(job_queue))
            algorithm_procedure_output_file.write("\tProcess-{} Moved From Job-Queue to Ready-Queue."
                                                  "\n".format(rear(ready_queue).process_id))

        if not is_empty(ready_queue) and running_process is None:
            running_process = dequeue(ready_queue)
            if running_process.response_time == -1:
                running_process.response_time = current_time
            algorithm_procedure_output_file.write("\tProcess-{} Moved From Ready-Queue to Running-State.\n"
                                                  .format(running_process.process_id))

        if not is_empty(waiting_queue):
            waiting_queue.front().IO_burst_time -= 1
            algorithm_procedure_output_file.write("\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O"
                                                  " Waiting Time = {}).\n".format(waiting_queue.front().process_id,
                                                                                  waiting_queue.front().IO_burst_time))
            if waiting_queue.front().IO_burst_time == 0:
                enqueue(dequeue(waiting_queue), ready_queue)
                algorithm_procedure_output_file.write("\tProcess-{}'s I/O Waiting Time Was Finished and Was Moved From"
                                                      " Waiting-Queue to Ready-Queue.\n"
                                                      .format(ready_queue.rear().process_id))

        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write("\tProcess-{}'s Second CPU Burst Was Executed for 1 Second"
                                                          " (Remaining Second CPU Burst Time = {}).\n"
                                                          .format(running_process.process_id, running_process
                                                                  .CPU_burst_time_2))
                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - running_process \
                            .arrival_time
                        running_process.waiting_time = \
                            running_process.turn_around_time - \
                            (running_process.CPU_burst_time_1 +
                             running_process.IO_burst_time + running_process.CPU_burst_time_2)
                        running_process = None
                        algorithm_procedure_output_file.write("\tProcess-{} Was Terminated (Moved From Running-State to"
                                                              " Terminated-Queue).\n"
                                                              .format(terminated_queue.rear().process_id))
                else:
                    running_process.CPU_burst_time_1 -= 1
                    algorithm_procedure_output_file.write("\tProcess-{}'s First CPU Burst Was Executed for 1 Second "
                                                          "(Remaining First CPU Burst Time = {}).\n"
                                                          .format(running_process.process_id, running_process.
                                                                  CPU_burst_time_1))
                    if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                        enqueue(waiting_queue, running_process)
                        running_process = None
                        algorithm_procedure_output_file.write("\tProcess-{} Moved From Running-State to Waiting-Queue"
                                                              "to Execute Its IO Burst.\n".format(waiting_queue.rear()
                                                                                                  .process_id))

        current_time += 1


    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()
