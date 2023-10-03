list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
chut=0
nechut=1
for i in range(len(list)):
    if i % 2==0:
        chut+=list[i]
    else:
        nechut*=list[i]
print('Сумма элементов с четными номерами:', chut)
print('Произведение элементов с нечетными номерами:', nechut)