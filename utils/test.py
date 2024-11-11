from utils.exec_cpp import exec_cpp
from utils.plot_times import plot_times
from utils.send2traq import send2traq

from config import MX_LOGS, TEST_NAME

def encode_result(result):
    message = ""

    # MD Style
    # create table

    message += f"# {TEST_NAME}\n"

    message += "| mx log | 平均 | 標準偏差 | 最大 | 最小 | 最初から5番目 | 最後から5番目 |\n"
    message += "| --- | --- | --- | --- | --- | --- | --- |\n"

    for mx_log, res in result.items():
        message += f"| {mx_log} | {res['mean']:.2f} | {res['sigma']:.2f} | {res['max']:.2f} | {res['min']:.2f} | {res['first5th']:.2f} | {res['last5th']:.2f} |\n"

    message += "\n"
    message += "```python\n"
    message += "{\n"
    for mx_log, res in result.items():
        message += f"    {mx_log}: ["
        message += ", ".join([f"{t:.2f}" for t in res["times"]])
        message += "],\n"
    message += "}\n"
    message += "```\n"

    return message

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
        
    # plot_times(results)

    encoded_result = encode_result(results)

    send2traq(encoded_result)