def obr(one, mod):
    print(one )
    print(mod)
    if one == 0:
        return (mod, 0, 1)
    else:
        nod, x, y = obr(mod % one, one)
        print(nod)
        print(x)
        print(y)

    return (nod, y - (mod // one) * x, x)

a = obr(12,17)
print(a)

