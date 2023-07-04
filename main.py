from Test_Section import *
from Scheduler import *
from Queue import *

def main():
    job_queue = read_processes_from_CSV_file("csv.csv")
    sort_queue_at(job_queue)
    FCFS_scheduling_algorithm(copy_queue(job_queue))
    RR_scheduling_algorithm(copy_queue(job_queue))
    # SJF_scheduling_algorithm(job_queue.copy())
    # SRTF_scheduling_algorithm(job_queue.copy())
    # MLFQ_scheduling_algorithm(job_queue.copy())

if __name__ == "__main__":
    main()
