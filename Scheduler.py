from Algorithm_Analyze import analyze_algorithm
from Process_Analyze import analyze_processes
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
    algorithm_procedure_output_file.write("*** First Come, First Serve (FCFS) Scheduling Algorithm in Operating System "
                                          "***\n\n")
    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write(f"Time = {current_time}-{current_time + 1}:\n")

        if not is_empty(job_queue) and (front(job_queue).arrival_time <= current_time):
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
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write("\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O"
                                                  " Waiting Time = {}).\n".format(front(waiting_queue).process_id,
                                                                                  front(waiting_queue).IO_burst_time))
            if front(waiting_queue).IO_burst_time == 0:
                enqueue(ready_queue, dequeue(waiting_queue))
                algorithm_procedure_output_file.write("\tProcess-{}'s I/O Waiting Time Was Finished and Was Moved From"
                                                      " Waiting-Queue to Ready-Queue.\n"
                                                      .format(rear(ready_queue).process_id))

        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        f"\tProcess-{running_process.process_id}'s Second CPU Burst Was Executed for 1 Second (Remaining Second CPU Burst Time = {running_process.CPU_burst_time_2}).\n")
                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - running_process.arrival_time
                        running_process.waiting_time = running_process.turn_around_time - (
                                    running_process.CPU_burst_time_1 + running_process.IO_burst_time + running_process.CPU_burst_time_2)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            f"\tProcess-{rear(terminated_queue).process_id} Was Terminated (Moved From Running-State to Terminated-Queue).\n")
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    f"\tProcess-{running_process.process_id}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {running_process.CPU_burst_time_1}).\n")
                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    enqueue(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        f"\tProcess-{rear(waiting_queue).process_id} Moved From Running-State to Waiting-Queue to Execute Its IO Burst.\n")

        current_time += 1


    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()

def RR_scheduling_algorithm(job_queue):

    create_directory("./output/RR")
    algorithm_procedure_output_file = create_file("./output/RR/", "RR - Algorithm Procedure", ".log")
    algorithm_analysis_output_file = create_file("./output/RR/", "RR - Algorithm Analysis", ".log")
    processes_analysis_output_file = create_file("./output/RR/", "RR - Processes Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)

    current_time = 0
    algorithm_procedure_output_file.write("*** Round-Robin (RR) Scheduling Algorithm in Operating System "
                                          "***\n\n")
    print("Enter your desired time-quantum:")
    time_quantum = int(input())
    temp_elapsed_time = 0

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))

        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            enqueue(ready_queue, dequeue(job_queue))
            algorithm_procedure_output_file.write(
                "\tProcess-{} Moved From Job-Queue to Ready-Queue.\n".format(rear(ready_queue).process_id))

        if not is_empty(ready_queue) and running_process is None:
            # Move the process from the ready queue to the running state
            running_process = dequeue(ready_queue)
            execution_elapsed_time = 0
            if running_process.response_time == -1:
                running_process.response_time = current_time
            algorithm_procedure_output_file.write(
                "\tProcess-{} Moved From Ready-Queue to Running-State.\n".format(running_process.process_id))

        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))

            if front(waiting_queue).IO_burst_time == 0:
                enqueue(ready_queue, dequeue(waiting_queue))
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s IO's Waiting Time Was Finished and Was Moved From Waiting-Queue to Ready-Queue.\n".format(
                        rear(ready_queue).process_id))

        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    temp_elapsed_time += 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second (Remaining Second CPU Burst Time = {}).\n".format(
                            running_process.process_id, running_process.CPU_burst_time_2))

                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - running_process.arrival_time
                        running_process.waiting_time = running_process.turn_around_time - (
                                    running_process.CPU_burst_time_1 + running_process.IO_burst_time + running_process.CPU_burst_time_2)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Was Terminated (Moved From Running-State to Terminated-Queue).\n".format(
                                rear(terminated_queue).process_id))

                    if temp_elapsed_time == time_quantum:
                        enqueue(ready_queue, running_process)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{}'s Time Quantum Was Finished and Was Moved From Running-State to Ready-Queue.\n".format(
                                rear(ready_queue).process_id))
            else:
                running_process.CPU_burst_time_1 -= 1
                temp_elapsed_time += 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {}).\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))

                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    enqueue(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        "\tProcess-{} Moved From Running-State to Waiting-Queue to Execute Its IO Burst.\n".format(
                            rear(waiting_queue).process_id))
                elif temp_elapsed_time == time_quantum:
                    enqueue(ready_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Time Quantum Was Finished and Was Moved From Running-State to Ready-Queue.\n".format(
                            rear(ready_queue).process_id))

        current_time += 1

    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()

