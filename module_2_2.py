first = input("Веедите первое число ")
second = input("Введите второе число ")
third = input("Введите третье число ")
if first == second and first == third:
    print('3')
elif first == second or first == third:
    print('2')
elif second == first or second == third:
    print('2')
elif third == second or third == first:
    print('2')
else:
    print('0')