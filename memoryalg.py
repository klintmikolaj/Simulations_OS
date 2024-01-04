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


    def replace_page(self, new_page):  # find and replace page with highest time_not_used
        index_to_replace = 0
        highest_time_not_used = -1
        for i, page in enumerate(self.slots):
            if page is not None and (highest_time_not_used < page.time_not_used):
                index_to_replace = i
                highest_time_not_used = page.time_not_used
        # Replace the least recently used page with the new page
        self.slots[index_to_replace] = new_page


    def fifo(self):
        longest_not_used_index = 0  # Initialize a pointer to track the oldest page index
        for page in self.reference_values:
            does_page_exist = self.if_value_exists(page)
            if not does_page_exist:
                # Replace the oldest page with the new page
                self.slots[longest_not_used_index] = page

                # Move the oldest page pointer to the next index, wrapping around if necessary
                longest_not_used_index = (longest_not_used_index + 1) % len(self.slots)

                self.page_faults += 1
            self.add_time_in_memory()

            print(self.slots)
            # print(f'Page faults counter: {self.page_faults}')
        # info = dict(page_faults=self.page_faults)
        print("Total page faults: ")
        return self.page_faults

    def lru(self):
        for page in self.reference_values:
            print(f"Adding page: {page}")
            if not self.if_value_exists(page):
                self.page_faults += 1
                if None in self.slots:
                    # Find the first empty slot and add the page there
                    empty_slot_index = self.slots.index(None)
                    self.slots[empty_slot_index] = page
                else:
                    # No empty slots, replace the least recently used page
                    self.replace_page(page)
            # Update the time not used for all pages
            self.change_time_not_used(page)
            print(self.slots)
        print("Total page faults: ")
        return self.page_faults


