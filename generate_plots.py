"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""


import numpy as np

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed: int):
    """Generate synthetic temperature sensor readings and timestamps.

    Parameters
    ----------
    seed : int
        Integer seed used to initialize numpy.random.default_rng for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        1-D array of shape (200,) with dtype float64 containing temperature
        readings for Sensor A sampled from a normal distribution with mean
        25.0 and standard deviation 3.0 (degrees Celsius).
    sensor_b : numpy.ndarray
        1-D array of shape (200,) with dtype float64 containing temperature
        readings for Sensor B sampled from a normal distribution with mean
        27.0 and standard deviation 4.5 (degrees Celsius).
    timestamps : numpy.ndarray
        1-D array of shape (200,) with dtype float64 containing timestamps
        uniformly sampled from the interval [0, 10] (seconds) and sorted in
        increasing order.
    """
    rng = np.random.default_rng(seed)
    n = 200

    # Timestamps uniformly drawn from 0..10 seconds and sorted for time-series
    timestamps = rng.uniform(0.0, 10.0, size=n)
    timestamps.sort()

    # Sensor readings: normal distributions with specified means and stddevs
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n).astype(np.float64)

    return sensor_a, sensor_b, timestamps

def plot_scatter(sensor_a: np.ndarray, sensor_b: np.ndarray, timestamps: np.ndarray, ax):
    """Draw a scatter plot of two sensor temperature series on an Axes.

    The function plots sensor_a and sensor_b versus timestamps on the
    provided Matplotlib Axes object. It styles points to match the notebook
    visualizations: Sensor A in blue circles, Sensor B in orange X markers,
    with semitransparent points to reveal overlap. Axes labels, title, legend,
    and a light grid are added. The Axes object is modified in place and
    nothing is returned.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1-D array of shape (N,) containing Sensor A temperature readings
        (float-like).
    sensor_b : numpy.ndarray
        1-D array of shape (N,) containing Sensor B temperature readings
        (float-like).
    timestamps : numpy.ndarray
        1-D array of shape (N,) containing timestamps (seconds) corresponding
        to the readings. Should be sorted for time-series clarity but the
        function does not require it.
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance on which to draw the scatter plot.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    # Local import to avoid forcing matplotlib at module import time
    import matplotlib.pyplot as _plt

    # Ensure arrays are numpy arrays
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)
    timestamps = np.asarray(timestamps)

    ax.scatter(timestamps, sensor_a, c='C0', s=25, alpha=0.7, label='Sensor A')
    ax.scatter(timestamps, sensor_b, c='C1', s=35, alpha=0.7, label='Sensor B', marker='x')

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Scatter of sensor readings vs time')
    ax.legend()
    ax.grid(alpha=0.3)
    # No return; modifies ax in place

def plot_histogram(sensor_a: np.ndarray, sensor_b: np.ndarray, ax):
    """Draw an overlaid histogram of two sensor temperature distributions.

    The function computes bin edges that span both input arrays and plots
    semi-transparent histograms for sensor_a and sensor_b on the provided
    Matplotlib Axes. Axis labels, title, legend, and a light grid are added.
    The Axes object is modified in place and nothing is returned.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1-D array of shape (N,) containing Sensor A temperature readings
        (float-like).
    sensor_b : numpy.ndarray
        1-D array of shape (N,) containing Sensor B temperature readings
        (float-like).
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance on which to draw the histogram.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    # Local import to avoid forcing matplotlib at module import time
    import matplotlib.pyplot as _plt

    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    # Determine bin edges that cover both datasets with a small margin
    min_edge = float(min(sensor_a.min(), sensor_b.min()) - 1.0)
    max_edge = float(max(sensor_a.max(), sensor_b.max()) + 1.0)
    bins = np.linspace(min_edge, max_edge, 25)

    ax.hist(sensor_a, bins=bins, alpha=0.6, color='C0', label='Sensor A')
    ax.hist(sensor_b, bins=bins, alpha=0.6, color='C1', label='Sensor B')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Overlaid histogram of Sensor A and Sensor B temperature distributions')
    ax.legend()
    ax.grid(alpha=0.3)
    # modifies ax in place

def plot_boxplot(sensor_a: np.ndarray, sensor_b: np.ndarray, ax):
    """Draw side-by-side box plots comparing two sensor distributions.

    The function places box plots for sensor_a and sensor_b on the provided
    Matplotlib Axes. Boxes are styled with a light fill color and a red median
    line for clarity. Axis labels, title, and a subtle horizontal grid are
    added. The Axes object is modified in place and nothing is returned.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1-D array of shape (N,) containing Sensor A temperature readings
        (float-like).
    sensor_b : numpy.ndarray
        1-D array of shape (N,) containing Sensor B temperature readings
        (float-like).
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance on which to draw the box plots.

    Returns
    -------
    None
        The function modifies the provided Axes in place.
    """
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    data = [sensor_a, sensor_b]
    labels = ['Sensor A', 'Sensor B']

    bp = ax.boxplot(data, labels=labels, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='C0'),
                    medianprops=dict(color='red'),
                    whiskerprops=dict(color='C0'), capprops=dict(color='C0'))

    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Box plot of Sensor A and Sensor B')
    ax.grid(axis='y', alpha=0.3)
    # modifies ax in place

def main(seed: int = 3557):
    """Generate data and produce a 1x3 figure with the three analyses.

    The function generates synthetic sensor data using ``generate_data``,
    creates a 1x3 Matplotlib figure (scatter, histogram, boxplot), and saves
    the combined figure to disk as ``sensor_analysis.png`` with 150 DPI and a
    tight bounding box.

    Parameters
    ----------
    seed : int, optional
        RNG seed passed to ``generate_data`` for reproducibility. Default is
        3557 (the seed used in the notebook).

    Returns
    -------
    None
        The function saves the figure to disk and does not return a value.
    """
    import matplotlib.pyplot as plt
    import argparse

    # Generate data
    sensor_a, sensor_b, timestamps = generate_data(seed)

    # Create 1x3 subplot figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Plot each panel using the helper functions
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    plt.tight_layout()

    out_path = 'sensor_analysis.png'
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    # Allow overriding the seed from the command line
    import argparse
    parser = argparse.ArgumentParser(description='Generate sensor plots')
    parser.add_argument('--seed', type=int, default=3557, help='RNG seed (default: 3557)')
    args = parser.parse_args()
    main(seed=args.seed)
