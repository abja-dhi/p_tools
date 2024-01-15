from .p_structure import p_structure
import numpy as np
from scipy.stats import skew

class p_stats:
    def __init__(self, X) -> None:
        if not isinstance(X, p_structure):
            raise TypeError("The input must be a p_structure!")
        else:
            if len(X.data.shape) == 1:
                N, MEAN, MIN, MAX, STD, SKEW = self.calculate_stats(X.data)
            else:
                N = np.array([])
                MEAN = np.array([])
                MIN = np.array([])
                MAX = np.array([])
                STD = np.array([])
                SKEW = np.array([])
                for i in range(X.data.shape[1]):
                    tN, tMEAN, tMIN, tMAX, tSTD, tSKEW = self.calculate_stats(X.data[:, i])
                    N = np.append(N, tN)
                    MEAN = np.append(MEAN, tMEAN)
                    MIN = np.append(MIN, tMIN)
                    MAX = np.append(MAX, tMAX)
                    STD = np.append(STD, tSTD)
                    SKEW = np.append(SKEW, tSKEW)
        self.N = N
        self.MEAN = MEAN
        self.MIN = MIN
        self.MAX = MAX
        self.STD = STD
        self.SKEW = SKEW

    def __str__(self) -> str:
        out = {"N": self.N, "Mean": self.MEAN, "Min": self.MIN, "Max": self.MAX, "Standard deviation": self.STD, "Skewness": self.SKEW}
        return str(out)

    def calculate_stats(self, data):
        data = data[np.logical_not(np.isnan(data))]
        N = data.shape[0]
        MEAN = np.mean(data)
        MIN = np.min(data)
        MAX = np.max(data)
        STD = np.std(data)
        SKEW = skew(data)
        return N, MEAN, MIN, MAX, STD, SKEW