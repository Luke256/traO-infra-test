from matplotlib import pyplot as plt

# 計測時間のリストを箱ひげ図で表示する関数
# 各MX_LOGに対して、計測時間のリストを箱ひげ図で表示する

def plot_times(results):
    fig, ax = plt.subplots()
    
    for mx_log, result in results.items():
        ax.boxplot(result["times"], positions=[mx_log], widths=0.6)
        
    ax.set_xlabel("mx_log2")
    ax.set_ylabel("Time (ms)")
    ax.set_title("Execution time")
    
    plt.savefig("times.png")