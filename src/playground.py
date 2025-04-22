import openvr
from config import CONNECTED_DEVICES
import time

vr_data = openvr.init(openvr.VRApplication_Other)

poses = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(
    openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount
)

def get_device_xyz(device_index):
    pose = poses[device_index]
    pose_matrix = pose.mDeviceToAbsoluteTracking
    x = pose_matrix[0][3]
    y = pose_matrix[1][3]
    z = pose_matrix[2][3]
    return x, y, z

for i in CONNECTED_DEVICES:
    print(f'\nDevice:\n{i}')
    print(f'Position(x,y,z): {get_device_xyz(CONNECTED_DEVICES[i]['index'])}')

# print(f"Position: x={x:.4f}, y={y:.4f}, z={z:.4f}")

# time.sleep(0.51)



import numpy as np
from scipy.spatial.transform import Rotation as R