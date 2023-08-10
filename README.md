# Operating-System-Scheduler

The **Operating-System-Scheduler** repository hosts an advanced project that offers a comprehensive simulation and in-depth analysis of processor timing using various algorithms commonly employed in operating systems. This project delves into the heart of scheduling methodologies, providing users with a deep understanding of how different algorithms impact system performance metrics.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

## Introduction

The **Operating-System-Scheduler** project adopts a scholarly approach to modern operating systems' process scheduling efficiency, providing a comprehensive platform for simulating and analyzing the interplay between processes and scheduling algorithms. Split into two phases, the project first facilitates process emulation to study diverse process behaviors and characteristics. In its second phase, it conducts a meticulous analysis of simulation outcomes, offering insights into scheduling algorithm performance under varying conditions. This project thus presents a valuable opportunity to enhance our understanding of process scheduling optimization and its implications in contemporary computing environments.

## Project Overview
The project is divided into two main phases:

### Phase 1: Simulation
In this phase, we simulate the behavior of different scheduling algorithms using the provided `input.csv` file. The simulation generates detailed analysis of algorithm performance and individual process metrics. The simulation output is organized within the `output` directory as follows:
```
- /output
  - /{Algorithm-Name}
    - Scheduling-Timeline-Flow.log
```
Scheduling timeline flow, including Gantt charts.
### Phase 2: Analysis
In the second phase, we analyze the data generated in Phase 1. We delve into various aspects of algorithm performance, such as CPU execution time, idle time, utilization, throughput, average turnaround time, average waiting time, and average response time. Additionally, individual process metrics such as arrival time, termination time, response time, turnaround time, and waiting time are analyzed.
``` 
- /output
  - /{Algorithm-Name}
    - Algorithm-Analysis.log
    - Process-Analysis.log
```
Analysis of the algorithm's performance metrics and individual process analysis.
```
output
├── FCFS
│   ├── FCFS-Algorithm-Analysis.log
│   ├── FCFS-Process-Analysis.log
│   └── FCFS-Scheduling-Timeline-Flow.log
├── HRRN
├── MLFQ
├── RR
├── SPN
└── SRTF
```
The project includes the following components:
- `input.csv`: Contains details of processes for analysis and simulation.
- `Process.py`: Defines the Process class to represent individual processes.
- `Queue.py`: Implements the Queue class for managing process queues.
- `Algorithm_Analyze.py`: Analyzes the performance of scheduling algorithms.
- `Process_Analyze.py`: Analyzes individual process performance.
- `Scheduler.py`: Contains the implementations of scheduling algorithms.
- `Scheduler_Utils.py`: Provides utility functions for the scheduler.
- `output`: Directory where simulation outputs are stored based on algorithms used.


Additionally, the project features a GUI with a user interface that prompts users to select the desired scheduling algorithm and customize parameters like the number of queues and size of each queue in the MLFQ algorithm. It also prompts for the time quantum in the RR algorithm. The implementation is designed to be fault-tolerant.

## Features
- Simulate and analyze processor timing using various scheduling algorithms.
- Detailed analysis of algorithm performance, including CPU execution time, idle time, utilization, throughput, average turnaround time, average waiting time, and average response time.
- Individual process analysis with metrics like arrival time, termination time, response time, turnaround time, and waiting time.
- GUI with user-friendly interface for selecting algorithms and customizing parameters.
- Fault-tolerant implementation to handle unexpected scenarios.

## Getting Started
1. Clone this repository.
2. Ensure you have Python installed (version 3.0 or higher).
3. Install any necessary dependencies by running: `pip install -r requirements.txt` (if applicable).
4. Run the application: `python3 main.py`.
5. Follow the prompts to choose the algorithm and provide necessary inputs.

## Conclusion
The Operating-System-Scheduler project offers valuable insights into the behavior of different scheduling algorithms on processor timing. By simulating and analyzing these algorithms, users can better understand their impact on system performance. The GUI provides an interactive experience for experimenting with various settings and exploring the outcomes.
