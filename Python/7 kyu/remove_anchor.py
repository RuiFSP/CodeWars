def remove_url_anchor(url):
    return url.split('#')[0]


if __name__ == "__main__":
    assert remove_url_anchor("www.codewars.com#about") == "www.codewars.com"
    assert remove_url_anchor("www.codewars.com/katas/?page=1#about") == "www.codewars.com/katas/?page=1"
    assert remove_url_anchor("www.codewars.com/katas/") == "www.codewars.com/katas/"
    assert remove_url_anchor("www.codewars.com/katas/?page=1") == "www.codewars.com/katas/?page=1"
    assert remove_url_anchor("www.codewars.com/katas/?page=1#") == "www.codewars.com/katas/?page=1"
    print("All tests passed!")
