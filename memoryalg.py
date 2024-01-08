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
        """Initializes memory values"""
        self.reference_values = [Page(base_id) for base_id in reference_string]

    def set_slots(self, slot_size: int):
        """Initializes slots in the memory list"""
        self.slots = [None for _ in range(slot_size)]

    def add_time_in_memory(self, val=1):
        """Increases pages time in the memory"""
        for slot in self.slots:
            if slot is not None:
                slot.time_in_memory += val


    def change_time_not_used(self, switched_page, val=1):
        '''Increases already existing pages time and sets it to 0 for recently switched ones'''
        for slot in self.slots:
            if slot is not None:
                if slot.equals(switched_page):
                    slot.time_not_used = 0
                else:
                    slot.time_not_used += val

    def if_value_exists(self, page: Page):
        '''Checks if the given page already exists in the memory list'''
        for value in self.slots:
            if value is not None and value.equals(page):
                return True
        return False


    def replace_page(self, new_page):
        '''Replaces the page in the memory with a new one'''
        # Initialize the variables to keep track of which page to replace
        index_to_replace = 0
        highest_time_not_used = -1 # -1 to ensure that any real time_not_used > -1

        # Iterate through each slot to find the page with the highest 'time_not_used' value
        for i, page in enumerate(self.slots):
            # Ensure the page slot is not empty and check if the current page has the highest 'time_not_used'
            if page is not None and (highest_time_not_used < page.time_not_used):
                # If it is the highest, mark this page to be replaced
                index_to_replace = i
                highest_time_not_used = page.time_not_used

        # Replace the page at the found index with the new page.
        self.slots[index_to_replace] = new_page


    def fifo(self):
        '''First in First out algorithm implementation'''

        longest_not_used_index = 0

        for page in self.reference_values:
            print(f"Adding page: {page}")

            # Check if the page already exists in the slots
            does_page_exist = self.if_value_exists(page)

            # If the page does not exist, increase the page fault counter, and add the page
            if not does_page_exist:
                # Replace the page at the index for the longest not used with the new page.
                self.slots[longest_not_used_index] = page
                # Update the index for the next longest not used page.
                longest_not_used_index = (longest_not_used_index + 1) % len(self.slots)
                # Increase the page fault counter.
                self.page_faults += 1
            self.add_time_in_memory()

            print(self.slots)
        print("Total page faults: ")
        return self.page_faults

    def lru(self):
        for page in self.reference_values:
            print(f"Adding page: {page}")
            # Check if the page already exists in the slots
            if not self.if_value_exists(page):
                # If it does not exist, increase the page fault counter
                self.page_faults += 1
                # Check if there is an empty slot to add the page (represented by None value)
                if None in self.slots:
                    # Find the index of the empty slot
                    empty_slot_index = self.slots.index(None)
                    # Place the page into the empty slot
                    self.slots[empty_slot_index] = page
                else:
                    # Replace the least recently used page if there are no empty spots.
                    self.replace_page(page)
            self.change_time_not_used(page)
            print(self.slots)
        print("Total page faults: ")
        return self.page_faults


