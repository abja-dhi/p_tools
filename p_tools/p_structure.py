import mikeio_DHI
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os
import pkg_resources

class p_structure:
    def __init__(self,
                 name="P1",
                 xyz=[],
                 ttt=[],
                 legend="",
                 fname="",
                 item="",
                 icol=[],
                 bins=[],
                 vref="MSL",
                 href="EPSG:4326",
                 source="",
                 ndec=3,
                 ascii=".xlsx") -> None:
        self.name = name
        self.item = item
        self.legend = legend
        self.fname = fname
        self.date = datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
        self.author = "DHI"
        self.ndec = ndec
        self.source = source
        self.python = sys.version
        self.user = os.getlogin()
        self.icol = icol
        self.ttt = ttt
        self.xyz = xyz
        self.ascii = ascii
        self.figure = ".jpg"
        self.table = ".png"
        self.reso = 600
        self.TimeAxisType = ""
        self.TimeFormat = "%Y-%m-%d %H:%M:%S"
        self.tref = "UTC"
        self.href = href
        self.vref = vref
        self.subseries = 0
        self.fontsize = 9
        self.delval = -9999
        self.group = "Omni"
        self.title = "Omni"
        self.load_Colors()
        LineOrder   = ['-', '--', '-.', ':']
        MarkerOrder = ['.','o', 'x', 's', '^']
        self.LineOrder = LineOrder * 15
        self.MarkerOrder = MarkerOrder * 12
        
        self.icol = icol
        #if type(self.icol) == type(self.item) == np.ndarray:
        #    if len(self.icol) != len(self.item):
        #        raise Exception("Length of 'item' is not equal to length of 'icol'")
        #elif type(self.icol) != type(self.item):
        #    raise Exception("Types of 'icol' and 'item' are not the same!")
        
        self.p_item()
        self.p_read()
        self.p_heading()
        self.bins = bins
        
    def __str__(self) -> str:
        string = "p_structure of " + self.label + " from " + self.fname + "\n"
        string = string + "bins = " + str(self.bins) + "\n"
        return string
    
    def p_item(self):
        if "Wind Speed" in self.item or "WS" in self.item:
            self.label = "Wind Speed"
            self.unit = "m/s"
            self.isdir = 0
            self.isspec = 0
        elif "Curren Speed" in self.item or "CS" in self.item:
            self.label = "Current Speed"
            self.unit = "m/s"
            self.isdir = 0
            self.isspec = 0
        elif "Hm0" in self.item or "Significant Wave Height" in self.item or "Sig. Wave Height" in self.item:
            self.label = "Sig. Wave Height"
            self.unit = "m"
            self.isdir = 0
            self.isspec = 0

    def load_Colors(self):
        ColorOrderPath = pkg_resources.resource_filename('p_tools', 'ColorOrder.csv')
        ColorMapPath = pkg_resources.resource_filename('p_tools', 'ColorMap.csv')
        ColorOrder = pd.read_csv(ColorOrderPath, header=None).to_numpy()
        ColorMap = pd.read_csv(ColorMapPath, header=None)
        self.ColorOrder = ColorOrder
        self.ColorMap = ColorMap
        return

    def p_read(self):
        df = mikeio_DHI.read(self.fname)
        df = df.sel(time=slice(self.ttt[0].strftime("%Y-%m-%d %H:%M"), self.ttt[1].strftime("%Y-%m-%d %H:%M")))
        try:
            self.data = df[self.icol - 1].values
            self.datetime = df.time
        except:
            raise NameError("The file couldn't be found!")
        
        return
    
    def p_heading(self):
        self.xyz_str = self._create_xyz_str(self.xyz, self.ndec)
        self.ttt_str, self.ttt_str_long = self._create_ttt_str(self.ttt)
        self.heading = [self.item + " " + self.xyz_str, self.ttt_str_long]

    def _create_xyz_str(self, xyz, ndec=3):
        degree_sign = u'\N{DEGREE SIGN}'
        if len(xyz) == 2:
            xyz_str = "(" + str(np.round(xyz[0], ndec)) + degree_sign + "W; " + str(np.round(xyz[1], 3)) + degree_sign + "N)"
        elif len(xyz) == 3:
            xyz_str = "(" + str(np.round(xyz[0], ndec)) + degree_sign + "W; " + str(np.round(xyz[1], 3)) + degree_sign + "N; d=" + str(np.round(xyz[2], 2)) + " mMSL)"
        
        return xyz_str
    
    def _create_ttt_str(self, ttt):
        t1 = ttt[0].strftime("%Y-%m-%d")
        t2 = ttt[1].strftime("%Y-%m-%d")
        ttt_str = "(" + t1 + "_" + t2 + ")"
        ttt_str_long = ttt_str
        if len(ttt) == 3:
            if ttt[2] > 30:
                ttt[2] = ttt[2] / 60
            delta_sign = u'\N{GREEK CAPITAL LETTER DELTA}'
            ttt_str_long = "(" + t1 + "_" + t2 + "; " + delta_sign + "t=" + str(np.round(ttt[2], 1)) + "h)"
        return ttt_str, ttt_str_long
    
