from data_saver import DataSaver
import openvr
import time
import numpy as np

class VRDataCollector:
    def __init__(self, connected_devices: dict, data_saver: DataSaver, collection_time_interval: float = 0.01):
        self.connected_devices = connected_devices
        self.collection_time_interval = collection_time_interval
        self.vr_data = openvr.init(openvr.VRApplication_Other)
        self.data_saver = data_saver

    def collect_data_once(self):
        timestamp = time.time()
        raw_tracking_data = {}
        poses = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, len(self.connected_devices))
        
        for device, meta in self.connected_devices.items():
            index = meta['index']
            pose = poses[index]
            matrix = self._get_pose_matrix(pose)

            raw_tracking_data [device] = {
                'timestamp': timestamp,
                'pose_is_valid': pose.bPoseIsValid,
                'device_connected': pose.bDeviceIsConnected,
                
                'position_x (m)': matrix[0][3],
                'position_y (m)': matrix[1][3],
                'position_z (m)': matrix[2][3],

                # Orientation matrix (rotation basis vectors)
                'orientation_right_x': matrix[0][0],
                'orientation_right_y': matrix[1][0],
                'orientation_right_z': matrix[2][0],

                'orientation_up_x': matrix[0][1],
                'orientation_up_y': matrix[1][1],
                'orientation_up_z': matrix[2][1],

                'orientation_forward_x': matrix[0][2],
                'orientation_forward_y': matrix[1][2],
                'orientation_forward_z': matrix[2][2],

                'linear_vel_x (m/s)': pose.vVelocity.v[0],
                'linear_vel_y (m/s)': pose.vVelocity.v[1],
                'linear_vel_z (m/s)': pose.vVelocity.v[2],

                'angular_vel_x (rad/s)': pose.vAngularVelocity.v[0],
                'angular_vel_y (rad/s)': pose.vAngularVelocity.v[1],
                'angular_vel_z (rad/s)': pose.vAngularVelocity.v[2],
            }
        
        self.data_saver.save_raw_data(raw_tracking_data)
        
    
    def run(self, duration: float = 0):
        self.running = True
        start_time = time.time()

        while self.running:
            self.collect_data_once()
            if duration and (time.time() - start_time) >= duration:
                break
            time.sleep(self.collection_time_interval)

    def stop(self):
        self.running = False

    def _get_pose_matrix(self, pose):
        mat = pose.mDeviceToAbsoluteTracking
        return np.array([
            [mat[0][0], mat[0][1], mat[0][2], mat[0][3]],
            [mat[1][0], mat[1][1], mat[1][2], mat[1][3]],
            [mat[2][0], mat[2][1], mat[2][2], mat[2][3]],
        ])
    