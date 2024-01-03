import random
num_of_tests = int(input("Enter the number of tests: "))
num_of_slots = int(input("Enter the number of slots: "))
num_of_pages = int(input("Enter the number of pages: "))

memory_data = []

def load_memory_data(tests_amount: int, pages_amount: int):
    for i in range(tests_amount):
        test_page = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=pages_amount)
        memory_data.append(test_page)
# for i in range(num_of_tests):
#     page = random.choices(range(1, 10), k=num_of_pages)
#     data.append(page)
load_memory_data(num_of_tests, num_of_pages)
print(memory_data)