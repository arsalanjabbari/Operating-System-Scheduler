from Test_Section import *
from Scheduler import *
from Queue import *

def main():
    job_queue = read_processes_from_CSV_file("csv.csv")
    job_queue.sort_queue_at()

    FCFS_scheduling_algorithm(job_queue.copy_queue())
    # RR_scheduling_algorithm(job_queue.copy())
    # SJF_scheduling_algorithm(job_queue.copy())
    # SRTF_scheduling_algorithm(job_queue.copy())
    # MLFQ_scheduling_algorithm(job_queue.copy())

if __name__ == "__main__":
    main()
