import numpy as np
import mikeio_DHI
from .p_structure import p_structure

def uv2spddir(u, v, DIR, *arg):
    """
    SYNTAX: spd, dir = uv2spddir(u, v, 'to')     # Current
            spd, dir = uv2spddir(u, v, 'from')   # Wind & Waves
            spd, dir = uv2spddir(u, v, 'from','angle',-4.2)
    """
    if type(u) == "p_structure":
        spd = u
        dir = v
        spd.data, dir.data = convert(u.data, v.data, DIR, *arg)

        if 'from' in DIR:
            spd.item = "WS"
            dir.item = "WD"
        else:
            spd.item = "CS"
            dir.item = "CD"
    else:
        spd, dir = convert(u, v, DIR, *arg)
        

    return spd, dir


def convert(u, v, DIR, *arg):
    
    if np.max(u) > 50 or np.min(u) < -50:
        print("Suspiscious range of u data, please check input!")
    elif np.max(v) > 50 or np.min(v) < -50:
        print("Suspiscious range of v data, please check input!")

    if np.max(u) > 20:
        print("Most likely wind data, remember to invert direction!")
    
    spd = np.sqrt(np.power(u, 2) + np.power(v, 2))
    dir = np.arctan2(u, v) * 180 / np.pi

    if 'from' in DIR:
        dir = dir + 180.0

    i = 0
    while i < len(arg):
        if 'angle' in arg[i]:
            dir = dir + arg[i+1]
            i = i + 1
        i = i + 1

    dir[dir < 0] = dir[dir < 0] + 360
    dir[dir >= 360] = dir[dir >= 360] - 360

    return spd, dir