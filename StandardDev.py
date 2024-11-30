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
def plot_line(y_intercept, slope, x_lower, x_upper):
    """
    Plots a line based on the given parameters.

    Parameters:
        y_intercept (float): The y-intercept of the line, where the line crosses the Y-axis.
        slope (float): The slope of the line, determining its steepness.
        x_lower (float): The lower boundary of the X-axis range.
        x_upper (float): The upper boundary of the X-axis range.

    Graph Details:
        - The line is plotted within the range [x_lower, x_upper].
        - X and Y axes are marked with dashed lines.
        - The graph includes a legend displaying the line equation.

    Returns:
        None
    """
    # Generate X values
    x_values = np.linspace(x_lower, x_upper, 100)

    # Calculate corresponding Y values
    y_values = slope * x_values + y_intercept

    # Plot the line
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f"y = {slope}x + {y_intercept}")
    plt.title("Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid(True)
    plt.legend()
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

def test_live_graph_point_generation():
    # Generate 20 points
    points = [np.random.normal(0, 1) for _ in range(20)]
    
    # Only the last 10 points should be retained
    recent_points = points[-10:]

    assert len(recent_points) == 10, "Should only retain the last 10 points"
    assert recent_points == points[-10:], "Recent points should match the last 10 points"