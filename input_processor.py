import random


def load_random_data():
    '''Creates random data list for FCFS/SJF algorithms containing processes as double-value list'''
    num_of_tests = int(input("Enter the number of tests: "))
    num_of_processes = int(input("Enter the number of processes: "))
    random_data = []

    for _ in range(num_of_tests):
        processes_data = []
        for _ in range(num_of_processes):
            process_start_time = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=1)[0]
            process_execution_time = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=1)[0]
            process = [process_start_time, process_execution_time]
            processes_data.append(process)
        random_data.append(processes_data)

    return random_data


def load_specific__processor_data():
    points = {
        'p1': [0, 1], 'p11': [5, 2],
        'p2': [1, 2], 'p12': [2, 2],
        'p3': [1, 2], 'p13': [3, 2],
        'p4': [2, 1], 'p14': [1, 1],
        'p5': [3, 3], 'p15': [0, 1],
        'p6': [0, 1], 'p16': [7, 3],
        'p7': [1, 2], 'p17': [8, 1],
        'p8': [4, 2], 'p18': [1, 1],
        'p9': [5, 3], 'p19': [11, 2],
        'p10': [3, 3], 'p20': [13, 3]
    }
    specific_data = [points[f"p{i}"] for i in range(1, 21)]
    print(specific_data)
    return specific_data

