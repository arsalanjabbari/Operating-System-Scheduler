from Algorithm_Analyze import analyze_algorithm_on_the_queue
from Process_Analyze import analyze_processes_of_queue
from Queue import *
from Test_Section import create_directory, create_file


def admit(job_queue, ready_queue):
    enqueue(ready_queue, dequeue(job_queue))
    report_text = "\tProcess-{} Moved From Job-Queue to Ready-Queue.\n".format(rear(ready_queue).process_id)
    return report_text


def dispatch(running_process, current_time):
    if running_process.response_time == -1:
        running_process.response_time = current_time
    return "\tProcess-{} Moved From Ready-Queue to Running-State.\n".format(running_process.process_id)


def preempt(ready_queue, running_process):
    enqueue(ready_queue, running_process)
    return "\tProcess-{}'s Time Quantum Was Finished and Was Moved From Running-State to Ready-Queue." \
           "\n".format(rear(ready_queue).process_id)


def IO_request(waiting_queue, running_process):
    enqueue(waiting_queue, running_process)
    return f"\tProcess-{rear(waiting_queue).process_id} Moved From Running-State to Waiting-Queue to" \
           f" Execute Its IO Burst.\n"


def IO_completion(waiting_queue, ready_queue):
    temp = dequeue(waiting_queue)
    enqueue(ready_queue, temp)
    return "\tProcess-{}'s I/O Waiting Time Was Finished and Was Moved From" \
           " Waiting-Queue to Ready-Queue.\n".format(temp.process_id)


def terminate(running_process, terminated_queue, current_time):
    enqueue(terminated_queue, running_process)
    running_process.termination_time = current_time + 1
    running_process.turn_around_time = running_process.termination_time - (
        running_process.arrival_time)
    running_process.waiting_time = running_process.turn_around_time - (
            running_process.CPU_burst_time_1 + running_process.IO_burst_time
            + running_process.CPU_burst_time_2)
    return f"\tProcess-{rear(terminated_queue).process_id} Was Terminated " \
           f"(Moved From Running-State to Terminated-Queue).\n"


