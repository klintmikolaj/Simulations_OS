import input_processor
from input_processor import data
class Process:
    base_id = 0

    def __init__(self, process_execution_time):
        Process.base_id += 1
        self.id = self.base_id
        self.execution_time = process_execution_time
        self.waiting_time = 0

    def __repr__(self):
        info = f"Process id: {self.id} | execution time: {self.execution_time} | waiting time: {self.waiting_time}"
        return info

    def __str__(self):
        return self.__repr__()

    def add_waiting_time(self, val=1):
        self.waiting_time += val
        return self.waiting_time

class Processor_alg:
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

    def fcfs(self):
        num_of_processes = len(self.processes)
        while self.processes:
            process = self.processes.pop(0)
            self.processes_waiting_times.append(process.waiting_time)
            self.delay_processes(process.execution_time)
            print("Finished process ->", process)
            self.add_process_setting_time()

        self.average_process_waiting_time = self.average(self.processes_waiting_times, num_of_processes)
        print("Finished fcfs!")
        info_dict = dict(
                    execution_time=self.execution_time,
                    average_waiting_time=self.average_process_waiting_time,
                    max_waiting_time=max(self.processes_waiting_times))
        return info_dict

    def sjf(self):
        num_of_processes = len(self.processes)
        while self.processes:
            self.processes.sort(key=lambda x: x.execution_time)
            process = self.processes.pop(0)
            self.processes_waiting_times.append(process.waiting_time)
            print("Finished process ->", process)
            self.delay_processes(process.execution_time)
            self.add_process_setting_time()

        self.average_process_waiting_time = self.average(self.processes_waiting_times, num_of_processes)
        print("Finished sjf!")
        info_dict = dict(
                    execution_time=self.execution_time,
                    average_waiting_time=self.average_process_waiting_time,
                    max_waiting_time=max(self.processes_waiting_times))
        return info_dict

# test = [2, 45 , 325 , 135]
# processes_list = []
# for exec_time in test:
#     processes_list.append(Process(exec_time))
#
# alg = Processor_alg(processes_list)
# w = alg.fcfs()
# print(w)


print(input_processor.data)
for i in range(1, len(data)):
    print(f"Test number {i}:")
    processes_list = []
    test = data[i-1]
    for exec_time in test:
        processes_list.append(Process(exec_time))
    alg = Processor_alg(processes_list)
    w = alg.sjf()
    print(w)



