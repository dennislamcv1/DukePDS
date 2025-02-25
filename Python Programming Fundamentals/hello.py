# A function to compute the greeting for someone
# given their name.  If given "Drew" as the name,
# this function should return "Hello Drew!"
# In general, it should return "Hello " followed
# by the name and then an exclaimation mark
def hello(name):
    return "Hello" + " " + name + "!"


# A function to print a greeting for someone
# given their name
def print_greeting(name):
    print(hello(name))
    pass


# Define a function says what we want
# our program to do when we run it
def main():
    print_greeting("Drew")
    print_greeting("Genevieve")
    print_greeting("Nick")
    print_greeting("Kyle")
    pass


# Later, you will learn that this should be
# under if __name__ == "__main__":
main()