def SPN_scheduling_algorithm(job_queue):

    create_directory("./output/SPN")
    algorithm_procedure_output_file = create_file("./output/SPN/", "SPN - Algorithm Procedure", ".log")
    algorithm_analysis_output_file = create_file("./output/SPN/", "SPN - Algorithm Analysis", ".log")
    processes_analysis_output_file = create_file("./output/SPN/", "SPN - Processes Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)

    current_time = 0
    algorithm_procedure_output_file.write("*** Shortest-Process-Next (SPN) Scheduling Algorithm in Operating System "
                                          "***\n\n")
    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))

        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            enqueue(ready_queue, dequeue(job_queue))
            algorithm_procedure_output_file.write(
                "\tProcess-{} Moved From Job-Queue to Ready-Queue.\n".format(rear(ready_queue).process_id))

        if not is_empty(ready_queue) and running_process is None:
            running_process = remove_process_with_minimum_CPU_burst_time(ready_queue)
            if running_process.response_time == -1:
                running_process.response_time = current_time
            algorithm_procedure_output_file.write(
                "\tProcess-{} Moved From Ready-Queue to Running-State.\n".format(running_process.process_id))

        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))

            if front(waiting_queue).IO_burst_time == 0:
                enqueue(ready_queue, dequeue(waiting_queue))
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s IO's Waiting Time Was Finished and Was Moved From Waiting-Queue to Ready-Queue.\n".format(
                        rear(ready_queue).process_id))

        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second (Remaining Second CPU Burst Time = {}).\n".format(
                            running_process.process_id, running_process.CPU_burst_time_2))

                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - running_process.arrival_time
                        running_process.waiting_time = running_process.turn_around_time - (
                                    running_process.CPU_burst_time_1 + running_process.IO_burst_time + running_process.CPU_burst_time_2)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Was Terminated (Moved From Running-State to Terminated-Queue).\n".format(
                                rear(terminated_queue).process_id))
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {}).\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))

                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    enqueue(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        "\tProcess-{} Moved From Running-State to Waiting-Queue to Execute Its IO Burst.\n".format(
                            rear(waiting_queue).process_id))

        current_time += 1

    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()

def SRTF_scheduling_algorithm(job_queue):

    create_directory("./output/SRTF")
    algorithm_procedure_output_file = create_file("./output/SRTF/", "SRTF - Algorithm Procedure", ".log")
    algorithm_analysis_output_file = create_file("./output/SRTF/", "SRTF - Algorithm Analysis", ".log")
    processes_analysis_output_file = create_file("./output/SRTF/", "SRTF - Processes Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)

    current_time = 0
    algorithm_procedure_output_file.write("*** Shortest-Remaining-Time-First (SRTF) Scheduling Algorithm in Operating System "
                                          "***\n\n")

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))

        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            enqueue(ready_queue, dequeue(job_queue))
            algorithm_procedure_output_file.write(
                "\tProcess-{} Moved From Job-Queue to Ready-Queue.\n".format(rear(ready_queue).process_id))

        if not is_empty(ready_queue) and running_process is None:
            running_process = remove_process_with_minimum_CPU_burst_time(ready_queue)
            if running_process.response_time == -1:
                running_process.response_time = current_time
            algorithm_procedure_output_file.write(
                "\tProcess-{} Moved From Ready-Queue to Running-State.\n".format(running_process.process_id))

        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))

            if front(waiting_queue).IO_burst_time == 0:
                enqueue(ready_queue, dequeue(waiting_queue))
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s IO's Waiting Time Was Finished and Was Moved From Waiting-Queue to Ready-Queue.\n".format(
                        rear(ready_queue).process_id))

        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second (Remaining Second CPU Burst Time = {}).\n".format(
                            running_process.process_id, running_process.CPU_burst_time_2))

                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - running_process.arrival_time
                        running_process.waiting_time = running_process.turn_around_time - (
                                    running_process.CPU_burst_time_1 + running_process.IO_burst_time + running_process.CPU_burst_time_2)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Was Terminated (Moved From Running-State to Terminated-Queue).\n".format(
                                rear(terminated_queue).process_id))
                    else:
                        enqueue(ready_queue, running_process)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Was Preempted (Moved From Running-State to Ready-Queue).\n".format(
                                rear(ready_queue).process_id))
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {}).\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))

                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    enqueue(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        "\tProcess-{} Moved From Running-State to Waiting-Queue to Execute Its IO Burst.\n".format(
                            rear(waiting_queue).process_id))
                else:
                    enqueue(ready_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        "\tProcess-{} Was Preempted (Moved From Running-State to Ready-Queue).\n".format(
                            rear(ready_queue).process_id))

        current_time += 1

    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()

def MLFQ_scheduling_algorithm(job_queue):

    create_directory("./output/MLFQ")
    algorithm_procedure_output_file = create_file("./output/MLFQ/", "MLFQ - Algorithm Procedure", ".log")
    algorithm_analysis_output_file = create_file("./output/MLFQ/", "MLFQ - Algorithm Analysis", ".log")
    processes_analysis_output_file = create_file("./output/MLFQ/", "MLFQ - Processes Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)

    current_time = 0
    algorithm_procedure_output_file.write("*** Multi-Level-Feedback-Queue (MLFQ) Scheduling Algorithm in Operating System "
                                          "***\n\n")



    algorithm_procedure_output_file.close()

    analyze_algorithm(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes(job_queue_copy, terminated_queue, processes_analysis_output_file)

    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()