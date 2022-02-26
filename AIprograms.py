# ai
import pyttsx3
engine = pyttsx3.init()
while True:
    engine.setProperty('rate', 125)
    engine.say("Whats is your name?")
    engine.runAndWait()
    name = input("What is your name? ")
    engine.say("Hi {} i am an AI".format(name))
    print("Hi {} i am an AI".format(name))
    engine.runAndWait()
    engine.say("How can I help you? {}".format(name))
    engine.runAndWait()
    help = input("How can I help you? ")
    if help == "stupid":
        print("Very Sadness!")
        engine.say("Very Sadness!")
        engine.runAndWait()
    elif help == "":
        print("Bro type something")
        engine.say("Bro type something!")
        engine.runAndWait()
    elif help == "calculator":
        engine.say("welcome to calculator")
        engine.runAndWait()
        print("operator: +, -, *, /, <, =, >, ++, --, **, //")
        op = input("operator: ")
        num1 = int(float(input("Enter a number: ")))
        num2 = int(float(input("Enter another number: ")))
        if op == "+":
            print("{} + {} =".format(num1, num2), num1 + num2)
        elif op == "-":
            print("{} - {} =".format(num1, num2), num1 - num2)
        elif op == "*":
            print("{} * {} =".format(num1, num2), num1 * num2)
        elif op == "/":
            print("{} / {} =".format(num1, num2), num1 / num2)
        elif op == "<":
            print("{} < {}:".format(num1, num2), num1 < num2)
        elif op == "=":
            print("{} = {}:".format(num1, num2), num1 == num2)
        elif op == ">":
            print("{} > {}:".format(num1, num2), num1 > num2)
        elif op == "++":
            print("{} ++ {} =".format(num1, num2), num1 + + num2)
        elif op == "**":
            print("{} ** {} =".format(num1, num2), num1 ** num2)
        elif op == "//":
            print("{} // {} =".format(num1, num2), num1 // num2)
        elif op == "<<":
            print("{} << {} =".format(num1, num2), num1 << num2)
        elif op == ">>":
            print("{} >> {} =".format(num1, num2), num1 >> num2)
        else:
            engine.say("Error operator not found:", op)
            engine.runAndWait()
            print("Error operator not found:", op)
    else:
        print("oops Error!")
