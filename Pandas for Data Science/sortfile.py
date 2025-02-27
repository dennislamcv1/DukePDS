def sortFile(filename):
    """Reads the lines from the given file, sorts them, and returns the sorted list."""
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines into a list

    return sorted(lines)  # Return the sorted list of lines


# You should not change any of this code
def main():
    ans = sortFile("input.txt")
    print("The values from sorting input.txt are:")
    n = 1
    for i in ans:
        print("{}: {}".format(n, i), end="")
        n = n + 1
        pass
    pass


if __name__ == "__main__":
    main()
    pass
