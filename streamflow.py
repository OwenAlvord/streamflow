import matplotlib.pyplot as plt
import numpy as np

# Create the NumPy array and separate the dates and five gauge flows
data = np.genfromtxt(
"June-2021-Provo-River-Streamflow-Rates.csv",
delimiter=",",
skip_header=1,
dtype=str
)

x = data[:, 0].astype("datetime64")
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

# Plot the five Provo River gauges
plt.figure(figsize=(12, 5))

plt.plot(x, y_1, color='purple', label='10163000')
plt.plot(x, y_2, color='teal', label='10155200')
plt.plot(x, y_3, color='green', label='10155500')
plt.plot(x, y_4, color='orange', label='10154200')
plt.plot(x, y_5, color='orangered', label='10155000')

plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')

plt.legend(title='Site Numbers')
plt.grid()

plt.xticks(rotation=45)
plt.xlim(np.datetime64('2021-06-01'), np.datetime64('2021-07-01'))

plt.tight_layout()
plt.show()

