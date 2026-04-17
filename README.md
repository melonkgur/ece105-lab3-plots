# ECE105 Lab 3 — Sensor Plotting

Short description

This repository generates synthetic temperature sensor data and produces publication-quality visualizations (scatter, overlaid histogram, and box plot) for lab analysis.

## Installation

1. Activate the course environment:

   conda activate ece105

2. Install dependencies with conda or mamba:

   conda install numpy matplotlib

   or

   mamba install numpy matplotlib

(If using pip outside the conda env: pip install numpy matplotlib)

## Usage

Run the standalone script to generate the plots:

    python generate_plots.py

Optional: pass --seed to set the RNG seed, e.g., python generate_plots.py --seed 1234

## Example output

The script writes sensor_analysis.png (a 1x3 figure) containing:

- Scatter plot: sensor readings vs time (Sensor A blue circles, Sensor B orange X markers).
- Overlaid histogram: temperature distributions for both sensors with semi-transparent bars to show overlap.
- Box plot: side-by-side boxplots comparing medians, IQRs, and outliers.

## AI tools used and disclosure

While the code under this repo is human-reviewed, it was primarily generated through the Copilot CLI.
