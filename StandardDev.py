import numpy as np


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