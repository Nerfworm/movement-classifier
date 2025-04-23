from vr_data_collector import VRDataCollector
from data_saver import DataSaver
from config import CONNECTED_DEVICES

data_label = "testing"
duration_in_seconds = 10
collection_interval_seconds = .1

data_saver = DataSaver(data_label)
data_collector = VRDataCollector(CONNECTED_DEVICES, data_saver, collection_interval_seconds)
# data_collector.collect_data_once()
data_collector.run(duration_in_seconds)