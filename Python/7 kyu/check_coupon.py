from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):

    if entered_code != correct_code:
        return False

    if type(entered_code) != str:
        return False

    # Convert the date strings to datetime objects
    current_date = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date = datetime.strptime(expiration_date, "%B %d, %Y")

    # Check if the current date is on or before the expiration date
    return current_date < expiration_date


if __name__ == "__main__":
    assert (check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014') == True)
    assert (check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014') == False)
    print("Everything passed")