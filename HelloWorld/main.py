import random as ran

def helloWorld():
    hello = 8
    print ("hello world")
    
def forLoop():
    values = ["hello", "bye", "hi"]
    for i in range(ran.randrange(15)):
        print(i)

if __name__=="__main__":
    print ("Hello world")
    helloWorld()
    forLoop()
    