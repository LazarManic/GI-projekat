import matplotlib.pyplot as plt
import pandas as pd

class Graph:
    """Class to drive graph for visualisation"""
    @staticmethod
    def Drive(programs):
        heuristics = []
        words_len = []
        times = []
        memories = []
        for program in programs:
            heuristics.append(program.get_heuristics())
            words_len.append(len(program.get_word()))
            times.append(program.get_execution_time())
            memories.append(program.get_execution_memory())

        data_dict = { 'Heuristic': heuristics, 'Word lenght': words_len, 'Time': times, 'Memory': memories }
        df = pd.DataFrame(data_dict)
        print(df)

        fig, ax = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')

        df1_h1 = df[df['Heuristic'] == 'Goodsuffix']
        df1_h1 = df1_h1.sort_values(by=['Memory'], ascending=True)
        print(df1_h1)
        df1_h2 = df[df['Heuristic'] == 'Badcharacter + Goodsuffix']
        df1_h2 = df1_h2.sort_values(by=['Memory'], ascending=True)
        print(df1_h2)
        ax[0].bar(df1_h1['Word lenght'] - 0.25, df1_h1['Memory'], label='Memory Goodsuffix', width = 0.5)  # Plot some data on the axes.
        ax[0].bar(df1_h2['Word lenght'] + 0.25, df1_h2['Memory'], label='Memory Badcharacter + Goodsuffix', width = 0.5)  # Plot some data on the axes.

        ax[0].set_xlabel('word lenght')  # Add an x-label to the axes.
        ax[0].set_ylabel('memory [KiB]')  # Add a y-label to the axes.
        ax[0].set_title("Memory")  # Add a title to the axes.
        ax[0].legend();  # Add a legend.

        df2_h1 = df[df['Heuristic'] == 'Goodsuffix']
        df2_h1 = df2_h1.sort_values(by=['Time'], ascending=True)
        print(df2_h1)

        df2_h2 = df[df['Heuristic'] == 'Badcharacter + Goodsuffix']
        df2_h2 = df2_h2.sort_values(by=['Time'], ascending=True)
        print(df2_h2)
        ax[1].bar(df2_h1['Word lenght'] - 0.25, df2_h1['Time'], label='Time Goodsuffix', width = 0.5)  # Plot some data on the axes.
        ax[1].bar(df2_h2['Word lenght'] + 0.25, df2_h2['Time'], label='Time Badcharacter + Goodsuffix', width = 0.5)  # Plot some data on the axes.

        ax[1].set_xlabel('word lenght')  # Add an x-label to the axes.
        ax[1].set_ylabel('Time [s]')  # Add a y-label to the axes.
        ax[1].set_title("Time")  # Add a title to the axes.
        ax[1].legend();  # Add a legend.
        plt.savefig('Test_figure.png', dpi=300)

        plt.show()
