studentSchedule = []

def BuildSchedule ():
    schedule = []
    validDaysOfWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    validShortHand = ["sun", "mon", "tues", "wed", "thurs", "fri", "sat"]

    completeCheck = ""
    classNum = int(1)

    while (str.toLower(completeCheck).contains("y")):
        # Solicit input from user to build their schedule
        print(f"What is your {classNum} class")
        classCode = input()
        print(f"What time does class {classNum} start at?")
        classStart = input()
        print(f"What time does class {classNum} end?")
        classEnd = input()
        print(f"What day does class {classNum} take place? Separate days with spaces")
        classDay = input()

        # Checks if input was vaid and if so add to the users schedule
        for day in validDaysOfWeek:
            if (str.toLower(classDay) in day):
                studentSchedule.append(classCode + "_" + classStart + "_" + classEnd + "_" + classDay)
                break         
        
        # Increment the class number by 1
        classNum = classNum + 1

        # Prompt user if they would like to add another class
        print("Would you like to add another class? (y/N)")
        completeCheck = input()

def ListSchedule ():
    for i in studentSchedule:
        classInfo = studentSchedule[i].split("_")
        print(f"Class: {classInfo[0]}")
        print(f"Time: {classInfo[1]} - {classInfo[2]}")
        print(f"Days of week: {classInfo[3]}")

if __name__ == "__main__":
    BuildSchedule()
    ListSchedule()