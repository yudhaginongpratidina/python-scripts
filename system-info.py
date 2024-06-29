import psutil
import platform
from datetime import datetime
import cpuinfo
import socket
import uuid
import re

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


print()
print("=====================================================================")
print("System Information")
print("=====================================================================")
uname = platform.uname()
print(f"System          \t      : {uname.system}")
print(f"Node Name       \t      : {uname.node}")
print(f"Release         \t      : {uname.release}")
print(f"Version         \t      : {uname.version}")
print(f"Machine         \t      : {uname.machine}")
print(f"Processor       \t      : {uname.processor}")
print(f"Processor       \t      : {cpuinfo.get_cpu_info()['brand_raw']}")
print(f"Ip-Address      \t      : {socket.gethostbyname(socket.gethostname())}")
print(f"Mac-Address     \t      : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")
print()

print()
print("=====================================================================")
print("Disk Information")
print("=====================================================================")
partitions = psutil.disk_partitions()
for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint            \t      : {partition.mountpoint}")
        print(f"  File system type      \t      : {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size        \t\t      : {get_size(partition_usage.total)}")
        print(f"  Used              \t\t      : {get_size(partition_usage.used)}")
        print(f"  Free              \t\t      : {get_size(partition_usage.free)}")
        print(f"  Percentage        \t\t      : {partition_usage.percent}%")
        print()
print()