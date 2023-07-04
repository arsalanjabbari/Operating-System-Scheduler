from Process import *
from Queue import *
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
            line_count = sum(1 for line in file)
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
            added_process = Process(process_id, arrival_time, CPU_burst_time_1, CPU_burst_time_2 ,IO_burst_time)
            enqueue(queue, added_process)

    create_directory("./output")

    return queue
