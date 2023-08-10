# Operating-System-Scheduler

## Description
This repository contains a project that simulates and analyzes the process of processor timing using different algorithms in an operating system.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

## Introduction
In this project, we aim to simulate and analyze the process of processor timing through various algorithms employed in operating systems. The primary goal is to understand how different scheduling algorithms impact the performance metrics of a system.

## Project Overview
The project includes the following components:
- `input.csv`: Contains details of processes for analysis and simulation.
- `Process.py`: Defines the Process class to represent individual processes.
- `Queue.py`: Implements the Queue class for managing process queues.
- `Algorithm_Analyze.py`: Analyzes the performance of scheduling algorithms.
- `Process_Analyze.py`: Analyzes individual process performance.
- `Scheduler.py`: Contains the implementations of scheduling algorithms.
- `Scheduler_Utils.py`: Provides utility functions for the scheduler.
- `output`: Directory where simulation outputs are stored based on algorithms used.

The simulation outputs are organized within the `output` directory, with subdirectories for each algorithm containing analysis logs and scheduling timeline flow logs, including Gantt charts depicting processor execution.

Additionally, the project features a GUI with a user interface that prompts users to select the desired scheduling algorithm and customize parameters like the number of queues and size of each queue in the MLFQ algorithm. It also prompts for the time quantum in the RR algorithm. The implementation is designed to be fault-tolerant.

## Features
- Simulate and analyze processor timing using various scheduling algorithms.
- Detailed analysis of algorithm performance, including CPU execution time, idle time, utilization, throughput, average turnaround time, average waiting time, and average response time.
- Individual process analysis with metrics like arrival time, termination time, response time, turnaround time, and waiting time.
- GUI with user-friendly interface for selecting algorithms and customizing parameters.
- Fault-tolerant implementation to handle unexpected scenarios.

## Getting Started
1. Clone this repository.
2. Ensure you have Python installed (version X.Y or higher).
3. Install any necessary dependencies by running: `pip install -r requirements.txt` (if applicable).
4. Run the GUI application: `python GUI.py`.
5. Follow the prompts to choose the algorithm and provide necessary inputs.

## Conclusion
The Operating-System-Scheduler project offers valuable insights into the behavior of different scheduling algorithms on processor timing. By simulating and analyzing these algorithms, users can better understand their impact on system performance. The GUI provides an interactive experience for experimenting with various settings and exploring the outcomes.
