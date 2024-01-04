import random


def load_random_data():
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


def load_specific_data():
    p1 = [0, 5]
    p2 = [1, 2]
    p3 = [1, 5]
    p4 = [6, 2]
    p5 = [8, 1]
    specific_data = [p1, p2, p3, p4, p5]
    return specific_data
