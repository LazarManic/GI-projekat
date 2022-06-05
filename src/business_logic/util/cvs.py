import csv

class Cvs():
    """Class to create cvs file for easier graph creation"""
    @staticmethod
    def write(cvs_file_path, programs):
        with open(cvs_file_path, 'w') as csvfile:
            
            # include the names for each column/feature
            fieldnames = ['Heuristic','Word', 'Time', 'Memory']
            
            # create a writer object that takes the csv file and fieldnames as parameters.
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # this writer the fieldnames to the file, i.e 'number' and 'colour'
            thewriter.writeheader()
            
            for program in programs:
                thewriter.writerow({'Heuristic':program.get_heuristics, 'Word': program.get_word, 'Time': program.get_execution_time, 'Memory': program.get_execution_memory})
