from matplotlib import pyplot as plt

# results.timesを箱ひげ図で表示する関数
# 各結果のスケールは異なる可能性があるため、グラフは分けて表示する
# resultsの要素数は可変であることを想定している
def plot_times(results):
    fig, axs = plt.subplots(1, len(results), figsize=(5 * len(results), 10))
    
    for i, (mx_log, result) in enumerate(results.items()):
        times = result["times"]
        
        axs[i].boxplot(times, vert=True)
        axs[i].set_title(f"MX_LOG={mx_log}")
        axs[i].set_ylabel("Time (ms)")
    
    plt.tight_layout()
    plt.savefig("times.png", dpi=200)