import matplotlib.pyplot as plt
import pandas as pd

class Graph:
    """Class to drive graph for visualisation"""
    @staticmethod
    def Drive(file_path):
        # TODO serious todo.. :')
        gas = pd.read_csv(file_path)
        plt.figure(figsize=(8,5))

        plt.title('Memory allocation for different heuristics on same text input and search words', fontdict={'fontweight':'bold', 'fontsize': 16})

        plt.plot(gas.Word, gas.Memory, 'b.-', label=gas.Heuristic)

        plt.savefig('Test_figure.png', dpi=300)

        plt.show()