import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Graph:
    """Class to drive graph for visualisation"""
    @staticmethod
    def Drive(data_metrics):
        heuristics = []
        words_len = []
        times = []
        memories = []

        # create data frame
        for data in data_metrics:
            heuristics.append(data.heuristic_name)
            words_len.append(data.word_length)
            times.append(data.time)
            memories.append(data.memory)

        data_dict = { 'Heuristic': heuristics, 'Word lenght': words_len, 'Time': times, 'Memory': memories }
        df = pd.DataFrame(data_dict)

        # create 2 figures, one for memory allocation and one for time
        fig, ax = plt.subplots(1, 2, figsize=(10, 6.4), layout='constrained')
        # Memory
        ax[0].grid()
        ax[0].set_xticks(np.arange(min(df['Word lenght']), max(df['Word lenght'])+1, 1.0))
        ax[0].set_xlabel('word lenght')  # Add an x-label to the axes.
        ax[0].set_ylabel('memory [KiB]')  # Add a y-label to the axes.
        ax[0].set_title("Memory")  # Add a title to the axes.

        # Time
        ax[1].grid()
        ax[1].set_xticks(np.arange(min(df['Word lenght']), max(df['Word lenght'])+1, 1.0))
        ax[1].set_xlabel('word lenght')  # Add an x-label to the axes.
        ax[1].set_ylabel('Time [s]')  # Add a y-label to the axes.
        ax[1].set_title("Time")  # Add a title to the axes.

        
        # Prepare data
        # get unique heuristics
        heuristics = df['Heuristic'].unique()
        width = 1 / len(heuristics)
        move_unit = width / 2
        unit = - (len(heuristics) / 2)

        for h in heuristics:
            df_h = df[df['Heuristic'] == h]
            ax[0].bar(df_h['Word lenght'] + unit * width + move_unit , df_h['Memory'], label=h, width = width)  # Plot some data on the axes.
            ax[1].bar(df_h['Word lenght'] + unit * width + move_unit , df_h['Time'], label=h, width = width)  # Plot some data on the axes.
            unit += 1

        ax[0].legend();  # Add a legend.
        ax[1].legend();  # Add a legend.

        plt.savefig('Test_figure.png', dpi=300)
        plt.show()

        # Export table
        df = df.sort_values(by=['Word lenght','Time','Memory'], ascending=[False,True,True])
        df.to_html('Test_table.html')
        
