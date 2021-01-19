import time
import os.path
from ctypes import *

LOG_FILENAME = 'PyBatteryLog.csv'
LOG_DELAY_S = 5


# This assumes that if the file already exists, it is a valid file from a previous session
def setup_log_file(filename):
    if not os.path.isfile(filename):
        f = open(filename, "x")
        f.write('timestamp,ACLineStatus,BatteryFlag,BatteryLifePercent,SystemStatusFlag,BatteryLifeTime,BatteryFullLifeTime\n')
        f.close()


class SYSTEM_POWER_STATUS(Structure):
    _fields_ = [
        ('ACLineStatus', c_byte),
        ('BatteryFlag', c_byte),
        ('BatteryLifePercent', c_byte),
        ('SystemStatusFlag', c_byte),
        ('BatteryLifeTime', c_ulong),
        ('BatteryFullLifeTime', c_ulong)]


setup_log_file(LOG_FILENAME)
lpSystemPowerStatus = SYSTEM_POWER_STATUS()

while True:
    if windll.kernel32.GetSystemPowerStatus(byref(lpSystemPowerStatus)) == 0:
        print("ERROR: the function GetSystemPowerStatus() fails")
    else:
        f = open(LOG_FILENAME, "a")
        f.write(str(int(time.time())) + ',')
        f.write(str(lpSystemPowerStatus.ACLineStatus) + ',')
        f.write(str(lpSystemPowerStatus.BatteryFlag) + ',')
        f.write(str(lpSystemPowerStatus.BatteryLifePercent) + ',')
        f.write(str(lpSystemPowerStatus.SystemStatusFlag) + ',')
        f.write(str(lpSystemPowerStatus.BatteryLifeTime) + ',')
        f.write(str(lpSystemPowerStatus.BatteryFullLifeTime) + '\n')
        f.close()

        print(lpSystemPowerStatus.BatteryLifePercent)

    time.sleep(LOG_DELAY_S)
