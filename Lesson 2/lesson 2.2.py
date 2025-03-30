number = int(input("Enter a 5-digit number: "))

e = number % 10
d = (number % 100) // 10
c = (number % 1000) // 100
b = (number % 10000) //1000
a = number // 10000

print(e, d, c, b, a)
