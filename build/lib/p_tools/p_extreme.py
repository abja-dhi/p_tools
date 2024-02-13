from .p_structure import p_structure

def p_extreme(X, options, *arg):
    if not isinstance(X, p_structure):
        raise TypeError("The input must be a p_structure!")
    elif not (isinstance(options, dict)):
        raise TypeError("quantiles must a list or numpy array!")
    else:
        