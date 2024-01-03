import random

num_of_tests = int(input("Enter the number of tests: "))
num_of_processes = int(input("Enter the number of processes: "))


p1 = [0, 5]
p2 = [1, 2]
p3 = [1, 5]
p4 = [6, 2]
p5 = [8, 1]
processes_data = [p1, p2, p3, p4, p5]
# def load_processes_data(tests_amount: int, processes_amount: int):
#     for i in range(tests_amount):
#         process = random.choices(range(1, 126), weights=[90 if x < 50 else 10 for x in range(1, 126)], k=processes_amount)
#         processes_data.append(process)
#
#
# load_processes_data(num_of_tests, num_of_processes)
# print(processes_data)
