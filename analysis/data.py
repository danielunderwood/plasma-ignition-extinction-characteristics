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
    """
    Gets the data from filename

    @param filename: Filename to get data from. Must be tab delimted in the
                     expected format. Defaults to data file's location in
                     repo
    @return Returns a dict of lists with keys of column names and values of
            strings of values. Missing values have empty strings and no
            data conversion is done
    """

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

def get_float_data(data=get_data()):
    """
    Gets experimental values as a dictionary of float values (with the exception
    of the date column, which is kept as a string)

    @param data: Data dictionary. Defaults to the data returned by get_data()
    @return Returns a dictionary of float arrays with the exception of the date
            column
    """

    # Convert values
    for key, value in data.iteritems():
        if key != 'Date':
            data[key] = [float(x) if x else None for x in value]

    return data

def min_max_values(data, errors):
    """
    Gets an array of minumum and maximum values of data with errors given in
    errors

    @param data: Array of mean data points
    @param errors: Array of errors
    @return Tuple of ([minimum], [maximum]) values
    """

    return ([data[i] - errors[i] if data[i] and errors[i] else None 
            for i in range(0, len(data))],
            [data[i] + errors[i] if data[i] and errors[i] else None
            for i in range(0, len(data))])

