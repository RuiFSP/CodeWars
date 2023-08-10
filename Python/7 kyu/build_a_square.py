def generate_shape(n: int) -> str:
    """
    Generate a shape of height n
    """
    return "\n".join(["+" * n] * n)
    pass


if __name__ == "__main__":
    assert generate_shape(3) == "+++\n+++\n+++"
    assert generate_shape(8) == "++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++"
    print("All tests passed")
