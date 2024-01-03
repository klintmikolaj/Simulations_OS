import random
num_of_tests = int(input("Enter the number of tests: "))
num_of_slots = int(input("Enter the number of slots: "))
num_of_pages = int(input("Enter the number of pages: "))

data = []
for i in range(num_of_tests):
    page = random.choices(range(1, 10), k=num_of_pages)
    data.append(page)
#print(data)