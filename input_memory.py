import random
def load_memory_data():
    print("-----------------------------------------")
    memory_data = []
    num_of_tests = int(input("Enter the number of tests: "))
    num_of_pages = int(input("Enter the number of pages: "))
    for i in range(num_of_tests):
        test_page = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=num_of_pages)
        memory_data.append(test_page)
    return memory_data
