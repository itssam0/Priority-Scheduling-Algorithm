# Priority-Scheduling-Algorithm
This repository contains an implementation of the Priority Scheduling algorithm in Python. Priority Scheduling is a widely used CPU scheduling algorithm where each process is assigned a priority, and the process with the highest priority is executed first. The repository includes the algorithm's source code, examples of its execution, and a detailed explanation of its advantages and disadvantages.

## Overview
The Priority Scheduling algorithm is a type of CPU scheduling used in operating systems where each process is assigned a priority. The scheduler selects the process with the highest priority (numerically lowest) to execute next. This can be either preemptive or non-preemptive depending on the implementation. It is commonly used in systems where some tasks are more critical than others.

## How It Works
- **Priority Assignment:** Each process is assigned a priority. The process with the highest priority (lowest numerical value) is selected for execution first.
- **Preemptive vs Non-Preemptive:** 
  - **Preemptive:** If a new process arrives with a higher priority than the currently running process, the CPU is preempted, and the new process is executed.
  - **Non-Preemptive:** The current process runs to completion, even if a new process with a higher priority arrives.
- **Flexibility:** The priority of a process can be static or dynamic, allowing the system to adjust priorities based on certain criteria (e.g., aging).

## Advantages
- **Efficiency for Critical Tasks:** High-priority tasks are executed first, which is ideal for time-sensitive applications.
- **Flexibility:** The ability to adjust priorities dynamically makes this algorithm adaptable to different types of workloads.
- **Effective in Real-Time Systems:** Priority Scheduling is particularly useful in real-time systems where certain tasks must be completed within strict time constraints.

## Disadvantages
- **Inversion of Priority:** A situation where a lower-priority process holds a resource needed by a higher-priority process, causing the latter to wait indefinitely, leading to a potential system deadlock.
- **Starvation:** Low-priority processes may suffer from starvation, as they might never get executed if higher-priority processes keep entering the queue.
- **Complexity:** Managing and adjusting priorities can add complexity to the system, especially in dynamic priority scenarios.

## Usage
To run the Priority Scheduling simulation, clone the repository and execute the Python script:

```bash
git clone https://github.com/yourusername/priority-scheduling.git
cd priority-scheduling
python priority_scheduling.py
