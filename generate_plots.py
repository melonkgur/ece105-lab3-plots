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
