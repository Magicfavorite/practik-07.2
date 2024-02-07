num = int(input("Введите значение числа"))
stepen = int(input("Введите значение степени"))

def power(num, stepen):
    if (stepen == 1):
        return (num)
    if (stepen != 1):
        return (num * power(num, stepen - 1))

print("Результат возведения в степень равен:", power(num, stepen))