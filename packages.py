import os
import shutil

print(os.getcwd())

total, used, free = shutil.disk_usage("/")

print(f"Total space is: {total // (2**30)}GB")
print(f"Used space is: {used // (2**30)}GB")
print(f"Free space is: {free // (2**30)}GB")
