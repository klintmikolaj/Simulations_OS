import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
matplotlib.use('TkAgg') # For opening pyplots in new windows

class ChartPainter:
    def __init__(self, chart_data):
        self.chart_data = chart_data

    def draw_chart(self):
        fig, ax = plt.subplots()
        for data in self.chart_data:
            start_time = data['start_time']
            execution_time = data['execution_time']
            waiting_time = data['waiting_time']
            process_id = data['process_id']

            # Rysowanie linii reprezentującej czas oczekiwania
            if waiting_time > 0:
                ax.plot([start_time, start_time + waiting_time], [process_id, process_id],
                        'r--')  # Przerywana czerwona linia

            # Rysowanie linii reprezentującej czas wykonania
            ax.plot([start_time + waiting_time, start_time + waiting_time + execution_time], [process_id, process_id],
                    'b-')  # Ciągła niebieska linia

        # Ustawienie etykiet i tytułu wykresu
        ax.set_xlabel('Czas')
        ax.set_ylabel('Nr procesu')
        ax.set_title('Wykres FCFS')
        ax.set_ylim(0, len(self.chart_data) + 1)  # Ustawienie zakresu osi Y
        ax.set_xlim(0, max([data['start_time'] + data['waiting_time'] + data['execution_time'] for data in
                            self.chart_data]))  # Ustawienie zakresu osi X
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

        ax.legend(['Czas oczekiwania', 'Czas wykonania'])
        plt.grid(color='grey', linestyle='-', linewidth=0.25)
        plt.show()
