"""
Fitting functionality for plasma data
"""

from data import get_float_data

from numpy import log
from scipy.optimize import curve_fit

def paschen_curve_model(pressure, distance, A, B, gamma):
    """ 
    Model for Paschen curve

    @param pressure: Pressure at which to measure breakdown voltage
    @param distance: Distance between electrodes
    @param A: Fit parameter. Saturation ionization of gas
    @param B: Fit parameter. Related to excitation and ionization energies
    @param gamma: Fit parameter. Secondary electron emission coefficient
    @return: Breakdown voltage as predicted by Paschen's Law
    """
    return B * pressure * distance / (log(A * pressure * distance) - 
            log(log(1 + 1 / gamma)))


def fit_data(y_key, data=get_float_data(), model=paschen_curve_model):
    """
    Fits the given data with given model

    @param y_key: Key to use for y data of fit
    @param data: Data to fit. Defaults to data.get_float_data()
    @param model: Model to fit. Defaults to paschen_curve_model
    @return: TODO
    """

    # Trim x data to y data
    x_data = []
    for i, y in enumerate(data[y_key]):
        if y:
            x_data.append(data['Pressure'][i])
    
    curve_fit(model, xdata=x_data, ydata=data[y_key])


# Code to execute when file is called from command line
if __name__ == '__main__':
    pass
