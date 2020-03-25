def my_func():
    sum = 0
    # exit
    exi = False
    #выполнять exi не False
    while exi == False:
        number = input('Enter numbers separated by space or 00 to exit - ').split()

        res = 0
        for el in range(len(number)):
            """
            если ввести 00, то exit True и завершить програграмму
            """
            if number[el] == '00' or number[el] == '00':
                exi = True
                break
            else:
                res = res + int(number[el])
        sum = sum + res
        #sum before enter 00
        print(f'Current sum is {sum}')
    #sum after enter 00
    print(f'Final sum after exut is {sum}')


my_func()
