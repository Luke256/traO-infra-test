from exec_cpp import exec_cpp
from plot_times import plot_times

MX_LOGS = [1,2,4,8,16]

def run_test():
    results = {}
    
    for mx_log in MX_LOGS:
        print(f"Running test for {mx_log} MX logs")
        
        times = exec_cpp(mx_log)
        times = sorted(times)
        
        mean = sum(times) / len(times)
        sigma = (sum((t - mean) ** 2 for t in times) / len(times)) ** 0.5
        max_time = max(times)
        min_time = min(times)
        first5th = times[4]
        last5th = times[-5]
        
        results[mx_log] = {
            "times": times,
            "mean": mean,
            "sigma": sigma,
            "max": max_time,
            "min": min_time,
            "first5th": first5th,
            "last5th": last5th
        }
        
    plot_times(results)