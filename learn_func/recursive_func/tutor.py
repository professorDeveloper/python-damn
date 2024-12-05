def factorial(n):
    if n>1:
        return  n*factorial(n-1)
    else:
        return 1

a=factorial(5)
print(a)
