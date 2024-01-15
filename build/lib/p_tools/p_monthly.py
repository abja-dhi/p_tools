from .p_structure import p_structure
from datetime import datetime
import numpy as np

def p_monthly(X):
    if not isinstance(X, p_structure):
        raise TypeError("The input must be a p_structure!")
    else:
        X.title = [X.title] + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        X.group = [X.group] + 12 * ['Monthly']
        new_data = X.data
        for i in range(12):
            month_data = np.empty(X.data.shape)
            month_data[:] = np.nan
            month_data[X.datetime.month == i+1] = X.data[X.datetime.month == i+1]
            new_data = np.column_stack((new_data, month_data))
        X.data = new_data
    return X