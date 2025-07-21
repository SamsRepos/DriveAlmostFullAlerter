import shutil

from .util import format_2dp

BYTES_PER_GIGABYTE = 1024 * 1024 * 1024

def bytes_to_gb(bytes):
    return bytes / BYTES_PER_GIGABYTE

class DriveUsageInfo:
    def __init__(self, path="/"):
        self.path = path
        self.total, self.used, self.free = shutil.disk_usage(path)

class DriveUsage:
    def __init__(self, alert_threshold_fraction):
        self.alert_threshold_fraction = alert_threshold_fraction

    def get_alert_threshold(self, drive_usage_info):
        return bytes_to_gb(drive_usage_info.total) * self.alert_threshold_fraction

    def drive_usage_messages(self, drive_usage_info):
        return [
            f"Drive: {drive_usage_info.path}",
            f"  Total:           {format_2dp(bytes_to_gb(drive_usage_info.total))} GB",
            f"  Used:            {format_2dp(bytes_to_gb(drive_usage_info.used)) } GB",
            f"  Free:            {format_2dp(bytes_to_gb(drive_usage_info.free)) } GB",
            f"  Alert Threshold: {format_2dp(self.get_alert_threshold(drive_usage_info))} GB"
        ]

    def print_drive_usage(self, drive_usage_info):
        for message in self.drive_usage_messages(drive_usage_info):
            print(message)
    
