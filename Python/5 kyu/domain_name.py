def domain_name(url):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    return url.split(".")[0]


if __name__ == "__main__":
    assert domain_name("http://github.com/carbonfive/raygun") == "github"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("https://www.cnet.com") == "cnet"
    assert domain_name("http://www.google.com") == "google"
    print("Everything passed")
