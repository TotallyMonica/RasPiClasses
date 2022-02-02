def getSchedule():
    print("What department is the class in?")
    department = input()
    print("What course number is the class?")
    course = input()
    print("What section is this class?")
    section = input()
    return department, course, section

def main():
    print("How many classes do you have?")
    courseCount = int(input())
    schedule = []

    for i in courseCount:
        print("For course", i)
        schedule.append(getSchedule())
        
