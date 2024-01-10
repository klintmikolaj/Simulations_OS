from processor_alg import Process
from processor_alg import ProcessorAlg
from memoryalg import MemoryAlg
from chart_painter import ChartPainter
from input_memory import load_specific_memory_data
from input_processor import load_specific_processor_data
import json


class Test:
    """Class used for testing all algorithms, contains a loop for performing uninterrupted tests"""

    def __init__(self):
        self.test_count = 0

        # Colors variables definition
        self.RED = '\033[31m'
        self.RESET = '\033[0m'
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'

    def help_panel(self):
        """Displays a help panel with all useful commands"""

        print(f"{self.BLUE} WELCOME TO THE HELP PANEL {self.RESET}")
        print(self.BLUE + "> q" + self.RESET + " - quits the program")
        print(self.BLUE + "> t" + self.RESET + " - displays a number of conducted tests")
        print(self.BLUE + "> fcfs" + self.RESET + "- perform the simulation of the FCFS algorithm")
        print(self.BLUE + "> sjf" + self.RESET + "- perform the simulation of the SJF algorithm ")
        print(self.BLUE + "> fifo" + self.RESET + "- perform the simulation of the FIFO algorithm ")
        print(self.BLUE + "> lru" + self.RESET + "- perform the simulation of the LRU algorithm ")
        print(self.BLUE + "> lfu" + self.RESET + "- perform the simulation of the LFU algorithm ")

    def test_processor(self, data, alg_type):
        """Creates a processes list and passes it to the ProcessorAlg instance, then simulates FCFS/SJF algorithms"""

        print("-----------------------------------------")
        if alg_type == "fcfs":
            print("Testing FCFS algorithm")
        elif alg_type == "sjf":
            print("Testing SJF algorithm")
        print(f"Test data: {data}")

        # Creates the processes list to store all processes used in the test
        processes_list = []
        for process in data:
            process_start = process[0]
            process_exec = process[1]
            processes_list.append(Process(process_start, process_exec))
        algorithm = ProcessorAlg(processes_list)

        # Performs the processor algorithms
        if alg_type == "fcfs":
            alg_output = algorithm.fcfs()
            chart = ChartPainter(alg_output['chart_data'], "FCFS")
        elif alg_type == "sjf":
            alg_output = algorithm.sjf()
            chart = ChartPainter(alg_output['chart_data'], "SJF")
        del alg_output["chart_data"]

        # More readable output
        print(f"Logs: {json.dumps(alg_output, indent=4)}")
        print("-----------------------------------------")

        # Displays a chart in a separate window
        chart.draw_chart()
        self.test_count += 1

    def test_memory(self, data, alg_type):
        """Creates a pages list and passes it to the MemoryAlg instance, then simulates FIFO/LRU algorithms"""

        num_of_slots = int(input("Enter the number of slots: "))

        if alg_type == "fifo":
            print("Testing FIFO algorithm")
        elif alg_type == "lru":
            print("Testing LRU algorithm")
        elif alg_type == "lfu":
            print("Testing LFU algorithm")

        # for i in range(1, len(data) + 1): # Used for an alternative way of testing
        # print(f"Test number {i}:")

        # Creates the processes list to store all processes used in the test
        pages_list = []
        test_data = data
        for base_id in test_data:
            pages_list.append(base_id)
        print(f'Pages list: {pages_list}')

        # Performs an algorithms with a given number of slots in the memory list
        algorithm = MemoryAlg()
        algorithm.set_reference_values(pages_list)
        algorithm.set_slots(num_of_slots)
        if alg_type == "fifo":
            alg_output = algorithm.fifo()
        elif alg_type == "lru":
            alg_output = algorithm.lru()
        elif alg_type == "lfu":
            alg_output = algorithm.lfu()
        print(alg_output)
        print("-----------------------------------------")
        self.test_count += 1

    def testing_loop(self):
        """Loop for performing uninterrupted tests"""

        # Create a dictionary which contains a command as a key
        # Values associated with the key: test method, function to load the data,
        # prompt for the user and available values to enter
        commands_dict = {
            "fcfs": (self.test_processor, load_specific_processor_data,
                     "Enter a test value (1, 2, 3, 4, 5.1, 5.2 or 5.3) -> ", {"1", "2", "3", "4", "5.1", "5.2", "5.3"}),
            "sjf": (self.test_processor, load_specific_processor_data,
                    "Enter a test value (1, 2, 3, 4, 5.1, 5.2 or 5.3) -> ", {"1", "2", "3", "4", "5.1", "5.2", "5.3"}),
            "fifo": (self.test_memory, load_specific_memory_data, "Enter a test value (1, 2 or 3) -> ", {"1", "2", "3"}),
            "lru": (self.test_memory, load_specific_memory_data, "Enter a test value (1, 2 or 3) -> ", {"1", "2", "3"}),
            "lfu": (self.test_memory, load_specific_memory_data, "Enter a test value (1, 2 or 3) -> ", {"1", "2", "3"})
        }

        print("-----------------------------------------")
        print(self.RED + "ALGORITHM TESTER" + self.RESET)
        print("Press 'h' to open the help panel")

        while True:
            choice = input("Enter a command -> ").strip()
            if choice == "q":
                return 0
            elif choice == "t":
                print(f"Number of conducted tests: {self.RED}{self.test_count}{self.RESET}")
            elif choice == "h":
                self.help_panel()

            # If the choice value is equal to the test command
            elif choice in commands_dict:
                # Take all values from the dictionary and declare new variables
                test_method, data_function, prompt, commands_set = commands_dict[choice]
                while True:
                    test = input(prompt).strip()
                    if test in commands_set:
                        test_method(data_function(test), choice)
                        break
                    else:
                        print(
                            self.RED + "Incorrect test number. Select the proper one from the given list." + self.RESET)
            else:
                print(self.RED + "Unknown command, press 'h' to display the help panel" + self.RESET)
