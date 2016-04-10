"""
Loads collected data
"""

from collections import defaultdict

# Column names in the order of the file
DATA_COL_NAMES = ['Date', 'Pressure', 'Sigma Pressure', 'Ignition Power',
                  'Sigma Ignition Power', 'Ignition Voltage',
                  'Sigma Ignition Voltage', 'Equilibrium Voltage',
                  'Sigma Equilibrium Voltage', 'Extinction Voltage',
                  'Sigma Extinction Voltage', 'Extinction Power',
                  'Sigma Extinction Power']

def get_data(filename='../resources/Plasma_Chamber.tsv'):
    # Dictionary for data
    data = defaultdict(list)

    with open(filename, 'r') as datafile:
        # Skip first line
        datafile.next()

        for line in datafile:
            # Strip newlines and split at tabs
            cols = line.strip('\r\n').split('\t')

            # Add data to dictionary corresponding to row in DATA_COL_NAMES
            [data[DATA_COL_NAMES[index]].append(value) for index, value in
                    enumerate(cols)]

    return data;

