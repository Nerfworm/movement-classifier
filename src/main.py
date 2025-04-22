from vr_data_collector import VRDataCollector
from config import CONNECTED_DEVICES

data_collector = VRDataCollector(CONNECTED_DEVICES, .5)
# data_collector.collect_data_once()
data_collector.run(5)