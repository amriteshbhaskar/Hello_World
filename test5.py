def prn(n):
    print(n,prn(n-1))
    return " "
prn(10)
