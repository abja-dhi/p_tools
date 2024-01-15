from p_tools import p_structure
from p_tools import uv2spddir
from p_tools import p_monthly
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import skew
from p_tools import p_stats
from scipy.stats.mstats import mquantiles
import mikeio
from matplotlib.transforms import Bbox

xyz = np.array([-124.794, 41.137, 1748.121])
ttt = [datetime(1979, 1, 1, 0, 0, 0), datetime(2022, 1, 1, 0, 0, 0), 60]
fname = r'D:\Personal\OneDrive - DHI\Humboldt\Data\GWM\Total\Total.dfs0'
Hm0 = p_structure(name="OCS-P 0561", xyz=xyz, ttt=ttt, legend="GWM", fname=fname, item="Hm0", icol=1, bins=np.arange(0, 15.5, 0.5), ndec=2)
#print(Hm0.bins)
Hm0 = p_monthly(Hm0)
#Hm0.data.shape
Hm0.bins


stats = p_stats(Hm0)
Q = np.array([])
for i in range(Hm0.data.shape[1]):
    Q = np.append(Q, np.nanquantile(Hm0.data[:, i], 0.5))
print(stats)
Hm0.bins

heading = " ".join([Hm0.name + Hm0.xyz_str]) + "\n" + " ".join(["Statistics", Hm0.ttt_str_long.replace("_", "-"), Hm0.legend, Hm0.group[-1]])

fig = plt.figure(0)
#mngr = plt.get_current_fig_manager()
#geom = mngr.window.geometry()
#x, y, dx, dy = geom.getRect()
#print(x, y, dx, dy)
#mngr.window.setGeometry(int(x/2), int(y/2), int(dx*3), int(dy))
ax = fig.add_subplot()
ax.plot(stats.MAX[1:], color=Hm0.ColorOrder[1, :], linewidth=1, linestyle='-.')
ax.plot(stats.MEAN[1:], color=Hm0.ColorOrder[0, :], linewidth=1, linestyle='-.')
ax.plot(stats.MIN[1:], color=Hm0.ColorOrder[2, :], linewidth=1, linestyle='-.')
ax.plot(stats.MEAN[1:] + stats.STD[1:], color="black", marker="+", linestyle="none")
ax.plot(stats.MEAN[1:] - stats.STD[1:], color="black", marker="+", linestyle="none")
ax.set_title(heading, fontweight="normal")
ax.legend(["MAX", "MEAN", "MIN", "+/- STD"])
ax.set_xlim(0,len(Hm0.group)-2)
ax.set_ylabel(" ".join([Hm0.label, "["+Hm0.unit+"]"]))
ax.set_ylim(Hm0.bins[0], Hm0.bins[-1])
ax.set_yticks(Hm0.bins)
ax.grid()
ax.set_xticks(np.arange(0, len(Hm0.group)-1,1))
ax.set_xticklabels(Hm0.title[1:])



#fpos = ax.get_position()
#npos = [fpos.x0/2, fpos.y0/2, fpos.width*4, fpos.height]
#ax.set_position(npos)

plt.show()