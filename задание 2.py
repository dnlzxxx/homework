x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
if y==0:
    print("Делить на ноль нельзя!")
else:
    if x % y == 0:
        print(f"Число {x} делится на {y} без остатка")
    else:
        print (f"Число {x} не делится на {y} без остатка")
