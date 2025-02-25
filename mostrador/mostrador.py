import tkinter as tk
from tkinter import ttk
import subprocess
import platform

def get_cpu_usage():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic cpu get loadpercentage /value", shell=True).decode()
            return float(output.strip().split("=")[-1])
        else:
            output = subprocess.check_output("top -bn1 | grep 'Cpu(s)'", shell=True).decode()
            return float(output.split()[1].replace('%', ''))
    except:
        return 0.0

def get_ram_usage():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /value", shell=True).decode()
            mem_info = output.strip().split("\n")
            free_mem = int(mem_info[0].split("=")[-1])
            total_mem = int(mem_info[1].split("=")[-1])
        else:
            output = subprocess.check_output("free -m", shell=True).decode().split("\n")[1].split()
            total_mem = int(output[1])
            free_mem = int(output[3])
        return 100 - ((free_mem / total_mem) * 100)
    except:
        return 0.0

def get_battery_status():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic Path Win32_Battery Get EstimatedChargeRemaining /value", shell=True).decode()
            return int(output.strip().split("=")[-1]) if "=" in output else "N/A"
        else:
            output = subprocess.check_output("acpi -b", shell=True).decode()
            return int(output.split(",")[1].strip().replace('%', '')) if ',' in output else "N/A"
    except:
        return "N/A"

def update_stats():
    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()
    battery_percent = get_battery_status()
    
    cpu_label["text"] = f"Uso da CPU: {cpu_usage:.2f}%"
    ram_label["text"] = f"Uso da RAM: {ram_usage:.2f}%"
    battery_label["text"] = f"Bateria: {battery_percent}%"
    
    cpu_progress["value"] = cpu_usage
    ram_progress["value"] = ram_usage
    if isinstance(battery_percent, int):
        battery_progress["value"] = battery_percent
    
    root.after(1000, update_stats)

root = tk.Tk()
root.title("Monitor do Sistema")
root.geometry("300x200")

cpu_label = ttk.Label(root, text="Uso da CPU: 0%")
cpu_label.pack(pady=5)
cpu_progress = ttk.Progressbar(root, length=200, mode="determinate")
cpu_progress.pack(pady=5)

ram_label = ttk.Label(root, text="Uso da RAM: 0%")
ram_label.pack(pady=5)
ram_progress = ttk.Progressbar(root, length=200, mode="determinate")
ram_progress.pack(pady=5)

battery_label = ttk.Label(root, text="Bateria: N/A")
battery_label.pack(pady=5)
battery_progress = ttk.Progressbar(root, length=200, mode="determinate")
battery_progress.pack(pady=5)

update_stats()
root.mainloop()