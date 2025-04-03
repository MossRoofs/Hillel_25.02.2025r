def calculator():
    try:
        num1 = float(input("Введіть перше число: "))
        operation = input("Виберіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Помилка! Ділення на нуль заборонено."
            else:
                result = num1 / num2
        else:
            return "Невірна операція!"


        return f"Результат: {result}"

    except ValueError:
        return "Помилка! Будь ласка, введіть правильні числа."

print(calculator())
