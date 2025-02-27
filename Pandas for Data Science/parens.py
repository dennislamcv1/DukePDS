def get_parenthesized_regions(s):
    regions = []
    start = -1  # Track the index of the last unmatched '('

    for i in range(len(s)):
        if s[i] == "(":
            start = i  # Store the index of the open parenthesis
        elif s[i] == ")" and start != -1:
            regions.append(s[start + 1 : i])  # Extract the substring inside ()
            start = -1  # Reset start after extracting

    return regions


if __name__ == "__main__":

    def test(s):
        print(
            "get_parenthesized_regions('{}') is {}".format(
                s, get_parenthesized_regions(s)
            )
        )
        pass

    test("")
    test("abc")
    test("a(bcde)fgh")
    test("abc(def)ghi(jkl)")
    test("hello)world(apple)")
    test("apple(bear)(cat)(dog")
    test("(hello)world)apple(bear)cat(dog)fr(og")
    test("a(b)c(d)e(f)(g)hi(jkl)(m)(ab)(c)xyz(ef)")
    pass
