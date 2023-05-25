def in_array(array1, array2):
    return sorted({sub for sub in array1 for word in array2 if sub in word})


if __name__ == '__main__':
    assert (in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]) == ["arp", "live", "strong"])
    assert (in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]) == [])

    print("All tests passed")
