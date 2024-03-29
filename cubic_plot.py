import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Cubic Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig('Cubic_plot.png', bbox_inches='tight')
