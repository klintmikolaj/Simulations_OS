import random


def load_random_data():
    """Creates random data list for FCFS/SJF algorithms containing processes as double-value list"""

    num_of_tests = int(input("Enter the number of tests: "))
    num_of_processes = int(input("Enter the number of processes: "))
    random_data = []

    # Create certain number of lists containing processes as double-value lists
    for _ in range(num_of_tests):
        processes_data = []
        for _ in range(num_of_processes):
            # Add weights to ensure that more processes start earlier and have shorter execution times
            process_start_time = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=1)[0]
            process_execution_time = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=1)[0]
            process = [process_start_time, process_execution_time]
            processes_data.append(process)
        random_data.append(processes_data)

    return random_data


def generate_processes(num_of_processes, max_start, max_execution):
    """Generates the list of processes of size given by num_of_processes"""

    processes = []
    for _ in range(num_of_processes):
        start_time = random.randint(0, max_start)
        execution_time = random.randint(0, max_execution)
        processes.append([start_time, execution_time])
    return processes


def load_specific__processor_data():
    # Test 1
    specific_data = [[0, 3], [2, 6], [4, 4], [6, 5], [8, 2]]

    # Test 2
    # specific_data = [[1, 9], [1, 7], [1, 3], [1, 5], [1, 1]]

    # Test 3
    # specific_data = [[0, 10], [1, 3], [3, 3], [5, 1], [5, 11]]

    # Test 4
    # specific_data = [[0, 1], [1, 2], [1, 2], [2, 1], [3, 3], [0, 1], [1, 2], [4, 2], [5, 3], [3, 3], [5, 2], [2, 2], [3, 2], [1, 1], [0, 1], [7, 3], [8, 1], [1, 1], [11, 2], [13, 3]]

    # Test 5.1 Done by generate_processes(25, 30, 30)
    # specific_data = [[26, 17], [4, 11], [21, 27], [1, 29], [0, 13], [22, 27], [13, 11], [13, 11], [1, 21], [13, 28], [19, 21], [2, 5], [0, 5], [16, 21], [7, 23], [17, 16], [30, 5], [0, 23], [6, 6], [7, 30], [19, 26], [24, 22], [12, 23], [4, 16], [23, 0]]

    # Test 5.2 Done by generate_processes(50, 30, 30)
    # specific_data = [[22, 0], [27, 20], [2, 11], [0, 0], [14, 12], [29, 17], [3, 1], [28, 7], [16, 3], [3, 29], [7, 30], [9, 12], [7, 26], [28, 12], [26, 12], [13, 16], [10, 13], [22, 8], [15, 12], [13, 7], [27, 14], [2, 21], [18, 22], [15, 29], [13, 8], [9, 19], [10, 21], [2, 22], [18, 24], [4, 0], [3, 2], [1, 6], [27, 2], [13, 19], [25, 5], [28, 27], [23, 26], [26, 23], [5, 12], [13, 14], [21, 30], [29, 16], [12, 9], [27, 22], [27, 30], [23, 16], [18, 10], [24, 26], [23, 2], [14, 26]]

    # Test 5.3 Done by generate_processes(100, 30, 30)
    # specific_data = [[21, 27], [19, 21], [30, 3], [17, 15], [8, 23], [10, 22], [16, 2], [21, 0], [27, 23], [27, 26], [14, 4], [21, 28], [4, 7], [10, 7], [12, 26], [2, 22], [10, 28], [3, 29], [9, 10], [21, 28], [22, 3], [26, 22], [15, 15], [0, 15], [21, 25], [1, 12], [23, 1], [10, 24], [23, 17], [3, 29], [8, 22], [25, 26], [11, 13], [21, 27], [2, 23], [28, 14], [1, 21], [29, 13], [2, 29], [2, 24], [2, 19], [3, 5], [22, 13], [13, 9], [16, 7], [13, 22], [28, 27], [15, 10], [19, 13], [15, 13], [9, 7], [7, 12], [30, 19], [25, 13], [8, 26], [19, 25], [19, 0], [24, 23], [3, 27], [24, 7], [25, 27], [9, 19], [8, 7], [18, 22], [25, 25], [29, 4], [29, 4], [23, 17], [11, 23], [10, 9], [14, 2], [27, 4], [5, 24], [20, 6], [13, 21], [10, 0], [26, 19], [27, 3], [21, 0], [10, 10], [15, 6], [5, 22], [11, 17], [29, 8], [10, 16], [0, 25], [12, 21], [14, 21], [18, 13], [24, 2], [24, 6], [30, 1], [2, 1], [16, 24], [0, 5], [26, 18], [23, 3], [9, 6], [8, 16], [1, 9]]

    return specific_data
