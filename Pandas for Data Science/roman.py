def roman_numeral(n):
    roman_map = [
        (1000, "M"),
        (500, "D"),
        (100, "C"),
        (50, "L"),
        (10, "X"),
        (5, "V"),
        (1, "I"),
    ]

    ans = ""

    for value, symbol in roman_map:
        while n >= value:
            ans += symbol
            n -= value

    return ans


if __name__ == "__main__":
    for i in range(1, 25):
        print(roman_numeral(i))
        pass
    print(roman_numeral(50))
    print(roman_numeral(100))
    print(roman_numeral(500))
    print(roman_numeral(1000))
    print(roman_numeral(178))
    print(roman_numeral(2841))
    print(roman_numeral(8492))
    pass
