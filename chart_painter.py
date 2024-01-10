import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

matplotlib.use('TkAgg')  # Opens pyplots in new windows


class ChartPainter:
    """Class for drawing charts to visualize FCFS/SJF algorithms"""

    def __init__(self, chart_data, alg_type):
        self.chart_data = chart_data
        self.alg_type = alg_type

    def draw_chart(self):
        """Creates a chart showing the timelapse of FCFS/SJF algorithms"""

        # Define the chart figure as fig and axes as ax
        fig, ax = plt.subplots()

        # Set minimum and maximum process ID from given data
        min_id = min(data['process_id'] for data in self.chart_data)
        max_id = max(data['process_id'] for data in self.chart_data)

        # Set local variables from given dict
        for data in self.chart_data:
            start_time = data['start_time']
            execution_time = data['execution_time']
            waiting_time = data['waiting_time']
            process_id = data['process_id']

            # Draw a dashed red line simulating processes waiting time if it exists
            if waiting_time > 0:
                ax.plot([start_time, start_time + waiting_time], [process_id, process_id], 'r--')

            # Draw the processes execution times as a solid line
            ax.plot([start_time + waiting_time, start_time + waiting_time + execution_time], [process_id, process_id],
                    'b-')

        # Set axis labels and the chart title
        ax.set_title(f'{self.alg_type} algorithm chart')
        ax.set_xlabel('Time')
        ax.set_ylabel('Process ID')

        # Set the axis y limits based on the process IDs value, start with ID lower by one and end with higher by one
        # for better transparency
        ax.set_ylim(min_id - 1, max_id + 1)

        # Set the axis x limits based on the maximum value of start, waiting, and execution times
        ax.set_xlim(0, max([data['start_time'] + data['waiting_time'] + data['execution_time'] for data in
                            self.chart_data]))

        # Show major marks at int values.
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

        # Add a legend to the chart
        ax.legend(['Execution time', 'Waiting time'])

        # Draw an auxiliary line and show the chart
        plt.grid(color='grey', linestyle='-', linewidth=0.25)
        plt.show()

