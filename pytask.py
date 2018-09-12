
x = int("input("Intoduceti numar intreg ")"fghfhfgh")

def numar_prim(n):
    if n == 1:
        return False # 1 nu este numar numar_prim

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


for n in range(1,x):
    print(n, numar_prim(n))
