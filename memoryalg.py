import colorama
import input_memory
from input_memory import data
class Page:


    def __init__(self, base_id):
        self.id = base_id
        self.time_in_memory = 0
        self.time_not_used = 0

    def __repr__(self):
        RED = '\033[91m'
        WHITE = '\033[97m'
        RESET = '\033[0m'
        # info = f"Page id: {self.id} | Time in memory: {self.time_in_memory} | Time not used: {self.time_not_used}"
        info = f"Page id: {RED} {self.id} {RESET}| Time in memory: {self.time_in_memory}"
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
            if slot != switched_page and slot is not None:
                slot.time_in_memory += val
            elif slot == switched_page:
                slot.time_in_memory = val

    def if_value_exists(self, page: Page):
        for value in self.slots:
            if value is not None and value.equals(page):
                return True
        return False



    def fifo(self):
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
        return self.page_faults


# size = 3
# values1 = [1, 3, 0, 3, 5, 6, 3]
# values2 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
# test = MemoryAlg()
# test.set_reference_values(values1)
# test.set_slots(size)
# print(test.slots)
# print(test.reference_values)
# print(test.fifo())


print(data)
for i in range(1, len(data) + 1):
    print(f"Test number {i}:")
    pages_list = []
    test = data[i-1]
    for base_id in test:
        pages_list.append(base_id)
    print(f'Pages list: {pages_list}')
    alg = MemoryAlg()
    alg.set_reference_values(pages_list)
    alg.set_slots(input_memory.num_of_slots)
    print(alg.fifo())






