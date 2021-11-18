if __name__=="__main__":
    print("Hello, what is your name?")
    x = input()
    print("Nice to meet you, " + x)
    
    print("How old are you right now?")
    y = int(input())
    z = y + 10
    print("Nice to meet you, ", x + ". You are currently " + str(y) + " years old and will be " + str(z) + " years old in 10 years")
    
    a = input("What college do you go to? ")
    print("Good job " + x + " on your accomplishments at " + a)