def FCFS_scheduling_algorithm(job_queue):
    create_directory("./output/FCFS")
    algorithm_procedure_output_file = create_file("./output/FCFS/", "FCFS - Scheduling Timeline Flow", ".log")
    algorithm_analysis_output_file = create_file("./output/FCFS/", "FCFS - Algorithm's Analysis", ".log")
    processes_analysis_output_file = create_file("./output/FCFS/", "FCFS - Job-Queue's Processes' Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)
    current_time = 0
    algorithm_procedure_output_file.write("***"
                                          " First Come, First Served (FCFS) Scheduling Algorithm in Operating System "
                                          "***\n\n")

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write(f"Time = {current_time}-{current_time + 1}:\n")
        if not is_empty(job_queue) and (front(job_queue).arrival_time <= current_time):
            admit_report = admit(job_queue, ready_queue)
            algorithm_procedure_output_file.write(admit_report)
        if not is_empty(ready_queue) and running_process is None:
            running_process = dequeue(ready_queue)
            dispatch_report = dispatch(running_process, current_time)
            algorithm_procedure_output_file.write(dispatch_report)
        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write("\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O"
                                                  " Waiting Time = {}).\n".format(front(waiting_queue).process_id,
                                                                                  front(waiting_queue).IO_burst_time))
            if front(waiting_queue).IO_burst_time == 0:
                IO_comp_report = IO_completion(waiting_queue, ready_queue)
                algorithm_procedure_output_file.write(IO_comp_report)
        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        f"\tProcess-{running_process.process_id}'s Second CPU Burst Was Executed for 1 Second"
                        f" (Remaining Second CPU Burst Time = {running_process.CPU_burst_time_2}).\n")
                    if running_process.CPU_burst_time_2 == 0:
                        terminate_report = terminate(running_process, terminated_queue, current_time)
                        running_process = None
                        algorithm_procedure_output_file.write(terminate_report)
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    f"\tProcess-{running_process.process_id}'s First CPU Burst Was Executed for 1 Second "
                    f"(Remaining First CPU Burst Time = {running_process.CPU_burst_time_1}).\n")
                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    IO_req_report = IO_request(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(IO_req_report)
        current_time += 1

    algorithm_procedure_output_file.close()
    analyze_algorithm_on_the_queue(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes_of_queue(terminated_queue, processes_analysis_output_file)
    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()


def RR_scheduling_algorithm(job_queue):
    create_directory("./output/RR")
    algorithm_procedure_output_file = create_file("./output/RR/", "RR - Scheduling Timeline Flow", ".log")
    algorithm_analysis_output_file = create_file("./output/RR/", "RR - Algorithm's Analysis", ".log")
    processes_analysis_output_file = create_file("./output/RR/", "RR - Job-Queue's Processes' Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)

    current_time = 0
    algorithm_procedure_output_file.write("*** Round-Robin (RR) Scheduling Algorithm in Operating System "
                                          "***\n\n")

    time_quantum = int(input("Enter your desired time-quantum: "))
    temp_elapsed_time = 0

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))
        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            admit_report = admit(job_queue, ready_queue)
            algorithm_procedure_output_file.write(admit_report)
        if not is_empty(ready_queue) and running_process is None:
            running_process = dequeue(ready_queue)
            dispatch_report = dispatch(running_process, current_time)
            algorithm_procedure_output_file.write(dispatch_report)
        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))
            if front(waiting_queue).IO_burst_time == 0:
                IO_comp_report = IO_completion(waiting_queue, ready_queue)
                algorithm_procedure_output_file.write(IO_comp_report)
        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    temp_elapsed_time += 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second "
                        "(Remaining Second CPU Burst Time = {}).\n".format(
                            running_process.process_id, running_process.CPU_burst_time_2))
                    if running_process.CPU_burst_time_2 == 0:
                        terminate_report = terminate(running_process, terminated_queue, current_time)
                        running_process = None
                        algorithm_procedure_output_file.write(terminate_report)
                    if temp_elapsed_time == time_quantum:
                        preempt_report = preempt(ready_queue, running_process)
                        running_process = None
                        algorithm_procedure_output_file.write(preempt_report)
            else:
                running_process.CPU_burst_time_1 -= 1
                temp_elapsed_time += 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {})."
                    "\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))
                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    IO_req_report = IO_request(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(IO_req_report)
                elif temp_elapsed_time == time_quantum:
                    preempt_report = preempt(ready_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(preempt_report)
        current_time += 1

    algorithm_procedure_output_file.close()
    analyze_algorithm_on_the_queue(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes_of_queue(terminated_queue, processes_analysis_output_file)
    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()


def SPN_scheduling_algorithm(job_queue):
    create_directory("./output/SPN")
    algorithm_procedure_output_file = create_file("./output/SPN/", "SPN - Scheduling Timeline Flow", ".log")
    algorithm_analysis_output_file = create_file("./output/SPN/", "SPN - Algorithm's Analysis", ".log")
    processes_analysis_output_file = create_file("./output/SPN/", "SPN - Job-Queue's Processes' Analysis", ".log")

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
            admit_report = admit(job_queue, ready_queue)
            algorithm_procedure_output_file.write(admit_report)
        if not is_empty(ready_queue) and running_process is None:
            running_process = remove_process_with_minimum_CPU_burst_time(ready_queue)
            dispatch_report = dispatch(running_process, current_time)
            algorithm_procedure_output_file.write(dispatch_report)
        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))
            if front(waiting_queue).IO_burst_time == 0:
                IO_comp_report = IO_completion(waiting_queue, ready_queue)
                algorithm_procedure_output_file.write(IO_comp_report)
        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second "
                        "(Remaining Second CPU Burst Time = {}).\n".format(running_process.process_id,
                                                                           running_process.CPU_burst_time_2))
                    if running_process.CPU_burst_time_2 == 0:
                        terminate_report = terminate(running_process, terminated_queue, current_time)
                        running_process = None
                        algorithm_procedure_output_file.write(terminate_report)
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {})."
                    "\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))
                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    IO_req_report = IO_request(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(IO_req_report)
        current_time += 1

    algorithm_procedure_output_file.close()
    analyze_algorithm_on_the_queue(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes_of_queue(terminated_queue, processes_analysis_output_file)
    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()


def SRTF_scheduling_algorithm(job_queue):
    create_directory("./output/SRTF")
    algorithm_procedure_output_file = create_file("./output/SRTF/", "SRTF - Scheduling Timeline Flow", ".log")
    algorithm_analysis_output_file = create_file("./output/SRTF/", "SRTF - Algorithm's Analysis", ".log")
    processes_analysis_output_file = create_file("./output/SRTF/", "SRTF - Job-Queue's Processes' Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)
    current_time = 0
    algorithm_procedure_output_file.write(
        "*** Shortest-Remaining-Time-First (SRTF) Scheduling Algorithm in Operating System "
        "***\n\n")

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))

        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            admit_report = admit(job_queue, ready_queue)
            algorithm_procedure_output_file.write(admit_report)
        if not is_empty(ready_queue) and running_process is None:
            running_process = remove_process_with_minimum_CPU_burst_time(ready_queue)
            dispatch_report = dispatch(running_process, current_time)
            algorithm_procedure_output_file.write(dispatch_report)
        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))

            if front(waiting_queue).IO_burst_time == 0:
                IO_comp_report = IO_completion(waiting_queue, ready_queue)
                algorithm_procedure_output_file.write(IO_comp_report)
        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second (Remaining Second CPU Burst Time = "
                        "{}).\n".format(
                            running_process.process_id, running_process.CPU_burst_time_2))
                    if running_process.CPU_burst_time_2 == 0:
                        terminate_report = terminate(running_process, terminated_queue, current_time)
                        algorithm_procedure_output_file.write(terminate_report)
                        running_process = None
                    else:
                        preempt_report = preempt(ready_queue, running_process)
                        running_process = None
                        algorithm_procedure_output_file.write(preempt_report)
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {})."
                    "\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))

                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    IO_req_report = IO_request(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(IO_req_report)
                else:
                    preempt_report = preempt(ready_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(preempt_report)

        current_time += 1

    algorithm_procedure_output_file.close()
    analyze_algorithm_on_the_queue(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes_of_queue(terminated_queue, processes_analysis_output_file)
    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()


def MLFQ_scheduling_algorithm(job_queue):
    create_directory("./output/MLFQ")
    algorithm_procedure_output_file = create_file("./output/MLFQ/", "MLFQ - Scheduling Timeline Flow", ".log")
    algorithm_analysis_output_file = create_file("./output/MLFQ/", "MLFQ - Algorithm's Analysis", ".log")
    processes_analysis_output_file = create_file("./output/MLFQ/", "MLFQ - Job-Queue's Processes' Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queues = []  # List to hold multiple queues
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)
    current_time = 0
    temp_elapsed_time = 0
    process_previous_running_level = 1

    algorithm_procedure_output_file.write(
        "*** Multi-Level-Feedback-Queue (MLFQ) Scheduling Algorithm in Operating System ***\n\n")

    # Ask user for the number of queues and quantum time for each queue
    num_queues = int(input("Enter the number of queues: "))
    quantum_times = []
    for i in range(num_queues):
        quantum_time = int(input("Enter the quantum time for Queue {}: ".format(i + 1)))
        quantum_times.append(quantum_time)
        ready_queues.append(Queue(job_queue.capacity))

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))
        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            admit_report = admit(job_queue, ready_queues[0])
            algorithm_procedure_output_file.write(admit_report)
        if not is_empty(ready_queues[0]) and running_process is None:
            running_process = dequeue(ready_queues[0])
            process_previous_running_level = 1
            temp_elapsed_time = 0
            dispatch_report = dispatch(running_process, current_time)
            algorithm_procedure_output_file.write(dispatch_report)
        else:
            for i in range(1, num_queues):
                if not is_empty(ready_queues[i]) and running_process is None:
                    running_process = dequeue(ready_queues[i])
                    process_previous_running_level = i + 1
                    temp_elapsed_time = 0
                    if running_process.response_time == -1:
                        running_process.response_time = current_time
                    algorithm_procedure_output_file.write(
                        "\tProcess-{} Moved From Ready-Queue Level {} to Running-State.\n".format(
                            running_process.process_id, i + 1))
                    break

        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))

            if front(waiting_queue).IO_burst_time == 0:
                enqueue(ready_queues[0], dequeue(waiting_queue))
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s IO's Waiting Time Was Finished and Was Moved From Waiting-Queue to Ready-Queue."
                    "\n".format(
                        rear(ready_queues[0]).process_id))

        if running_process is not None:
            queue_index = process_previous_running_level - 1  # Index of the queue from which process was dequeued
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    temp_elapsed_time += 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second "
                        "(Remaining Second CPU Burst Time = {}).\n".format(
                            running_process.process_id, running_process.CPU_burst_time_2))

                    if running_process.CPU_burst_time_2 == 0:
                        enqueue(terminated_queue, running_process)
                        running_process.termination_time = current_time + 1
                        running_process.turn_around_time = running_process.termination_time - (
                            running_process.arrival_time)
                        running_process.waiting_time = running_process.turn_around_time - (
                                running_process.CPU_burst_time_1 + running_process.IO_burst_time + (
                                    running_process.CPU_burst_time_2))
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Was Terminated (Moved From Running-State to Terminated-Queue).\n".format(
                                rear(terminated_queue).process_id))
                    elif temp_elapsed_time == quantum_times[queue_index]:
                        if queue_index + 1 < num_queues:
                            enqueue(ready_queues[queue_index + 1], running_process)
                            running_process = None
                            algorithm_procedure_output_file.write(
                                "\tProcess-{} Was Preempted (Moved From Running-State to Ready-Queue Level {})."
                                "\n".format(
                                    rear(ready_queues[queue_index + 1]).process_id, queue_index + 2))
                        else:
                            enqueue(ready_queues[queue_index], running_process)
                            running_process = None
                            algorithm_procedure_output_file.write(
                                "\tProcess-{} Time Slice Expired "
                                "(Moved From Running-State to the Same Ready-Queue Level).\n".format(
                                    rear(ready_queues[queue_index]).process_id))
            else:
                running_process.CPU_burst_time_1 -= 1
                temp_elapsed_time += 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {})."
                    "\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))

                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    enqueue(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(
                        "\tProcess-{} Moved From Running-State to Waiting-Queue to Execute Its IO Burst.\n".format(
                            rear(waiting_queue).process_id))
                elif temp_elapsed_time == quantum_times[queue_index]:
                    if queue_index + 1 < num_queues:
                        enqueue(ready_queues[queue_index + 1], running_process)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Was Preempted (Moved From Running-State to Ready-Queue Level {}).\n".format(
                                rear(ready_queues[queue_index + 1]).process_id, queue_index + 2))
                    else:
                        enqueue(ready_queues[queue_index], running_process)
                        running_process = None
                        algorithm_procedure_output_file.write(
                            "\tProcess-{} Time Slice Expired (Moved From Running-State to the Same Ready-Queue Level)."
                            "\n".format(
                                rear(ready_queues[queue_index]).process_id))

        current_time += 1

    algorithm_procedure_output_file.close()
    analyze_algorithm_on_the_queue(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes_of_queue(terminated_queue, processes_analysis_output_file)
    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()


def HRRN_scheduling_algorithm(job_queue):
    create_directory("./output/HRRN")
    algorithm_procedure_output_file = create_file("./output/HRRN/", "HRRN - Scheduling Timeline Flow", ".log")
    algorithm_analysis_output_file = create_file("./output/HRRN/", "HRRN - Algorithm's Analysis", ".log")
    processes_analysis_output_file = create_file("./output/HRRN/", "HRRN - Job-Queue's Processes' Analysis", ".log")

    job_queue_copy = copy_queue(job_queue)
    ready_queue = Queue(job_queue.capacity)
    running_process = None
    waiting_queue = Queue(job_queue.capacity)
    terminated_queue = Queue(job_queue.capacity)
    current_time = 0
    algorithm_procedure_output_file.write(
        "*** Highest-Response-Ratio-Next (HRRN) Scheduling Algorithm in Operating System ***\n\n")

    while not is_full(terminated_queue):
        algorithm_procedure_output_file.write("Time = {}-{}:\n".format(current_time, current_time + 1))
        if not is_empty(job_queue) and front(job_queue).arrival_time <= current_time:
            admit_report = admit(job_queue, ready_queue)
            algorithm_procedure_output_file.write(admit_report)
        if not is_empty(ready_queue) and running_process is None:
            running_process = remove_process_with_minimum_CPU_burst_time(ready_queue)
            dispatch_report = dispatch(running_process, current_time)
            algorithm_procedure_output_file.write(dispatch_report)
        if not is_empty(waiting_queue):
            front(waiting_queue).IO_burst_time -= 1
            algorithm_procedure_output_file.write(
                "\tProcess-{}'s Waited for I/O Resource for 1 Second (Remaining I/O Waiting Time = {}).\n".format(
                    front(waiting_queue).process_id, front(waiting_queue).IO_burst_time))
            if front(waiting_queue).IO_burst_time == 0:
                IO_comp_report = IO_completion(waiting_queue, ready_queue)
                algorithm_procedure_output_file.write(IO_comp_report)
        if running_process is not None:
            if running_process.CPU_burst_time_1 == 0:
                if running_process.IO_burst_time == 0 and running_process.CPU_burst_time_2 != 0:
                    running_process.CPU_burst_time_2 -= 1
                    algorithm_procedure_output_file.write(
                        "\tProcess-{}'s Second CPU Burst Was Executed for 1 Second "
                        "(Remaining Second CPU Burst Time = {}).\n".format(running_process.process_id,
                                                                           running_process.CPU_burst_time_2))
                    if running_process.CPU_burst_time_2 == 0:
                        terminate_report = terminate(running_process, terminated_queue, current_time)
                        running_process = None
                        algorithm_procedure_output_file.write(terminate_report)
            else:
                running_process.CPU_burst_time_1 -= 1
                algorithm_procedure_output_file.write(
                    "\tProcess-{}'s First CPU Burst Was Executed for 1 Second (Remaining First CPU Burst Time = {})."
                    "\n".format(
                        running_process.process_id, running_process.CPU_burst_time_1))
                if running_process.CPU_burst_time_1 == 0 and running_process.IO_burst_time != 0:
                    IO_req_report = IO_request(waiting_queue, running_process)
                    running_process = None
                    algorithm_procedure_output_file.write(IO_req_report)
        current_time += 1

    algorithm_procedure_output_file.close()
    analyze_algorithm_on_the_queue(job_queue_copy, terminated_queue, algorithm_analysis_output_file)
    analyze_processes_of_queue(terminated_queue, processes_analysis_output_file)
    algorithm_analysis_output_file.close()
    processes_analysis_output_file.close()
