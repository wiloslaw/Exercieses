#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.


def compare(x, y):
    if x == y or x + y == 5 or x - y == 5 or y - x == 5:
        return True
    else:
        return False


print(compare(7,2))




