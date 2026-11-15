import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
"""Load dates and streamflow data from the CSV file."""
data = np.genfromtxt(
filename,
delimiter=",",
skip_header=1,
dtype=str
)

dates = data[:, 0].astype("datetime64")

y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

flows = np.column_stack((y_1, y_2, y_3, y_4, y_5))

return dates, flows


def plot_streamflow(dates, flows, sites):
"""Plot the streamflow data for all five gauges."""
plt.figure(figsize=(12, 5))

colors = ['purple', 'teal', 'green', 'orange', 'orangered']

for i in range(len(sites)):
plt.plot(dates, flows[:, i], color=colors[i], label=sites[i])

plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.legend(title='Site Numbers')
plt.grid()
plt.xticks(rotation=45)
plt.xlim(np.datetime64('2021-06-01'), np.datetime64('2021-07-01'))

plt.tight_layout()
plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)
