import colorama
import time
import input_memory
from input_memory import memory_data
class Page:


    def __init__(self, base_id):
        self.id = base_id
        self.time_in_memory = 0
        self.time_not_used = 0

    def __repr__(self):
        RED = '\033[91m'
        RESET = '\033[0m'
        # info = f"Page id: {RED} {self.id} {RESET} | Time in memory: {self.time_in_memory} | Time not used: {self.time_not_used}"
        # info = f"Page id: {RED} {self.id} {RESET}| Time in memory: {self.time_in_memory}"
        info = f" {RED} {self.id} {RESET}"
        return info

    def __str__(self):
        return self.__repr__()

    def equals(self, obj_page):
        return self.id == obj_page.id and obj_page is not None

class MemoryAlg:
    def __init__(self):
        self.slots: list[None or Page] = []
        self.reference_values: list[Page] = []
        self.page_faults = 0
        self.execution_time = 0

    def set_reference_values(self, reference_string):
        self.reference_values = [Page(base_id) for base_id in reference_string]

    def set_slots(self, slot_size: int):
        self.slots = [None for _ in range(slot_size)]

    def add_time_in_memory(self, val=1):
        for slot in self.slots:
            if slot is not None:
                slot.time_in_memory += val


    def change_time_not_used(self, switched_page, val=1):
        for slot in self.slots:
            if slot is not None:
                if slot.equals(switched_page):
                    slot.time_not_used = 0
                else:
                    slot.time_not_used += val

    def if_value_exists(self, page: Page):
        for value in self.slots:
            if value is not None and value.equals(page):
                return True
        return False

    def replace_page(self): #find and replace page with highest time_not_used
        index_to_replace = 0
        time_not_used = -1
        for i, page in enumerate(self.slots):
            if page is not None and (time_not_used < page.time_not_used):
                index_to_replace = i
                time_not_used = page.time_not_used
        if index_to_replace is not None:
            self.slots[index_to_replace] = None

    def fifo(self):
        # start_clock = time.time()
        for page in self.reference_values:
            does_page_exist = self.if_value_exists(page)
            if not does_page_exist:
                if None in self.slots:
                    empty_slot_index = self.slots.index(None)
                    self.slots[empty_slot_index] = page
                else:
                    self.slots.pop(0)
                    self.slots.append(page)
                self.page_faults += 1
            self.add_time_in_memory()

            print(self.slots)
            print(self.page_faults)
        # self.execution_time = time.time() - start_clock
        info = dict(
                    execution_time=self.execution_time,
                    page_faults=self.page_faults)
        return info

    def lru(self):
        for page in self.reference_values:
            print(f"Adding page: {page}")
            if not self.if_value_exists(page):
                self.page_faults += 1
                if None in self.slots:
                    empty_slot_index = self.slots.index(None)
                    self.slots[empty_slot_index] = page
                else:
                    self.replace_page()
                    for i in range(len(self.slots)):
                        if self.slots[i] is None:
                            self.slots[i] = page
                            break
            print(self.slots)
            self.change_time_not_used(page)

        return self.page_faults






# size = 4
# values1 = [1, 3, 0, 3, 5, 6, 3]
# values2 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
# test = MemoryAlg()
# test.set_reference_values(values2)
# test.set_slots(size)
# print(test.slots)
# print(test.reference_values)
# print(test.fifo())


print(memory_data)
for i in range(1, len(memory_data) + 1):
    print(f"Test number {i}:")
    pages_list = []
    test = memory_data[i-1]
    for base_id in test:
        pages_list.append(base_id)
    print(f'Pages list: {pages_list}')
    alg = MemoryAlg()
    alg.set_reference_values(pages_list)
    alg.set_slots(input_memory.num_of_slots)
    print(alg.fifo())






