#1.Linechart

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,13,18,20]

plt.plot(x,y, marker='o', linestyle='-', color='r', label='temperature')
plt.title('Daily temperature trend')

plt.xlabel('Time (hour)')
plt.ylabel('Temperature (C)')

plt.legend()

plt.grid(True)

plt.savefig("./Linechart.png")

plt.show()