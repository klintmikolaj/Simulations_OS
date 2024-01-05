from processor_alg import Process
from processor_alg import ProcessorAlg
from memoryalg import MemoryAlg
from chart_painter import ChartPainter
from input_memory import load_memory_data
from input_processor import load_specific_data


class Test:
    def __init__(self):
        self.test_count = 0
        self.RED = '\033[31m'
        self.RESET ='\033[0m'
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'

    def help_panel(self):
        print(f"{self.BLUE} WELCOME TO THE HELP PANEL {self.RESET}")
        print(self.BLUE + "> q" + self.RESET + " - quits the program")
        print(self.BLUE + "> t" + self.RESET + " - displays a number of conducted tests")
        print(self.BLUE + "> fcfs" + self.RESET + "- perform the simulation of the FCFS algorithm")
        print(self.BLUE + "> sjf" + self.RESET + "- perform the simulation of the SJF algorithm ")
        print(self.BLUE + "> fifo" + self.RESET + "- perform the simulation of the FIFO algorithm ")
        print(self.BLUE + "> lru" + self.RESET + "- perform the simulation of the LRU algorithm ")

    def test_processor(self, data, alg_type):
        print("-----------------------------------------")
        if alg_type == "fcfs":
            print("Testing FCFS algorithm")
        elif alg_type == "sjf":
            print("Testing SJF algorithm")
        print(f"Test data: {data}")

        processes_list = []
        for process in data:
            process_start = process[0]
            process_exec = process[1]
            processes_list.append(Process(process_start, process_exec))
        algorithm = ProcessorAlg(processes_list)
        if alg_type == "fcfs":
            alg_output = algorithm.fcfs()
            chart = ChartPainter(alg_output['chart_data'], "FCFS")
        elif alg_type == "sjf":
            alg_output = algorithm.sjf()
            chart = ChartPainter(alg_output['chart_data'], "SJF")
        print(f"Logs: {alg_output}")
        print("-----------------------------------------")
        chart.draw_chart()
        self.test_count += 1

    def test_memory(self, data, alg_type):
        num_of_slots = int(input("Enter the number of slots: "))

        if alg_type == "fifo":
            print("Testing FIFO algorithm")
        elif alg_type == "lru":
            print("Testing LRU algorithm")

        for i in range(1, len(data) + 1):
            print(f"Test number {i}:")
            pages_list = []
            test_data = data[i - 1]
            for base_id in test_data:
                pages_list.append(base_id)
            print(f'Pages list: {pages_list}')
            algorithm = MemoryAlg()
            algorithm.set_reference_values(pages_list)
            algorithm.set_slots(num_of_slots)
            if alg_type == "fifo":
                alg_output = algorithm.fifo()
            else:
                alg_output = algorithm.lru()
            print(alg_output)
            print("-----------------------------------------")
            self.test_count += 1

    def testing_loop(self):
        print("-----------------------------------------")
        print(self.RED + "ALGORITHM TESTER" + self.RESET)
        while True:
            choice = input("Enter a command -> ")
            if choice == "q":
                break
            elif choice == "fcfs":
                self.test_processor(load_specific_data(), "fcfs")
            elif choice == "sjf":
                self.test_processor(load_specific_data(), "sjf")
            elif choice == "fifo":
                self.test_memory(load_memory_data(), "fifo")
            elif choice == "lru":
                self.test_memory(load_memory_data(), "lru")
            elif choice == "t":
                print(f"Number of conducted tests: {self.RED}{self.test_count}{self.RESET}")
            elif choice == "h":
                self.help_panel()
            else:
                print(self.RED + "Unknown command, press 'h' to display the help panel" + self.RESET)


test = Test()
test.testing_loop()
