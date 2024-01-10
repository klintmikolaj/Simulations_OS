import random


def load_memory_data():
    """Creates random data list for FIFO/LRU/lFU algorithms containing lists as single int value"""

    print("-----------------------------------------")
    memory_data = []
    num_of_tests = int(input("Enter the number of tests: "))
    num_of_pages = int(input("Enter the number of pages: "))
    for i in range(num_of_tests):
        test_page = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=num_of_pages)
        memory_data.append(test_page)
    return memory_data


def load_specific_memory_data():
    # TEST 1
    # memory_data = [1, 2, 3, 4, 4, 3, 5, 6, 7, 1]

    # TEST 2
    # memory_data = [1, 4, 2, 1, 3, 4, 2, 4, 3, 1, 2, 2, 4, 3, 1, 4, 3, 2, 1, 4]

    # TEST 3.1/3.2 - tests vary in the number of slots
    memory_data = [3, 2, 1, 0, 3, 2, 4, 3, 2, 1, 0, 4]

    return memory_data
