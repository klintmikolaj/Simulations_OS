class Process:
    """Class imitating a single process in FCFS/SJF algorithms"""

    # Define base id to ensure that every process has its id greater by one from the previous one
    base_id = 0

    def __init__(self, process_start_time, process_execution_time):
        Process.base_id += 1
        self.id = self.base_id
        self.execution_time = process_execution_time
        self.start_time = process_start_time
        self.waiting_time = 0

        # Colors variables definition
        self.RED = '\033[91m'
        self.RESET = '\033[0m'
        self.BLUE = '\033[34m'
        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m'

    def __repr__(self):
        # Displays information about a process
        info = (f"Process id: {self.RED} {self.id} {self.RESET}"
                f"| start time: {self.BLUE} {self.start_time} {self.RESET} "
                f"| execution time: {self.GREEN} {self.execution_time} {self.RESET}"
                f"| waiting time: {self.YELLOW} {self.waiting_time} {self.RESET}")
        return info

    def __str__(self):
        return self.__repr__()

    def add_waiting_time(self, val=1):
        self.waiting_time += val
        return self.waiting_time


class ProcessorAlg:
    """Class used for manipulating data using FCFS/SJF algorithms"""

    def __init__(self, processes):
        # Defines self.processes as the list of objects Process
        self.processes: list[Process] = processes
        self.execution_time = 0
        self.average_process_waiting_time = 0
        self.processes_waiting_times: list[int] = []

    def add_process_setting_time(self, val=0):
        """Add time if the processor unit needs time to end process and start the new one"""

        self.execution_time += val

    @staticmethod
    def average(list_values, count):
        """Calculate the average value from the given list"""

        return round(sum(list_values) / count, 3)

    def delay_processes(self, val=1):
        """Add waiting time to processes and increase the whole algorithm execution time"""

        for i in self.processes:
            i.add_waiting_time(val)
        self.execution_time += val

    def sort_by_start_time(self):
        """Sort processes by their start time value"""

        self.processes.sort(key=lambda process: process.start_time)

    def fcfs(self):
        """First Come First Serve algorithm implementation"""

        # Sort the processes and set current time to 0
        self.sort_by_start_time()
        num_of_processes = len(self.processes)
        current_time = 0

        # Initialize a list to keep track of the chart logs for visualization
        chart_logs = []
        for process in self.processes:
            # If the current time is lower than the process's start time, update the current time
            if current_time < process.start_time:
                current_time = process.start_time

            # Calculate the waiting time for the process
            process.waiting_time = current_time - process.start_time

            # Update the current time
            current_time += process.execution_time

            # Add new waiting time to a list for future analysis
            self.processes_waiting_times.append(process.waiting_time)

            # Create a dictionary log for future visualisation
            process_logs = dict(
                process_id=process.id,
                start_time=process.start_time,
                execution_time=process.execution_time,
                waiting_time=process.waiting_time)
            chart_logs.append(process_logs)
            print("Finished process ->", process)

        # Calculate the average from all waiting times
        self.average_process_waiting_time = self.average(self.processes_waiting_times, num_of_processes)
        print("Finished fcfs!")

        # Create and return a dictionary with important data for analysis
        info_dict = dict(
            execution_time=current_time,
            average_waiting_time=self.average_process_waiting_time,
            max_waiting_time=max(self.processes_waiting_times),
            chart_data=chart_logs)
        return info_dict

    def sjf(self):
        """Shortest Job First algorithm implementation"""

        # Declare a number of processes and set current time to 0
        num_of_processes = len(self.processes)
        current_time = 0

        # Create a list to keep track of the chart logs for visualization
        chart_logs = []

        # The loop continues if there is at least one process in the list
        while self.processes:

            # Filter the processes by the current time
            available_processes = [p for p in self.processes if p.start_time <= current_time]

            # If no processes are available, increase the current time and continue
            if not available_processes:
                current_time += 1
                continue

            # Sort the available processes by their execution time
            available_processes.sort(key=lambda x: x.execution_time)

            # Select shortest process and delete it from the list
            process = available_processes[0]
            self.processes.remove(process)

            # Calculate the waiting time for the process and update the current time
            process.waiting_time = current_time - process.start_time
            current_time += process.execution_time

            self.processes_waiting_times.append(process.waiting_time)

            # Create a dictionary log for future visualisation
            process_logs = dict(
                process_id=process.id,
                start_time=process.start_time,
                execution_time=process.execution_time,
                waiting_time=process.waiting_time)
            chart_logs.append(process_logs)
            print("Finished process ->", process)

        # Add new waiting time to a list for future analysis
        self.average_process_waiting_time = self.average(self.processes_waiting_times, num_of_processes)

        print("Finished sjf!")

        # Create and return a dictionary with important data for analysis
        info_dict = dict(
            execution_time=current_time,
            average_waiting_time=self.average_process_waiting_time,
            max_waiting_time=max(self.processes_waiting_times),
            chart_data=chart_logs)
        return info_dict
