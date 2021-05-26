cont = int(0)
casos = int(input())
while (cont < casos):
    a, b, c, d, e, f, g = input().split(" ")
    numero_1 = int(a)
    barra = str(b)
    divisor_1 = int(c)
    sinal = str(d)
    numero_2 = int(e)
    barra = str(f)
    divisor_2 = int(g)
    var = int(0)
    if (sinal[0] == '+'):
        numero_3 = int(numero_1 * divisor_2) + (numero_2 * divisor_1)
        divisor_3 = int(divisor_1 * divisor_2)
    else:
        if (sinal[0] == '-'):
            numero_3 = int(numero_1 * divisor_2) - (numero_2 * divisor_1)
            divisor_3 = int(divisor_1 * divisor_2)
            teste_sinal1 = float(numero_1 / divisor_1)
            teste_sinal2 = float(numero_2 / divisor_2)
            if (teste_sinal2 > teste_sinal1):
                var = 1
        else:
            if (sinal[0] == '*'):
                numero_3 = int(numero_1 * numero_2)
                divisor_3 = int(divisor_1 * divisor_2)
            else:
                numero_3 = int(numero_1 * divisor_2)
                divisor_3 = int(numero_2 * divisor_1)
    numero_4 = int(numero_3)
    divisor_4 = int(divisor_3)
    if (numero_4 > divisor_4):
        menor = divisor_4
    else:
        menor = divisor_4
    while (menor >= 2):
        if (numero_4 % menor == 0 and divisor_4 % menor == 0):
            numero_4 = int(numero_4 / menor)
            divisor_4 = int(divisor_4 / menor)
            menor = 1
        else:
            menor = menor - 1

    print("{}/{} = {}/{}".format(numero_3, divisor_3, numero_4, divisor_4))
    cont = cont + 1