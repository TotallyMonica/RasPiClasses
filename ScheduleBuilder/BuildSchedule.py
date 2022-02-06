import RPi.GPIO as GPIO
import time

#Globally used variables
gpioPins = [int(4), int(5), int(6), int(12), int(13), int(16), int(17), int(18), int(19), int(20), int(21), int(22), int(23), int(24), int(25), int(26), int(27)]
studentSchedule = []
useLEDs = int(0)

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
    
    sourceFile = open('schedule.txt', 'w')
    for i in studentSchedule:
        sourceFile.write(i + ",")
    sourceFile.close

def ListSchedule ():
    with open('schedule.txt') as f:
        studentSchedule = f.split(",")

    for i in studentSchedule:
        classInfo = studentSchedule[i].split("_")
        print(f"Class: {classInfo[0]}")
        print(f"Time: {classInfo[1]} - {classInfo[2]}")
        print(f"Days of week: {classInfo[3]}")

def gpioUsage ():
    # Note: not using a boolean due to multiple potential outcomes
    # Outcome 1: Potential typo, reiterating it. This would be int(0).
    # Outcome 2: User has LEDs connected. This would be int(1).
    # Outcome 3: Uesr does not have LEDs connected and/or does not want to use LEDs. This would be int(2).

    while useLEDs == 0:
        print("Are LEDs connected to the Pi? (y/n)")
        ledsConnected = input()

        if ledsConnected.toUpper().contains("Y"):
            useLEDs = 1
            findGpioPins()
        
        elif ledsConnected.toUpper().contains("N"):
            print("Would you like to use LED(s)? (y/n)")
            queryLEDs = input()
            
            if queryLEDs.toUpper().contains("Y"):
                print("At this point, please connect some LED(s) to your Raspberry Pi.")
                print("In a later step, we will try to find what pin your LED(s) are connected to")
                print("If you have access to them, we recommend you use two LEDs: one red and one green.")
                print("Press enter when you're ready to continue.")
                input()

                useLEDs = 1
                findGpioPins()
            
            elif queryLEDs.toUpper().contains("N"):
                useLEDs = 2
                break
            
            else:
                print("Invalid input detected. ")


def findGpioPins ():
    # Variables used within the function needed for loops
    ledsSet = False
    currentLED = int(0)

    # Loop while not all of the desired LEDs have been set
    while not ledsSet:

        scanPin = True
        
        # LED Scan test
        while scanPin:

            # Iterate all of the GPIO pins in list gpioPins
            for i in gpioPins:

                #Set pin to high, then have user confirm whether the desired LED is on
                GPIO.output(i, GPIO.HIGH)
                print("Is the first LED turned on?")
                print("If you're following our recommendation, this should be your red one.")
                pin1Set = input("(y/N): ")
                
                # Yes, set stop the scan test
                if pin1Set.toUpper().contains("Y"):
                    scanPin = False

                else:
                    # On the off chance of bad wiring, missing the light, or whatever might go wrong that it iterated over all the LEDs, allow the ability to try again
                    if i == 27:
                        print("All of the allowed GPIO headers have been tried. Would you like to loop agin? (y/N)")
                        tryAgain = input()

                        if tryAgain.toUpper.contains("Y"):
                            continue
                        else:
                            scanPin = False
                    
                    # Well not every pin is going to be pin 27
                    else:
                        continue
        
        # Prompt if they would like to add another LED
        print("Would you like to add another LED? (y/n)")
        addAnother = input() 
        
        # If true, increment the LED list by 1, the continue
        if addAnother.toUpper().contains("Y"):
            continue

        # If the user inputs N/No, set boolean ledsSet to true, stopping the loop altogether and going back to the main screen.
        elif addAnother.toUpper().contains("N"):
            ledsSet = True
        
        # I like to have this as a failsafe
        else:
            print("Invalid input detected. Assuming yes.")


if __name__ == "__main__":
    gpioUsage()

    run = True
    while(run):
        print("Would you like to build your schedule, list your current schedule, or quit?")
        userInput = input()
        if (userInput.toLower().contains("build")):
            BuildSchedule()
        elif (userInput.toLower().contains("list")):
            ListSchedule()
        elif (userInput.toLower().contains("quit")):
            run = False
        else:
            print("Invalid input.")