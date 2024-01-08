import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
matplotlib.use('TkAgg') # Opens pyplots in new windows

class ChartPainter:
    def __init__(self, chart_data, alg_type):
        self.chart_data = chart_data
        self.alg_type = alg_type

    def draw_chart(self):
        '''Creates a chart showing the timelapse of FCFS/SJF algorithms'''
        plt.close()
        fig, ax = plt.subplots()
        ax.clear()

        # Set min and max process ID from given data
        min_process_id = min(data['process_id'] for data in self.chart_data)
        max_process_id = max(data['process_id'] for data in self.chart_data)

        for data in self.chart_data:
            start_time = data['start_time']
            execution_time = data['execution_time']
            waiting_time = data['waiting_time']
            process_id = data['process_id']

            # If there is a waiting time, draw it as a dashed red line
            if waiting_time > 0:
                ax.plot([start_time, start_time + waiting_time], [process_id, process_id], 'r--')
            # Draw the execution time as a solid blue line.
            ax.plot([start_time + waiting_time, start_time + waiting_time + execution_time], [process_id, process_id],
                    'b-')

        ax.set_xlabel('Time')
        ax.set_ylabel('Process ID')
        ax.set_title(f'{self.alg_type} algorithm chart')
        # Set the y-axis limits based on the process IDs.
        ax.set_ylim(min_process_id - 1, max_process_id + 1)
        # Set the x-axis limits based on the start, waiting, and execution times.
        ax.set_xlim(0, max([data['start_time'] + data['waiting_time'] + data['execution_time'] for data in
                            self.chart_data]))
        # Show major ticks at every integer value.
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

        ax.legend(['Execution time', 'Waiting time'])
        plt.grid(color='grey', linestyle='-', linewidth=0.25)
        plt.show()
        plt.close(fig)


