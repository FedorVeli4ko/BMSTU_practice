def find_min(num):
    if not num:
        print ("Список не должен быть пустым")
    else:
        minn = num[0]
        for n in num:
            if n < minn:
                minn = n
        return minn
    
n = int(input("Введите количество чисел: "))
if n <= 0:
        print ("Количество чисел должно быть положительным")

nums = []
for i in range(n):
        number = float(input(f"Введите число {i + 1}: "))
        nums.append(number)

print("Минимум:", find_min(nums))
