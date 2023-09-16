def nb_year(p0: int, percent: float, aug: int, p:int):
    years = 0
    while int(p0) < p:
        p0 = int(p0 + p0 * (percent / 100) + aug)
        years += 1
    return years

if __name__ == "__main__":
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94
    print("All tests passed")