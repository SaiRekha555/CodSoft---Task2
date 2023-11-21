
# # CODSOFT-Python-Programming

# # Task 2 - Simple calculator

# # programmer : SaiRekha Kollapudi

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


print("Please select operation -\n"         "1. Add\n"         "2. Subtract\n"         "3. Multiply\n"         "4. Divide\n"         "5. Exit\n")


calculate = True
while calculate:
    select = int(input("Select operations form 1, 2, 3, 4 , 5:"))
    if select == 1:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "+", number_2, "=",add(number_1, number_2))

    elif select == 2:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "-", number_2, "=",sub(number_1, number_2))

    elif select == 3:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "*", number_2, "=",mul(number_1, number_2))

    elif select == 4:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "/", number_2, "=",div(number_1, number_2))
    elif select == 5:
        user = input("\nAre you sure to exit?(Y/N):").lower()
        if user == "y":
            calculate = False
            print("Exit.")
    else:
         print("Invalid Entry")
            



