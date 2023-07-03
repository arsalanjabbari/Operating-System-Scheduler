from Process import Process

# Queue class
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity - 1
        self.array = [None] * capacity

def create_new_queue(capacity):
    queue = Queue(capacity)
    return queue

def is_full(queue):
    return queue.size == queue.capacity

def is_empty(queue):
    return queue.size == 0

def enqueue(queue, process):
    if is_full(queue):
        return

    queue.rear = (queue.rear + 1) % queue.capacity
    queue.array[queue.rear] = process
    queue.size += 1

def dequeue(queue):
    if is_empty(queue):
        return None

    process = queue.array[queue.front]
    queue.front = (queue.front + 1) % queue.capacity
    queue.size -= 1
    return process

def front(queue):
    if is_empty(queue):
        return None

    return queue.array[queue.front]

def rear(queue):
    if is_empty(queue):
        return None

    return queue.array[queue.rear]

def sort_queue(queue):
    for i in range(queue.size - 1):
        for j in range(queue.size - i - 1):
            if queue.array[j].arrival_time > queue.array[j + 1].arrival_time:
                queue.array[j], queue.array[j + 1] = queue.array[j + 1], queue.array[j]

def print_queue(queue):
    print("\nProcesses in the queue:")
    for i in range(queue.size):
        Process.print_process(queue.array[i])

def copy_queue(queue):
    new_queue = create_new_queue(queue.capacity)
    for i in range(queue.size):
        enqueue(new_queue, Process.copy_process(queue.array[i]))
    return new_queue

def get_process_from_queue(process, queue):
    for i in range(queue.size):
        if queue.array[i].process_id == process.process_id:
            return queue.array[i]
    return None

def remove_process(queue, process):
    for i in range(queue.size):
        if queue.array[i] == process:
            for j in range(i, queue.size - 1):
                queue.array[j] = queue.array[j + 1]
            queue.size -= 1
            break
    queue.rear -= 1

def get_process_with_minimum_CPU_burst_time(queue):
    process = queue.array[0]
    for i in range(1, queue.size):
        if ((process.CPU_burst_time_1 != 0 and queue.array[i].CPU_burst_time_1 != 0 and
             queue.array[i].CPU_burst_time_1 < process.CPU_burst_time_1) or
            (process.CPU_burst_time_1 == 0 and queue.array[i].CPU_burst_time_1 != 0 and
             queue.array[i].CPU_burst_time_1 < process.CPU_burst_time_2) or
            (process.CPU_burst_time_1 != 0 and queue.array[i].CPU_burst_time_1 == 0 and
             queue.array[i].CPU_burst_time_2 < process.CPU_burst_time_1) or
            (process.CPU_burst_time_1 == 0 and queue.array[i].CPU_burst_time_1 == 0 and
             queue.array[i].CPU_burst_time_2 < process.CPU_burst_time_2)):

            process = queue.array[i]
    return process

def remove_process_with_minimum_CPU_burst_time(queue):
    process = get_process_with_minimum_CPU_burst_time(queue)
    remove_process(queue, process)
    return process
