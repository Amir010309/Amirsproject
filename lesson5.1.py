number = int (input())

if number > 0 and number % 2 == 0:
    print ("Положительное четное число")
else:
    if number > 0 and not number % 2 == 0:
        print ("Положительное нечетное число")
    else:
        if number < 0 and number % 2 == 0:
            print("Отрицательное четное число")
        else:
            if number < 0 and not number % 2 == 0:
                print ("Отрицательное нечетное число")