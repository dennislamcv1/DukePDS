from operator import itemgetter

weird_characters = "-?.!,[]—:;\"'"


def countWords(counts, line):
    words = line.split()  # Step 1: Split line into words
    for word in words:
        clean_word = word.strip(weird_characters).lower()  # Step 2: Clean up word
        if clean_word:  # Ignore empty words
            counts[clean_word] = counts.get(clean_word, 0) + 1  # Update count
    return counts


def printResults(counts):
    as_list = sorted(counts.items(), key=itemgetter(0))  # Step 4: Sort alphabetically
    for word, count in as_list:
        print(f"{word} : {count}")  # Step 3: Print results properly


# You do not need to modify this function.
# It will call your countWords and printResults functions
def countFile(fname):
    counts = {}
    with open(fname) as f:
        for line in f:
            countWords(counts, line)
            pass
        pass
    printResults(counts)
    pass


if __name__ == "__main__":
    countFile("caesar.txt")
