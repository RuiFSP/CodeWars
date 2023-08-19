import math


def triangle_type(a: int, b: int, c: int) -> int:
    """
    Returns the type of triangle.
    0: Not a triangle
    1: Acute triangle
    2: Right angle triangle
    3: Obtuse triangle
    """
    # Check if the sides can form a triangle
    if a + b <= c or b + c <= a or c + a <= b:
        return 0

    # Calculate the squares of the side lengths
    a_squared = a * a
    b_squared = b * b
    c_squared = c * c

    # Check for right angle (90°)
    if a_squared + b_squared == c_squared or b_squared + c_squared == a_squared or c_squared + a_squared == b_squared:
        return 2

    # Calculate the angles using the Law of Cosines
    alpha = math.acos((b_squared + c_squared - a_squared) / (2 * b * c))
    beta = math.acos((c_squared + a_squared - b_squared) / (2 * c * a))
    gamma = math.acos((a_squared + b_squared - c_squared) / (2 * a * b))

    # Convert angles to degrees
    alpha_deg = math.degrees(alpha)
    beta_deg = math.degrees(beta)
    gamma_deg = math.degrees(gamma)

    # Check for obtuse angle (> 90°)
    if alpha_deg > 90 or beta_deg > 90 or gamma_deg > 90:
        return 3

    # If none of the above conditions were met, it's an acute triangle
    return 1


if __name__ == "__main__":
    assert triangle_type(7, 3, 2) == 0
    assert triangle_type(2, 4, 6) == 0
    assert triangle_type(8, 5, 7) == 1
    assert triangle_type(3, 4, 5) == 2
    assert triangle_type(7, 12, 8) == 3
    print("All tests passed")
