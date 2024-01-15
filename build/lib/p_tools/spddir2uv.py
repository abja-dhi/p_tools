import numpy as np
from .p_structure import p_structure

def spddir2uv(spd, dir, *arg):
    """
    'invert' option is for the wind. For the currents, don't use any varargin
    Converts from speed and direction to u- and v-components.
    """
    if type(spd) == "p_structure":
        u = spd
        v = spd
        u.data, v.data = convert(spd.data, dir.data, *arg)
    else:
        [u, v] = convert(spd, dir, *arg)
    
    return u, v

def convert(spd, dir, *arg):
    i = 0
    while i < len(arg):
        if "invert" in arg[i]:
            dir = dir + 180
            dir[dir > 360] = dir[dir > 360] - 360
        elif 'angle' in arg[i]:
            dir = dir + arg[i+1]
            i = i + 1
        i = i + 1
    
    u = spd * np.sin(dir * np.pi / 180)
    v = spd * np.cos(dir * np.pi / 180)

    return u, v
