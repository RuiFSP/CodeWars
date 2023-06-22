def is_valid_IP(ip_address: str) -> bool:
    """Check if the given string is a valid IP address.

    Args:
        ip_address: A string representing an IP address.

    Returns:
        A boolean indicating whether the IP address is valid.

    """
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        if octet.startswith('0') and len(octet) > 1:
            return False
        if not (0 <= int(octet) <= 255):
            return False

    return True


if __name__ == "__main__":
    assert is_valid_IP('12.255.56.1') == True
    assert is_valid_IP('abc.def.ghi.jkl') == False
    assert is_valid_IP('123.456.789.0') == False
    assert is_valid_IP('12.34.56') == False
    assert is_valid_IP('12.34.56 .1') == False
    assert is_valid_IP('12.34.56.-1') == False
    assert is_valid_IP('123.045.067.089') == False
    print("All tests passed successfully")
