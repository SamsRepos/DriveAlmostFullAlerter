from time import sleep
import os
from datetime import datetime
import win32api
import winsound

from modules.available_drives import *
from modules.drive_usage import *

clear = lambda: os.system('cls')

def datetime_formatted(dt):
  return dt.strftime('%H:%M:%S %d/%m/%Y')
#  return dt.strftime('%d/%m/%Y, %H:%M:%S')

GIGABYTES_THRESHOLD = 5
SECONDS_BETWEEN_CHECKS = 9

DIALOG_TITLE = "LOW DRIVE SPACE!"

if __name__ == '__main__':
    while True:
        drives_infos = []
        console_messages = []
        
        drives = available_drives()
        console_messages.append(f"{len(drives)} available drives: {drives}")
        console_messages.append("")
        
        for drive in drives:
            drives_infos.append(DriveUsageInfo(path=drive))
        
        for info in drives_infos:
            for message in drive_usage_messages(info):
                console_messages.append(message)
            console_messages.append("")
        
        clear()
        for message in console_messages:
            print(message)
        print(f"Last update: {datetime_formatted(datetime.now())}")
        
        any_drive_almost_full = False
        dialog_messages = []
        for info in drives_infos:
            if bytes_to_gb(info.free) < GIGABYTES_THRESHOLD:
                any_drive_almost_full = True
                dialog_messages.append(f"{info.path} drive is almost full")
                dialog_messages.append("")
                for message in drive_usage_messages(info):
                    dialog_messages.append(message)
                dialog_messages.append("")

        if any_drive_almost_full:
            winsound.PlaySound('./sfx/alert.wav', winsound.SND_FILENAME)
            dialog_message = "\n".join(dialog_messages)
            win32api.MessageBox(0, dialog_message, DIALOG_TITLE, 0x00001000)
        
        sleep(SECONDS_BETWEEN_CHECKS)
