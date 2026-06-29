import matplotlib.pyplot as plt

data = [40, 25, 15, 15, 5]
labels = ["profit", "rent", "fuel", "SS", "commissions"]

fig, ax = plt.subplots()
pie = ax.pie(data)
ax.pie_label(pie, labels, distance=0.7)
ax.pie_label(pie, "{frac:.1%}", distance=0.4)

plt.show()
