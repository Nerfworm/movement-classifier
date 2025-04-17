
import openvr
import time

class VRDataCollector:
    def __init__(self):
        self.vr = openvr.init(openvr.VRApplication_Other)

    