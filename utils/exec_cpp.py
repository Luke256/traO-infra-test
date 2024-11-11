import subprocess
import time
import tqdm
from config import ITERATIONS

def exec_cpp(mx_log):
    subprocess.run(["g++", "main.cpp", "-o", "main", "-D", f"MX_LOG={mx_log}"])
    
    times = []
    for _ in tqdm.tqdm(range(ITERATIONS), ascii=True):
        start = time.perf_counter()
        subprocess.run(["./main"], stdout=subprocess.DEVNULL)
        end = time.perf_counter()
        times.append((end - start) * 1000)
        
    return times