from .p_structure import p_structure

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