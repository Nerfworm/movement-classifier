
import openvr
from utils import get_all_devices

class VRDeviceMapper:
    def __init__(self):
        self.vr_isystem = openvr.init(openvr.VRApplication_Other)
        self.devices = get_all_devices(self.vr_isystem)

    def start_device_indentifier(self):
        
    
    def _identify_device(self, vr_system, device_index):
        device_class = vr_system.getTrackedDeviceClass(device_index)
        if device_class == openvr.TrackedDeviceClass_HMD:
            self._identify_hmd(vr_system, device_index) 
        if device_class == openvr.TrackedDeviceClass_Controller:
            self._identify_controller(vr_system, device_index)
        if device_class == openvr.TrackedDeviceClass_GenericTracker:
            self._identify_tracker

    def _identify_hmd(self, vr_system, device_index):
        hmd_serial_number = self._get_device_serial_number(vr_system, device_index)

    def _identify_controller(self, vr_system, device_index):
        controller_serial_number = self._get_device_serial_number(vr_system, device_index)

    def _get_device_serial_number(vr_system, device_index):
        return vr_system.getStringTrackedDeviceProperty(device_index, openvr.Prop_SerialNumber_String)