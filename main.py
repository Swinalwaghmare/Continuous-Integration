import matplotlib.pyplot as plt 

fig, ax = plt.subplots()

fruits = ["apple", "bluberry", "cherry", "orange"]
counts = [140, 10, 30, 55]
bar_label = ['red', 'blue', '_red', "orange"]
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_label, color = bar_colors)
ax.set_ylabel("fruit supply")
ax.set_title("Fruits supply by kind and color")
ax.legend(title='Fruit Color')

plt.savefig('bars.png', bbox_inches='tight')