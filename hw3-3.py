def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Result - {my_func(int(input("Enter arg1: ")), int(input("Enter arg2: ")), int(input("Enter arg3: ")))}')
