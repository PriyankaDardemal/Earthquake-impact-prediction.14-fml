"""
Earthquake Impact Prediction - Simple Hackathon Submission (Individual)
Filename: earthquake_predictor.py

This script demonstrates a very simple "impact score" predictor using linear regression
on a tiny synthetic dataset. It's intentionally simple so it can be run locally without
extra data or large dependencies.

How to run:
    python earthquake_predictor.py

You will be prompted to enter:
 - magnitude (e.g., 6.5)
 - population_density (people per sq km, e.g., 1200)
The script outputs a predicted impact score (0 = minimal, higher = more severe).
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Small synthetic dataset (Magnitude, PopulationDensity) -> ImpactScore
# ImpactScore is a made-up number for demonstration purposes.
X = np.array([
    [4.5, 50],
    [5.2, 100],
    [5.8, 300],
    [6.1, 800],
    [6.8, 1200],
    [7.2, 2000],
    [7.8, 5000],
    [8.3, 10000]
], dtype=float)
y = np.array([1, 2, 4, 7, 12, 20, 40, 80], dtype=float)  # made-up impact scores

model = LinearRegression()
model.fit(X, y)

print("Simple Earthquake Impact Predictor")
mag = float(input("Enter earthquake magnitude (e.g., 6.5): ").strip())
pop = float(input("Enter population density (people per sq km, e.g., 1200): ").strip())

inp = np.array([[mag, pop]])
pred = model.predict(inp)[0]

print(f"Predicted impact score: {pred:.2f} (higher means greater expected impact)")

# Simple guideline
if pred < 5:
    print("Guideline: Low to moderate impact — local response likely sufficient.")
elif pred < 20:
    print("Guideline: Significant impact — regional emergency response advised.")
else:
    print("Guideline: Severe impact — national-level emergency response advised.")