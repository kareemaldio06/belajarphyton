for mem1 in range(10):
    if mem1 >= 5:
        for mem2 in range(mem1):
            print('*'* 5, end='')
    else:
        for mem2 in range(mem1):
            print()
