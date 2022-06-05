from cProfile import label
from time import time
import matplotlib.pyplot as plt
import pandas as pd
from pyparsing import line

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


        # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
        fig, ax = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
        ax[0].plot(df[df['Heuristic'] == 'Goodsuffix']['Word lenght'], df[df['Heuristic'] == 'Goodsuffix']['Memory'], label='Memory Goodsuffix')  # Plot some data on the axes.
        ax[0].plot(df[df['Heuristic'] == 'Badcharacter + Goodsuffix']['Word lenght'], df[df['Heuristic'] == 'Badcharacter + Goodsuffix']['Memory'], label='Memory Badcharacter + Goodsuffix')  # Plot some data on the axes.
        ax[1].plot(df[df['Heuristic'] == 'Goodsuffix']['Word lenght'], df[df['Heuristic'] == 'Goodsuffix']['Time'], label='Time Goodsuffix', linestyle='--')  # Plot some data on the axes.
        ax[1].plot(df[df['Heuristic'] == 'Badcharacter + Goodsuffix']['Word lenght'], df[df['Heuristic'] == 'Badcharacter + Goodsuffix']['Time'], label='Time Badcharacter + Goodsuffix', linestyle='--')  # Plot some data on the axes.
        ax[0].set_xlabel('word lenght')  # Add an x-label to the axes.
        ax[0].set_ylabel('memory [KiB]')  # Add a y-label to the axes.
        ax[0].set_title("Memory")  # Add a title to the axes.
        ax[0].legend();  # Add a legend.
        ax[1].set_xlabel('word lenght')  # Add an x-label to the axes.
        ax[1].set_ylabel('Time [s]')  # Add a y-label to the axes.
        ax[1].set_title("Time")  # Add a title to the axes.
        ax[1].legend();  # Add a legend.
        plt.savefig('Test_figure.png', dpi=300)

        plt.show()
