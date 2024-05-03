import random

def aruncare_zaruri():
    return [random.randint(1, 6) for _ in range(6)]

def calculeaza_punctaj(zaruri, formatie):
    if formatie in ["1", "2", "3", "4", "5", "6"]:
        return sum(d for d in zaruri if d == int(formatie))
    elif formatie == "mici":
        return sum(d for d in zaruri if d <= 3)
    elif formatie == "mari":
        return sum(d for d in zaruri if d >= 4)
    elif formatie == "pare":
        return sum(d for d in zaruri if d % 2 == 0)
    elif formatie == "impare":
        return sum(d for d in zaruri if d % 2 != 0)
    elif formatie == "duble":
        for i in range(1, 7):
            if zaruri.count(i) >= 2:
                return 3 * i
        return 0
    elif formatie == "triple":
        for i in range(1, 7):
            if zaruri.count(i) >= 3:
                return 2 * 3 * i
        return 0
    elif formatie == "suita":
        if sorted(zaruri) == [1, 2, 3, 4, 5, 6]:
            return 20
        return 0
    elif formatie == "care":
        if zaruri.count(6) >= 4:
            return sum(zaruri)
        return 0
    elif formatie == "cameron":
        if zaruri == [4, 6, 4, 6, 4, 6]:
            return 36
        return 0
