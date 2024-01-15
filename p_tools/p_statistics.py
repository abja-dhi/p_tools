from .p_structure import p_structure
from .p_stats import p_stats
from .p_monthly import p_monthly
import numpy as np
import matplotlib.pyplot as plt

def p_statistics(X, sub="monthly", quantiles=np.array([25, 50, 75])):
    if not isinstance(X, p_structure):
        raise TypeError("The input must be a p_structure!")
    elif not (isinstance(quantiles, list) or isinstance(quantiles, np.array)):
        raise TypeError("quantiles must a list or numpy array!")
    else:
        if isinstance(quantiles, list):
            quantiles = np.array(quantiles)
            if quantiles[0] > 1:
                quantiles = quantiles / 100.0
        if "monthly" in sub.lower():
            X = p_monthly(X)
        stats = p_stats(X)
        Q = {}
        for q in quantiles:
            Q["P"+str(np.int(q*100))] = calculate_quantiles(X.data, q)

def calculate_quantiles(data, P):
    if len(data.shape) == 1:
        return np.array([np.nanquantile(data, P)])
    else:
        Q = np.array([])
        for i in range(data.shape[1]):
            np.append(Q, np.nanquantile(data[:, i], P))
        return Q
    
def plot_statistics(X, stats, Q):
    subtitle = X.ttt_str.replace("_", " - ")
    filename = "_".join([X.name, "Statistics", X.item, X.legend, subtitle, X.group[-1]])
    heading = [" ".join([X.name + X.xyz_str]),
               " ".join(["Statistics", X.ttt_str_long, X.legend, X.group[-1]])]
    