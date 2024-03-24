a = int (input())

if a < 0 and a % 2 == 0:
    print ("Отрицательное четное  число")
else:
    if a < 0 and not a % 2 == 0:
        print ("Отрицательное нечетное число")
    else:
        if a > 0 and a % 2 == 0:
            print ("Положительное четное число")
        else:
            print ("Положительное нечетное число")