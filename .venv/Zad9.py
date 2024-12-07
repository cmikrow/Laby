def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(8))
#   fi 0,1,1,2,3,5,8,13,21,34,55
#    n 0,1,2,3,4,5,6,07,08,09,10