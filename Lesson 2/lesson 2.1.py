number = int(input("Enter a 4-digit number: "))

a = number // 1000
b = (number % 1000) //100
c = (number % 100) // 10
d = number % 10

print(a)
print(b)
print(c)
print(d)
