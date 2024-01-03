import random

num_of_tests = int(input("Enter the number of tests: "))
num_of_processes = int(input("Enter the number of processes: "))

data = []
for i in range(num_of_tests):
    process = random.choices(range(1, 100), k=num_of_processes)
    data.append(process)
# print(data)