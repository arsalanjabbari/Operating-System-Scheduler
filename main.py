from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Scheduler_Utils import *
from Scheduler import *
from Queue import *

job_queue = None  # Global variable to hold the job queue

def run_algorithm(algorithm_name):
    if job_queue is None:
        messagebox.showwarning("Warning", "Please browse a CSV file before running the algorithm.")
    else:
        if algorithm_name == "FCFS":
            FCFS_scheduling_algorithm(copy_queue(job_queue))
        elif algorithm_name == "RR":
            RR_scheduling_algorithm(copy_queue(job_queue))
        elif algorithm_name == "SPN":
            SPN_scheduling_algorithm(copy_queue(job_queue))
        elif algorithm_name == "SRTF":
            SRTF_scheduling_algorithm(copy_queue(job_queue))
        elif algorithm_name == "MLFQ":
            MLFQ_scheduling_algorithm(copy_queue(job_queue))
        elif algorithm_name == "HRRN":
            HRRN_scheduling_algorithm(copy_queue(job_queue))

        messagebox.showinfo("Success", "Algorithm '{}' completed successfully; You can see results in "
                                       "./output/{}.".format(algorithm_name, algorithm_name))

def main():
    def on_algorithm_selected():
        algorithm_name = algorithm_var.get()
        run_algorithm(algorithm_name)

    def browse_file():
        filename = filedialog.askopenfilename(initialdir=".", title="Select CSV file")
        if filename:
            if filename.endswith('.csv'):
                global job_queue  # Declare job_queue as global
                job_queue = read_processes_from_CSV_file_make_them_queue(filename)
                sort_queue_at(job_queue)
                status_label.config(text="Selected file: " + filename)  # Update the status label
            else:
                messagebox.showwarning("Warning", "Please select a CSV file.")
        else:
            messagebox.showwarning("Warning", "No file selected.")

    root = Tk()
    root.title("Operating System Scheduling via Related Algorithms")
    root.geometry("400x300")  # Set the window size

    # Create a frame for the content
    content_frame = Frame(root)
    content_frame.pack(pady=20)

    algorithm_label = Label(content_frame, text="Select Algorithm:", font=("Arial", 12))
    algorithm_label.pack()

    algorithm_var = StringVar(content_frame)
    algorithm_var.set("FCFS")  # Default algorithm

    algorithm_menu = OptionMenu(content_frame, algorithm_var, "FCFS", "RR", "SPN", "SRTF", "MLFQ", "HRRN")
    algorithm_menu.config(font=("Arial", 12))
    algorithm_menu.pack()

    browse_button = Button(content_frame, text="Browse CSV", command=browse_file, font=("Arial", 12))
    browse_button.pack(pady=10)

    status_label = Label(content_frame, text="Selected file: None", font=("Arial", 12))
    status_label.pack()

    run_button = Button(content_frame, text="Run Algorithm", command=on_algorithm_selected, font=("Arial", 12))
    run_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()