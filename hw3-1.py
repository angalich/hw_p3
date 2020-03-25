def my_func():
    try:
        arg1 = int(input("Enter number: "))
        arg2 = int(input("Enter number: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong number! You can't use 0 as a number"

    return res


print(my_func())
