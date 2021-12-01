halls = ["geisert", "williams", "wyckoff", "harper", "university"]
    
if __name__ == "__main__":
    for i in halls:
        print("I've looked at", i, "hall but utlimately decided against it")
    
    while(True):
        print("Enter a number between 0 and 10. I'll raise 2 to that number.")
        i = input("-> ")
        if (int(i) < 0 or int(i) > 10):
            break
        print(pow(2, int(i)))
        print()