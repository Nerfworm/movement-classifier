import openvr
import time
import numpy as np

class VRDataCollector:
    def __init__(self,connected_devices: dict, collection_time_interval: float = 0.01):
        self.connected_devices = connected_devices
        self.collection_time_interval = collection_time_interval
        self.vr_data = openvr.init(openvr.VRApplication_Other)

    def collect_data_once(self):
        timestamp = time.time()
        raw_tracking_data = {}
        poses = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, len(self.connected_devices))
        
        for device, meta in self.connected_devices.items():
            index = meta['index']
            pose = poses[index]
            matrix = self.get_pose_matrix(pose)

            raw_tracking_data [device] = {
                'timestamp': timestamp,
                'pose_is_valid': pose.bPoseIsValid,
                'device_connected': pose.bDeviceIsConnected,
                
                # Position (meters)
                'position_x': matrix[0][3],
                'position_y': matrix[1][3],
                'position_z': matrix[2][3],

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

                'linear_vel_x': pose.vVelocity.v[0],
                'linear_vel_y': pose.vVelocity.v[1],
                'linear_vel_z': pose.vVelocity.v[2],

                'angular_vel_x': pose.vAngularVelocity.v[0],
                'angular_vel_y': pose.vAngularVelocity.v[1],
                'angular_vel_z': pose.vAngularVelocity.v[2],
            }
            print(f"\n\nraw_tracking_data") # debug
        
        # implement data saver object save here
        
    
    def run(self, duration: float = 0):
        self.running = True
        start_time = time.time()

        while self.running:
            # self.collect_data_once()
            print(f"Time: {time.time()}")
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
    