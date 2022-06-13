

import tracemalloc
import time
from dataclasses import dataclass

@dataclass
class PerformanceData:
    """Class holds relevant performance data for plotting on a graph"""
    heuristic_name:str
    word_length:int 
    time:int
    memory:int

    

class Performance():
    """Class is used to estimate performance metrics like execution time and memory usage"""
    def __init__(self):
        # Init members
        self.start_time = 0
        self.end_time = 0


    def start_clock(self):
       # start monitoring memory allocation and time of execusion
        tracemalloc.start()
        self.start_time = time.time()
    

    def stop_clock(self)->(int, int):

        # stop monitoring and fetch memory and time 
        self.end_time = time.time()
        memory = tracemalloc.get_traced_memory()

      
        tracemalloc.stop()

        self.time = self.end_time - self.start_time
        
        # memory at its peak - memory at start point
        self.memory = memory[1] - memory[0]

        print("Execution time: {}, execution memory peak: {} KiB".format(self.time,self.memory))
        return self.time, self.memory
