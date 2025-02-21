import psutil
import os
"""
# CPU usage 
cpu_percentage = psutil.cpu_percent(interval=1) 
 
# Memory usage 
memory = psutil.virtual_memory() 
memory_percentage = memory.percent 
 
print(f"CPU Usage: {cpu_percentage}%") 
print(f"Memory Usage: {memory_percentage}%")
"""
"""
def CPU_utilization():
    

CPU_utilization()
"""



start = psutil.cpu_percent(interval=1)
print("First check")
print(abs(psutil.cpu_percent(interval=1) - start))
print("Second check")
print(psutil.cpu_percent(interval=1))
print(f"CPU utilization: {psutil.cpu_percent()}%")
print(f"Memory utilization: {psutil.virtual_memory().percent}%")
# Get memory usage 
memory_info = psutil.virtual_memory() 
memory_usage = memory_info.percent 
print(f"Memory Usage: {memory_usage}%")


def getCPUtemperature():
    res = os.popen('vcgencmd mesaure_temp').readline()
    retrun(res.replace("temp=","").replace("'C\n",""))


