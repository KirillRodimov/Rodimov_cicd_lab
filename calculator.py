## @file calculator.py
# @brief Арифметические операции учебного калькулятора.


## @brief Складывает два числа.
# @param a Первое слагаемое.
# @param b Второе слагаемое.
# @return Сумма чисел.
def add(a, b):
    return a + b


## @brief Вычитает второе число из первого.
# @param a Уменьшаемое.
# @param b Вычитаемое.
# @return Разность чисел.
def subtract(a, b):
    return a - b


## @brief Умножает два числа.
# @param a Первый множитель.
# @param b Второй множитель.
# @return Произведение чисел.
def multiply(a, b):
    return a * b


## @brief Делит первое число на второе.
# @param a Делимое.
# @param b Делитель, не равный нулю.
# @return Частное чисел.
# @exception ZeroDivisionError Если делитель равен нулю.
def divide(a, b):
    return a / b