a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
def sum(a,b):
    first_num = a
    second_num = b
    def inner():
        result = 0
        for i in range(first_num, second_num + 1):
            result += i
        return result

    return inner

summa = sum(a,b)
print(summa())





