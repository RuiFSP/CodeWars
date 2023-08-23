def gps(s:float, x:list) -> int:
    """
    Calculate the maximum average speed in km/h from a list of distances and time intervals.

    Args:
        s (float): Time interval in seconds.
        x (list): List of distances traveled at each time interval.

    Returns:
        int: Maximum average speed in km/h.
    """
    if len(x) <= 1:
        return 0

    speeds = [(x[i + 1] - x[i]) * 3600 / s for i in range(len(x) - 1)]

    return int(max(speeds))


# Test cases
test_cases = [
    ([0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61], 20, 41),
    ([0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25], 12, 219)
]

if __name__ == "__main__":
    for x, s, expected in test_cases:
        result = gps(s, x)
        assert result == expected, f"For input s={s} and x={x}, expected {expected} but got {result}"
    print("Well done! Go check your code")

