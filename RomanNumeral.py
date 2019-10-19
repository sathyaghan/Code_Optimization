from datetime import datetime as time

roman_list = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC",
              100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

"""
A brute force method
"""


def convert_roman(num, roman=""):
    """
    This function takes an integer input below 4000 and returns its Roman Numeral equivalent
    :param num: 1904
    :param roman: null
    :return: MCMIV
    """
    if num - 1000 >= 0:
        count = num - 1000
        if count == 0:
            roman += roman_list.get(1000)
        else:
            for i in range(num // 1000):
                roman += roman_list.get(1000)
        return convert_roman(num % 1000, roman)
    elif num - 1000 < 0:
        if num in range(900, 1000):
            roman += "CM"
            return convert_roman(num % 100, roman)
        elif num > 500:
            count = num - 500
            roman += roman_list.get(500)
            for i in range(count // 100):
                roman += roman_list.get(100)
            return convert_roman(num % 100, roman)
        elif num == 500:
            roman += roman_list.get(500)
        elif num in range(400, 500):
            roman += "CD"
            return convert_roman(num % 100, roman)
        elif num > 100:
            for i in range(num // 100):
                roman += roman_list.get(100)
            return convert_roman(num % 10, roman)
        elif num == 100:
            roman += roman_list.get(100)
            return convert_roman(num % 10, roman)
        elif num > 50:
            count = num - 50
            roman += roman_list.get(50)
            for i in range(count // 10):
                roman += roman_list.get(10)
            return convert_roman(num % 10, roman)
        elif num == 50:
            roman += roman_list.get(50)
        elif num in range(40, 50):
            roman += "XV"
            return convert_roman(num % 10, roman)
        elif num > 10:
            for i in range(num // 10):
                roman += roman_list.get(10)
            return convert_roman(num % 10, roman)
        elif num == 10:
            roman += roman_list.get(10)
            return convert_roman(num % 10, roman)
        elif num > 5:
            count = num - 5
            roman += roman_list.get(5)
            for i in range(count // 10):
                roman += roman_list.get(1)
        elif num == 5:
            roman += roman_list.get(5)
        elif num == 4:
            roman += "IV"
        elif num > 1:
            for i in range(num):
                roman += roman_list.get(1)
        elif num == 1:
            roman += roman_list.get(1)
        else:
            pass
    return roman


"""
A different approach
"""


def num_splitter(num):
    """
    This function takes a number and splits it into component digits and then returns a dictionary of the digit and its
    position with the position as the key
    :param num: 3210
    :return: {1000:3, 100:2, 10:1, 1:0}
    """
    num1 = [int(d) for d in str(num)]
    num_dict = {}
    length = len(num1)
    for i in num1:
        num_dict.update({10 ** (length - 1): i})
        length -= 1
    return num_dict


def roman_converter(num):
    """
    This function converts the number to its roman numeral equivalent
    :param num: 1904
    :return: MCMIV
    """
    if num < 4000:
        roman = ""
        num_dict = num_splitter(num)
        numbers = [key * num_dict[key] for key in num_dict]
        for number in numbers:
            if number > 1000:
                roman += roman_list.get(1000)
                for i in range((number - 1000) // 1000):
                    roman += roman_list.get(1000)
            elif number in roman_list:
                roman += roman_list[number]
            else:
                place = 0
                for keys in roman_list:
                    if keys > number:
                        place = keys
                        break
                if place < 10:
                    if number > 5:
                        roman += roman_list.get(5)
                        for i in range(number - 5):
                            roman += roman_list.get(1)
                    else:
                        for i in range(number):
                            roman += roman_list.get(1)
                elif place < 100:
                    if number > 50:
                        roman += roman_list.get(50)
                        for i in range((number - 50) // 10):
                            roman += roman_list.get(10)
                    else:
                        for i in range(number // 10):
                            roman += roman_list.get(10)
                elif place < 1000:
                    if number > 500:
                        roman += roman_list.get(500)
                        for i in range((number - 500) // 100):
                            roman += roman_list.get(100)
                    else:
                        for i in range(number // 100):
                            roman += roman_list.get(100)
        return roman
    else:
        return "We currently do not allow numbers larger than or equal to 4000"

"""
A new and smaller method with divmod
"""

NUMERAL_TO_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                   (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def _convert_to_roman_numeral(number: int) -> str:
    """Convert number to a roman numeral string"""
    result = list()
    for numeral, roman in NUMERAL_TO_ROMAN:
        count, number = divmod(number, numeral)
        result.append(roman * count)
    return "".join(result)


# Calculates the time taken to run both the methods in microseconds
t1 = time.now().microsecond
print(convert_roman(1000))
t2 = time.now().microsecond
print(roman_converter(1000))
t3 = time.now().microsecond
print(_convert_to_roman_numeral(1000))
t4 = time.now().microsecond
# Print the times
print(t2 - t1)
print(t3 - t2)
print(t4 - t3)
# Print the improvement of the second approach over the first
print(round((abs((t3 - t2) - (t2 - t1)) / (t2 - t1)) * 100, 2))  # Comparison of 2nd and 1st method
print(round((abs((t4 - t3) - (t3 - t2)) / (t3 - t2)) * 100, 2))  # Comparison of 3rd and 2nd method
print(round((abs((t4 - t3) - (t2 - t1)) / (t2 - t1)) * 100, 2))  # Comparison of 3rd and 1st method
