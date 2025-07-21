import shutil

from .util import format_2dp

BYTES_PER_GIGABYTE = 1024 * 1024 * 1024

def bytes_to_gb(bytes):
    return bytes / BYTES_PER_GIGABYTE

class DriveUsageInfo:
    def __init__(self, path="/"):
        self.path = path
        self.total, self.used, self.free = shutil.disk_usage(path)

THRESHOLD_FRACTION = 0.01

def get_alert_threshold(drive_usage_info):
    return bytes_to_gb(drive_usage_info.total) * THRESHOLD_FRACTION

def drive_usage_messages(drive_usage_info):
    return [
        f"Drive: {drive_usage_info.path}",
        f"  Total:           {format_2dp(bytes_to_gb(drive_usage_info.total))} GB",
        f"  Used:            {format_2dp(bytes_to_gb(drive_usage_info.used)) } GB",
        f"  Free:            {format_2dp(bytes_to_gb(drive_usage_info.free)) } GB",
        f"  Alert Threshold: {format_2dp(get_alert_threshold(drive_usage_info))} GB"
    ]

def print_drive_usage(drive_usage_info):
    for message in drive_usage_messages(drive_usage_info):
        print(message)
    
