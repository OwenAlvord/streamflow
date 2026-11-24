import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    data = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        dtype=str
    )

    dates = data[:, 0].astype("datetime64")
    flows = data[:, 1:6].astype(float)

    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.figure(figsize=(12, 5))

    plt.plot(dates, flows[:, 0], color='purple', label=sites[0])
    plt.plot(dates, flows[:, 1], color='teal', label=sites[1])
    plt.plot(dates, flows[:, 2], color='green', label=sites[2])
    plt.plot(dates, flows[:, 3], color='orange', label=sites[3])
    plt.plot(dates, flows[:, 4], color='orangered', label=sites[4])

    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.legend(title='Site Numbers')
    plt.grid()
    plt.xticks(rotation=45)
    plt.xlim(np.datetime64('2021-06-01'), np.datetime64('2021-07-01'))

    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


def summarize(dates, flows, sites):
    # Excel check for gauge 10163000: MAX = 131 , AVERAGE = 56.95
    """Calculate, print, and save summary statistics for each gauge."""

    print("\nStreamflow Summary")
    print(f"{'Gauge':<12}{'Max (cfs)':>12} {'Date of max':<20}{'Min (cfs)':>12}{'Avg (cfs)':>12}")

    rows = []

    for i, site in enumerate(sites):
        gauge_flows = flows[:, i]

        max_index = np.argmax(gauge_flows)
        max_flow = np.max(gauge_flows)
        max_date = str(dates[max_index])[:16].replace("T", " ")
        min_flow = np.min(gauge_flows)
        avg_flow = np.mean(gauge_flows)

        print(f"{site:<12}{max_flow:>12.1f} {max_date:<20}{min_flow:>12.1f}{avg_flow:>12.1f}")

        rows.append((site, max_flow, max_date, min_flow, avg_flow))

    with open("streamflow_summary.csv", "w") as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")
        for row in rows:
            file.write(f"{row[0]},{row[1]:.1f},{row[2]},{row[3]:.1f},{row[4]:.1f}\n")


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)

summarize(dates, flows, sites)

# AI NOTE: this threshold code was written with AI help. It asks for a threshold,
# then for each gauge compares every reading to it (giving True/False values),
# np.sum counts the True values, and each 15-minute reading counts as 0.25 hours.
threshold = float(input("\nEnter a flow threshold in cfs: "))
for i, site in enumerate(sites):
    hours = np.sum(flows[:, i] > threshold) * 0.25
    print(f"Gauge {site}: {hours:.2f} hours above {threshold} cfs")
A
