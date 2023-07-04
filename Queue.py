from Process import Process as process

class Queue:

    def __init__(self, capacity):
        self.size = -1
        self.capacity = capacity
        self.front = 0
        self.size = 0
        self.rear = capacity - 1
        self.array = []

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, enqueuing_process):
        if Queue.is_full(self):
            return None

        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = enqueuing_process
        self.size += 1

    def dequeue(self):
        if Queue.is_empty(self):
            return None

        dequeued_process = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return dequeued_process

    def front(self):
        if Queue.is_empty(self):
            return None

        return self.array[self.front]

    def rear(self):
        if Queue.is_empty(self):
            return None

        return self.array[self.rear]

    # Sort on Arrival time
    def sort_queue_at(self):
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                if self.array[j].arrival_time > self.array[j + 1].arrival_time:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

    def print_queue(self):
        print("\nProcesses in the queue:")
        for i in range(self.size):
            process.print_process(self.array[i])

    def copy_queue(self):
        new_queue = Queue(self.capacity)
        for i in range(self.size):
            Queue.enqueue(new_queue, process.copy_process(self.array[i]))
        return new_queue

    def get_process_from_queue(self, selected_process):
        for i in range(self.size):
            if self.array[i].process_id == selected_process.process_id:
                return self.array[i]
        return None

    def remove_process(self, selected_process):
        for i in range(self.size):
            if self.array[i] == selected_process:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                break
        self.rear -= 1

    def get_process_with_minimum_CPU_burst_time(self):
        wanted_process = self.array[0]
        for i in range(1, self.size):
            if ((wanted_process.CPU_burst_time_1 != 0 and self.array[i].CPU_burst_time_1 != 0 and
                 self.array[i].CPU_burst_time_1 < wanted_process.CPU_burst_time_1) or
                (wanted_process.CPU_burst_time_1 == 0 and self.array[i].CPU_burst_time_1 != 0 and
                 self.array[i].CPU_burst_time_1 < wanted_process.CPU_burst_time_2) or
                (wanted_process.CPU_burst_time_1 != 0 and self.array[i].CPU_burst_time_1 == 0 and
                 self.array[i].CPU_burst_time_2 < wanted_process.CPU_burst_time_1) or
                (wanted_process.CPU_burst_time_1 == 0 and self.array[i].CPU_burst_time_1 == 0 and
                 self.array[i].CPU_burst_time_2 < wanted_process.CPU_burst_time_2)):


                wanted_process = self.array[i]
        return wanted_process

    def remove_process_with_minimum_CPU_burst_time(self):
        wanted_process = Queue.get_process_with_minimum_CPU_burst_time(self)
        Queue.remove_process(self, wanted_process)
        return wanted_process
