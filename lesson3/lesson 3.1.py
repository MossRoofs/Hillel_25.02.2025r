num1 = int(input("Введіть перше число: "))
operation = input("Введіть оператор (+, -, *, /): ")
num2 = int(input("Введіть друге число: "))
if num2 != 0:
    result = num1 / num2
if operation == "+" :
    print(num1+num2)
elif operation == "-" :
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/" :
    print(num1/num2)
else:
    print("Введіть один з наведених операторів (+, -, *, /)")