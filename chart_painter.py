import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
matplotlib.use('TkAgg') # For opening pyplots in new windows

class ChartPainter:
    def __init__(self, chart_data, alg_type):
        self.chart_data = chart_data
        self.alg_type = alg_type

    def draw_chart(self):
        plt.close()
        fig, ax = plt.subplots()
        ax.clear()

        min_process_id = min(data['process_id'] for data in self.chart_data)
        max_process_id = max(data['process_id'] for data in self.chart_data)

        for data in self.chart_data:
            start_time = data['start_time']
            execution_time = data['execution_time']
            waiting_time = data['waiting_time']
            process_id = data['process_id']

            if waiting_time > 0:
                ax.plot([start_time, start_time + waiting_time], [process_id, process_id], 'r--')
            ax.plot([start_time + waiting_time, start_time + waiting_time + execution_time], [process_id, process_id],
                    'b-')

        ax.set_xlabel('Time')
        ax.set_ylabel('Process ID')
        ax.set_title(f'{self.alg_type} algorithm chart')
        ax.set_ylim(min_process_id - 1, max_process_id + 1)
        ax.set_xlim(0, max([data['start_time'] + data['waiting_time'] + data['execution_time'] for data in
                            self.chart_data]))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

        ax.legend(['Waiting time', 'Execution time'])
        plt.grid(color='grey', linestyle='-', linewidth=0.25)
        plt.show()
        plt.close(fig)


