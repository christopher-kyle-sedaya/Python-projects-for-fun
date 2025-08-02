from calculator import Calculator

calc = Calculator()
running = True

print(calc.introduction_msg)

while running:
    user_input = input("Choose your operation (or type 'exit' to close) +, -, / ,*\n").lower()
    if user_input == "exit":
        running = False
    elif user_input != "exit":
        user_num1 = float(input("What is your first number?"))
        user_num2 = float(input("What is your second number?"))
        if user_input == "+":
            print(calc.add(user_num1 ,user_num2))
        elif user_input == "-":
            print(calc.subtract(user_num1, user_num2))
        elif user_input == "/":
            print(calc.divide(user_num1, user_num2))
        elif user_input == "*":
            print(calc.multiply(user_num1, user_num2))

        use_again = input("Do you want to use again? y/n \n")
        if use_again == "n":
            running = False
