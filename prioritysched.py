import time

# Processes with their priorities and burst times
processes = [{'id': 'P1', 'priority': 2, 'burst': 10},
             {'id': 'P2', 'priority': 1, 'burst': 4},
             {'id': 'P3', 'priority': 3, 'burst': 6}]

# Function to simulate priority scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: x['priority'])
    time_passed = 0
    turnaround_times = {}
    response_times = {}
    first_response = {}

    for process in processes:
        print(f"Process {process['id']} starts at time {time_passed}")
        response_times[process['id']] = time_passed
        if process['id'] not in first_response:
            first_response[process['id']] = time_passed
        time_passed += process['burst']
        turnaround_times[process['id']] = time_passed
        print(f"Process {process['id']} finishes at time {time_passed}")
        time.sleep(process['burst'] * 0.1)

    avg_turnaround_time = sum(turnaround_times.values()) / len(turnaround_times)
    avg_response_time = sum(response_times.values()) / len(response_times)
    
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"Average response time: {avg_response_time}")

priority_scheduling(processes)