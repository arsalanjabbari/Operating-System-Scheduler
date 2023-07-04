from Process import Process
from Queue import Queue
import os

# create a new file in a given directory with given name and given extension
def create_file(path, name, extension):
    file_path = os.path.join(path, name + extension)
    file = open(file_path, "w")
    return file

# create a directory if it doesn't exist already with given name in given path
def create_directory(path):
    os.makedirs(path, exist_ok=True)


def count_lines_in_CSV_file(path):
    try:
        with open(path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{path}' not found.")


# Read input Processes from CSV File and return a queue of processes to be scheduled
def read_processes_from_CSV_file(path):
    with open(path, "r") as CSV_file:
        CSV_file.readline()  # skip the header line

        queue = Queue(count_lines_in_CSV_file(path))
        for line in CSV_file:
            process_id, arrival_time, CPU_burst_time_1, IO_burst_time, CPU_burst_time_2 = map(int, line.strip().split(","))
            process = Process(process_id, arrival_time, CPU_burst_time_1, CPU_burst_time_2 ,IO_burst_time)
            Queue.enqueue(queue, process)

    create_directory("./output")

    return queue
