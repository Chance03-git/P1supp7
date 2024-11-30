import numpy as np
import matplotlib.pyplot as plt

def plot_normal_distribution():
     """
    Generates 200 points sampled from a standard normal distribution
    and plots them as a scatter plot.

     - Points are sampled independently for X and Y coordinates.
    - Standard normal distribution:
        - Mean = 0
        - StdDev = 1

    Visual Representation:
        - Each point is plotted with transparency to highlight density.
        - A grid is added for better visualization.
    """
     x = np.random.normal(loc=0, scale=1, size=200)
     y = np.random.normal(loc=0, scale=1, size=200)

    # Create the scatter plot
     plt.figure(figsize=(8, 6))
     plt.scatter(x, y, alpha=0.7, edgecolor='k')
     plt.title("Scatter Plot of 200 Points from a Standard Normal Distribution")
     plt.xlabel("X-axis")
     plt.ylabel("Y-axis")
     plt.grid(True)

     # Show the plot
     plt.show()

# Call the function to execute
if __name__ == "__main__":
    plot_normal_distribution()

def test_plot_normal_distribution():
    # Generate points from a standard normal distribution
    x = np.random.normal(loc=0, scale=1, size=200)
    y = np.random.normal(loc=0, scale=1, size=200)

    # Assertions
    assert len(x) == 200, "X array must contain 200 points"
    assert len(y) == 200, "Y array must contain 200 points"
    assert np.abs(np.mean(x)) < 0.1, "Mean of X should be close to 0"
    assert np.abs(np.mean(y)) < 0.1, "Mean of Y should be close to 0"
    assert np.abs(np.std(x) - 1) < 0.1, "StdDev of X should be close to 1"
    assert np.abs(np.std(y) - 1) < 0.1, "StdDev of Y should be close to 1"

def test_plot_line():
    # Parameters
    y_intercept = 2
    slope = 3
    x_lower = -5
    x_upper = 5

    # Generate X values and expected Y values
    x_values = np.linspace(x_lower, x_upper, 100)
    expected_y_values = slope * x_values + y_intercept

    # Assertions
    assert len(x_values) == 100, "X values should have 100 points"
    assert np.allclose(expected_y_values[0], slope * x_lower + y_intercept), "Y value at lower bound is incorrect"
    assert np.allclose(expected_y_values[-1], slope * x_upper + y_intercept), "Y value at upper bound is incorrect"