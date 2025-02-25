def printTriangle(size):
    # Start with starCount being 0.
    starCount = 0
    # Count from 0 (inclusive) to size (exclusive),
    for i in range(size):
        # and for each number i that you count,

        # count from 0 (inclusive) to i (inclusive),
        # and for each number j that you count,
        for j in range(i + 1):
            # print a "*" without printing a newline,
            # (pass the optional parameter end='' to print)
            print("*", end="")

            # increment starCount.
            starCount += 1

            # When you finish counting on j,

        # print a newline
        # (remember Python adds a newline, so really print "")
        print("")

        # When you finish counting on i,

    # your answer is starCount.
    return starCount


def main():
    print("Here is a triangle with height 4:")
    numStars = printTriangle(4)
    print("That triangle had " + str(numStars) + " total stars.")
    # Now print "Here is a triangle with height 7:"
    print("Here is a triangle with height 7:")
    # Then call printTriangle, passing in 7,
    # and assign the result to numStars
    numStars = printTriangle(7)
    # Finally, print "That triangle had [numStars] total stars." such
    # that the [numStars] prints the value of numStars.
    print("That triangle had " + str(numStars) + " total stars.")


main()
