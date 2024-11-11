import subprocess
import time

def exec_cpp(mx_log):
    subprocess.run(["g++", "main.cpp", "-o", "main", "-D", f"MX_LOG={mx_log}"])
    
    times = []
    for _ in range(10):
        start = time.perf_counter()
        subprocess.run(["./main"], stdout=subprocess.DEVNULL)
        end = time.perf_counter()
        times.append((end - start) * 1000)
        
    return times