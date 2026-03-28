def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Добро пожаловать в базовый калькулятор!")
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")

while True:
    choice = input("Введите номер операции (1/2) или 'q' для выхода: ")

    if choice.lower() == 'q':
        print("Выход из программы.")
        break

    if choice in ('1', '2'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}\n")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}\n")
    else:
        print("Неверный ввод. Пожалуйста, попробуйте снова.\n")