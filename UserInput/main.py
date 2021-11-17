if __name__== "__main__":
    name = input("Enter your name: ")
    print("Nice to meet you", name)

    print("Where are you from?")
    city = input()

    #Convert numbers to ints
    age = int(input("How old are you? "))

    #By default, an int will look like a string, so we're doing
    #this to show that the age can be manipulated
    futureAge = age + 10

    print("In 10 years,", name, "will be", futureAge, "years old, but will still be from", city, ".")