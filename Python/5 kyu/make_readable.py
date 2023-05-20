def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


if __name__ == "__main__":
    assert make_readable(0) == "00:00:00"
    assert make_readable(5) == "00:00:05"
    assert make_readable(60) == "00:01:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(359999) == "99:59:59"
    print("All tests passed")