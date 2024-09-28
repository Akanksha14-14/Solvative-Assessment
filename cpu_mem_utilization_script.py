import psutil
import os
#data
# Function to check CPU usage
def check_cpu_usage():
    print("---------------------------------")
    print("CPU Usage:")
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Load: {cpu_usage}%")
    print("---------------------------------")

# Function to check memory usage
def check_memory_usage():
    print("Memory Usage:")
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    print(f"Memory Usage: {memory_usage}%")
    print("---------------------------------")

# Function to list top 5 processes by CPU usage
def top_cpu_processes():
    print("Top 5 CPU-consuming processes:")
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']),
                       key=lambda p: p.info['cpu_percent'], reverse=True)[:5]
    for process in processes:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, CPU Usage: {process.info['cpu_percent']}%, Memory Usage: {process.info['memory_percent']}%")
    print("---------------------------------")

# Function to list top 5 processes by memory usage
def top_memory_processes():
    print("Top 5 Memory-consuming processes:")
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']),
                       key=lambda p: p.info['memory_percent'], reverse=True)[:5]
    for process in processes:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, CPU Usage: {process.info['cpu_percent']}%, Memory Usage: {process.info['memory_percent']}%")
    print("---------------------------------")

# Main function to call all the checks
def main():
    check_cpu_usage()
    check_memory_usage()
    
    top_cpu_processes()
    top_memory_processes()

if __name__ == "__main__":
    main()
