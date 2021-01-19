import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LOG_FILENAME = 'PyBatteryLog.csv'

data = pd.read_csv(LOG_FILENAME)
x = data['timestamp']
x = x - x[0]
y = data['BatteryLifePercent']
'''
charging = data['BatteryFlag']
charging = (charging & 8)
'''
charging = data['ACLineStatus']

fig, ax = plt.subplots()
ax.set_xlim(0, x[len(x) - 1] + 10)
ax.set_ylim(0, 105)
# ax.plot(x, y)
ax.scatter(x=x, y=y, s=2, c=charging, cmap='bwr_r')

ax.set(xlabel='time (s)', ylabel='BatteryLifePercent (%)')
ax.grid()

fig.savefig("PyBatteryView.png", dpi=300)
plt.show()
