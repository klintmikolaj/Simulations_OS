import input_processor
from chart_painter import ChartPainter
class Process:
    base_id = 0

    def __init__(self, process_start_time, process_execution_time):
        Process.base_id += 1
        self.id = self.base_id
        self.execution_time = process_execution_time
        self.start_time = process_start_time
        self.waiting_time = 0

    def __repr__(self):
        RED = '\033[91m'
        RESET = '\033[0m'
        BLUE = '\033[34m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        info = (f"Process id: {RED} {self.id} {RESET}"
                f"| start time: {BLUE } {self.start_time} {RESET} "
                f"| execution time: {GREEN} {self.execution_time} {RESET}"
                f"| waiting time: {YELLOW} {self.waiting_time} {RESET}")
        return info

    def __str__(self):
        return self.__repr__()

    def add_waiting_time(self, val=1):
        self.waiting_time += val
        return self.waiting_time

class ProcessorAlg:
    def __init__(self, processes):
        self.processes: list[Process] = processes
        self.execution_time = 0
        self.average_process_waiting_time = 0
        self.processes_waiting_times: list[int] = []

    def add_process_setting_time(self, val=0):
        '''Add time if the processor unit needs time to end process and start the new one '''
        self.execution_time += val

    @staticmethod
    def average(list_values, count):
        return round(sum(list_values) / count, 3)
    def delay_processes(self, val=1):
        for i in self.processes:
            i.add_waiting_time(val)
        self.execution_time += val


    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)


    def fcfs(self):
        self.sort_by_start_time()
        num_of_processes = len(self.processes)
        current_time = 0
        chart_logs = []
        for process in self.processes:
            if current_time < process.start_time:
                current_time = process.start_time
            process.waiting_time = current_time - process.start_time
            current_time += process.execution_time
            self.processes_waiting_times.append(process.waiting_time)
            process_logs = dict(
                process_id=process.id,
                start_time=process.start_time,
                execution_time=process.execution_time,
                waiting_time=process.waiting_time)
            chart_logs.append(process_logs)
            print("Finished process ->", process)
        self.average_process_waiting_time = self.average(self.processes_waiting_times, num_of_processes)
        print("Finished fcfs!")
        info_dict = dict(
            execution_time=current_time,
            average_waiting_time=self.average_process_waiting_time,
            max_waiting_time=max(self.processes_waiting_times),
            chart_data=chart_logs)
        return info_dict

    def sjf(self):
        num_of_processes = len(self.processes)
        current_time = 0
        chart_logs = []
        while self.processes:
            available_processes = [p for p in self.processes if p.start_time <= current_time]
            if not available_processes:
                current_time += 1
                continue
            available_processes.sort(key=lambda x: x.execution_time)
            process = available_processes[0]
            self.processes.remove(process)
            process.waiting_time = current_time - process.start_time
            current_time += process.execution_time
            self.processes_waiting_times.append(process.waiting_time)
            process_logs = dict(
                process_id=process.id,
                start_time=process.start_time,
                execution_time=process.execution_time,
                waiting_time=process.waiting_time)
            chart_logs.append(process_logs)
            print("Finished process ->", process)
        self.average_process_waiting_time = self.average(self.processes_waiting_times, num_of_processes)

        print("Finished sjf!")
        info_dict = dict(
            execution_time=current_time,
            average_waiting_time=self.average_process_waiting_time,
            max_waiting_time=max(self.processes_waiting_times),
            chart_data=chart_logs)
        return info_dict
