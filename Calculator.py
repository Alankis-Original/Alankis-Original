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
    print("{} ++ {} =".format(num1, num2), num1 ++ num2)
elif op == "**":
    print("{} ** {} =".format(num1, num2), num1 ** num2)
elif op == "//":
    print("{} // {} =".format(num1, num2), num1 // num2)
elif op == "<<":
    print("{} << {} =".format(num1, num2), num1 << num2)
elif op == ">>":
    print("{} >> {} =".format(num1, num2), num1 >> num2)
else:
    print("Error operator not found:", op)