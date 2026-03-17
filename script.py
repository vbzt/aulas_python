def ex1():
    val = float(input('Insira o valor do produto'))
    if 0 > val:
        print("Valor inválido.")
        ex1()
    discount = val * 0.88
    return print(f'Valor do produto R${val}. Valor final com desconto: R${discount}')

def ex2():
    val = int(input("Insira o tempo em segundos: "))
    if 0 > val:
        print("Valor inválido.")
        ex2()

    hours = val // 3600
    mins = (val - (hours * 3600)) // 60
    sec = val % 60

    print(f'{hours}h {mins}m  {sec}s')

def ex3():
    val = int(input('Insira a quantidade de frangos: '))
    if 0 > val:
        ex3()

    return val * 1.1

def ex4():
    real = float(input("Insira o valor em real: R$"))
    dolar = float(input("Insira o valor da cotação do dolar: US$"))
    if 0 > real or 0 > dolar:
        print("Valor inválido.")
        ex4()
    val = real / dolar
    return print(f"US$ {val:.2f}")






exs = int(input('Escolha um exercicio: '))

match exs:
    case 1:
        ex1()

    case 2:
        ex2()
