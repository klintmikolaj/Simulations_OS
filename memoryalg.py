class Page:
    """Class imitating a single page in FIFO/LRU/LFU algorithms"""

    def __init__(self, base_id):
        self.id = base_id
        self.time_in_memory = 0
        self.time_not_used = 0
        self.reference_count = 0

        # Colors variables definition
        self.RED = '\033[91m'
        self.RESET = '\033[0m'

    def __repr__(self):
        # Displays information about a page
        info = f" {self.RED} {self.id} {self.RESET}"

        # info = f"Page id: {RED} {self.id} {RESET} | Time in memory: {self.time_in_memory} | Time not used: {
        # self.time_not_used}" info = f"Page id: {RED} {self.id} {RESET}| Time in memory: {self.time_in_memory}"
        return info

    def __str__(self):
        return self.__repr__()

    def equals(self, obj_page):
        """Checks if the page is already in the list"""
        return self.id == obj_page.id and obj_page is not None


class MemoryAlg:
    """Class used for manipulating data using FIFO/LRU/LFU algorithms"""

    def __init__(self):
        # Create a list of None or Page objects
        self.slots: list[None or Page] = []
        # Create a list of Page objects
        self.pages_values: list[Page] = []
        self.page_faults = 0
        self.execution_time = 0

    def set_reference_values(self, input_pages):
        """Initialize memory values"""

        self.pages_values = [Page(base_id) for base_id in input_pages]

    def set_slots(self, slot_size: int):
        """Initialize slots in the memory list represented by a None value"""

        self.slots = [None for _ in range(slot_size)]

    def add_time_in_memory(self, val=1):
        """Increase pages time in the memory"""

        for slot in self.slots:
            if slot is not None:
                slot.time_in_memory += val

    def change_time_not_used(self, switched_page, val=1):
        """Increase time of pages already in memory and sets it to 0 for recently switched ones"""

        for slot in self.slots:
            if slot is not None:
                if slot.equals(switched_page):
                    slot.time_not_used = 0
                else:
                    slot.time_not_used += val

    def if_value_exists(self, page: Page):
        """Checks if the given page already exists in the memory list"""

        for value in self.slots:
            if value is not None and value.equals(page):
                return True
        return False

    def increase_reference_count(self, page):
        """Increases the reference count for a certain page"""

        for slot in self.slots:
            if slot is not None and slot.equals(page):
                slot.reference_count += 1
                break

    def change_page_LRU(self, new_page):
        """Replaces the page in the memory with a new one based on LRU rules"""

        # Initialize the variables to keep track of which page to replace
        index_to_change = 0
        highest_time_not_used = -1  # -1 to ensure that the value time_not_used is greater than -1

        # Iterate through each slot to find the page with the highest 'time_not_used' value
        for i, page in enumerate(self.slots):
            # Ensure the page slot is not empty and check if the current page has the highest 'time_not_used'
            if page is not None and (highest_time_not_used < page.time_not_used):
                # If it is the highest, mark this page to be replaced
                index_to_replace = i
                highest_time_not_used = page.time_not_used

        # Replace the page at the found index with the new page.
        self.slots[index_to_change] = new_page

    def change_page_LFU(self, new_page):
        """Replaces the page in the memory with a new one based on LFU rules"""

        index_to_change = 0
        # Sets lowest_reference_count to infinity to ensure that any real page reference count will be lower
        lowest_reference_count = float('inf')

        for i, page in enumerate(self.slots):
            # Check if the current slot is not empty and its page's reference count is lower than the current lowest
            if page is not None and page.reference_count < lowest_reference_count:
                index_to_change = i
                lowest_reference_count = page.reference_count

        # Replace the page at the found index with the new page.
        self.slots[index_to_change] = new_page

    def fifo(self):
        """First in First out algorithm implementation"""

        longest_not_used_index = 0

        for page in self.pages_values:
            print(f"Adding page: {page}")

            # Check if the page already exists in the slots
            does_page_exist = self.if_value_exists(page)

            # If the page does not exist, increase the page fault counter, and add the page
            if not does_page_exist:
                # Increase the page fault counter.
                self.page_faults += 1
                # Replace the page at the index for the longest not used with the new page
                self.slots[longest_not_used_index] = page
                # Update the index for the next longest not used page for the slot with higher index
                # If the increased index value doesn't exist in the memory list, return tu the beginning
                longest_not_used_index = (longest_not_used_index + 1) % len(self.slots)

            # Increase the time in memory for the future analysis
            self.add_time_in_memory()

            print(self.slots)
        print("Total page faults: ")
        return self.page_faults

    def lru(self):
        """Least Recently Used algorithm implementation"""

        for page in self.pages_values:
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
                # If not, replace the least recently used page
                else:
                    self.change_page_LRU(page)

            self.change_time_not_used(page)
            print(self.slots)
        print("Total page faults: ")
        return self.page_faults

    def lfu(self):
        """Least Frequently Used algorithm implementation"""

        for page in self.pages_values:
            print(f"Adding page: {page}")
            # Check if the page already exists in the slots
            if not self.if_value_exists(page):
                # If it does not exist, increase the page fault counter
                self.page_faults += 1
                # Check if there is an empty slot to add the page (represented by None value)
                if None in self.slots:
                    empty_slot_index = self.slots.index(None)
                    self.slots[empty_slot_index] = page
                # If not, replace the least frequent used page
                else:
                    self.change_page_LFU(page)

            self.increase_reference_count(page)
            print(self.slots)
        print("Total page faults: ")
        return self.page_faults
