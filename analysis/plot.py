"""
Plotting functionality for plasma chamber analysis
"""

import matplotlib.pyplot as plt

from data import get_float_data
from data import min_max_values

def plot_ignition_voltages(data=get_float_data(), fig=None):
    """
    Plots ignition  voltages with errors

    @param data: Data dictionary to use. Defaults to output from
                 data.get_float_data()
    @param fig: Handle to figure to use. Defaults to None, in which case a new
                figure is created
    @return: Handle to matplotlib plot
    """

    if fig is None:
        # Create new figure if not given
        fig = plt.figure()
    else:
        # Otherwise, switch active plot to the provided plot
        plt.sca(fig.gca())

    # Plot points
    plt.scatter(data['Pressure'], data['Ignition Voltage'], s=10)

    # Get minimum and max values for pressure errors
    pressure_minimums, pressure_maximums = min_max_values(data['Pressure'],
                                           data['Sigma Pressure'])

    # Plot horizontal (pressure) error lines
    plt.hlines(data['Ignition Voltage'], pressure_minimums, pressure_maximums)

    # Get minumum and maximum values for voltage errors
    voltage_minimums, voltage_maximums = min_max_values(data['Ignition Voltage'],
                                         data['Sigma Ignition Voltage'])

    # Plot vertical (voltage) error lines
    plt.vlines(data['Pressure'], voltage_minimums, voltage_maximums)

    return fig


def plot_equilibrium_voltages(data=get_float_data(), fig=None):
    """
    Plots the equilibrium voltage points

    @param data: Data to use for plot. Defaults to output from get_float_data()
    @return: Handle to matplotlib plot
    """

    if fig is None:
        # Create new figure if not given
        fig = plt.figure()
    else:
        # Otherwise, switch active plot to the provided plot
        plt.sca(fig.gca())

    # Plot equilibrium voltages
    plt.scatter(data['Pressure'], data['Equilibrium Voltage'], marker='s',
           s=10, color='red')

    # Error bars for equilibrium voltages
    # Get minimum and max values for pressure errors
    pressure_minimums, pressure_maximums = min_max_values(data['Pressure'],
                                           data['Sigma Pressure'])
    plt.hlines(data['Equilibrium Voltage'], pressure_minimums,
               pressure_maximums)
    voltage_minimums, voltage_maximums = min_max_values(data['Equilibrium Voltage'],
                                         data['Sigma Equilibrium Voltage'])
    plt.vlines(data['Pressure'], voltage_minimums, voltage_maximums)

    return fig


def plot_extinction_voltages(data=get_float_data(), fig=None):
    """
    Plots the extinction voltage points

    @param data: Data to use for plot. Defaults to output from get_float_data()
    @param fig: Figure for plot. Defaults to None, in which case a new plot is
                created
    @return Handle to matplotlib plot
    """

    if fig is None:
        # Create new figure if not given
        fig = plt.figure()
    else:
        # Otherwise, switch active plot to the provided plot
        plt.sca(fig.gca())

    # Plot extinction voltages
    plt.scatter(data['Pressure'], data['Extinction Voltage'], marker='D',
            s=10, color='green')

    # Error bars for extinction voltages
    # Get minimum and max values for pressure errors
    pressure_minimums, pressure_maximums = min_max_values(data['Pressure'],
                                           data['Sigma Pressure'])
    plt.hlines(data['Extinction Voltage'], pressure_minimums, pressure_maximums)
    voltage_minimums, voltage_maximums = min_max_values(data['Extinction Voltage'],
                                         data['Sigma Extinction Voltage'])
    plt.vlines(data['Pressure'], voltage_minimums, voltage_maximums)

    return fig


# Plot voltages if ran via CLI
if __name__ == '__main__':
    plot_voltages()
