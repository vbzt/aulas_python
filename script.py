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


def ex5():
    brancos = int(input('Insira o total de votos brancos: '))
    nulos = int(input('Insira o total de votos nulos: '))
    validos = int(input('Insira o total de votos validos: '))
    if 0 > brancos or 0 > nulos or 0 > validos:
        print('Valores invalidos.')
        ex5()

    total = brancos + nulos + validos
    print(f"Total: {total}\nNulos: {nulos/total*100}% \nBrancos: {brancos/total* 100}\nVálidos: {validos/total*100}%")


def ex6():
    raio = float(input('Insira o valor do raio: '))
    if raio < 0:
        print("Valor inválido.")

    area = raio**2 * 3.1415

    print(f'Aréa do circulo de raio {raio}: {area} ')

def ex7():
    custo = float(input('Insira o custo de fabricação: R$'))
    if custo < 0:
        print('Valor inválido.')
        ex7()

    finalPrice = (custo * 0.45) + (custo * 0.28) + custo
    print(f'Valor final: R${finalPrice}')

def ex8():
    salario = float(input('Insira o salario: R$'))
    if salario < 0:
        print('Valor inválido.')
        ex8()
    print(f'Novo salario: R${salario * 1.25}')

def ex9():
    value = 780000
    first = value * 0.46
    second = value * 0.32
    third = value * 0.22
    print(f'Primeiro: R${first}\nSegundo: R${second}\nTerceiro: R${third}')

def ex10():
    value = 80
    days = int(input('Insira a quantidade de dias trabalhados.'))
    if 0 > days:
        print('Valor invalido')
        ex10()

    print(f'Valor a ser pago: R${value * 0.92}')

def ex11():
    pao = 0.38
    broa = 4.5

    qnt_pao = int(input('Quantidade de pãos vendidos: '))
    qnt_broa = int(input('Quantidade de broas vendidas: '))

    if qnt_pao < 0 or qnt_broa < 0:
        print('Valores invalidos.')
        ex11()

    total = (pao * qnt_pao) + (broa * qnt_broa)
    print(f'Vendas totais: R${total}, Quantidade a guardar: R${total * 0.1}')

def ex12():
    comprimento = float(input('Digite o comprimento da cozinha: '))
    altura = float(input('Digite a altura da cozinha: '))
    largura = float(input('Digite a largura da cozinha: '))

    if comprimento < 0 or altura < 0 or largura < 0:
        print('Valor invalido.')
        ex12()

    parede_larg = altura * largura
    parede_comp = altura * comprimento

    area = parede_comp * 2 + parede_larg * 2
    caixas = (area // 1.5) + 1
    print(f'Quantidade de caixas: {caixas}.')


exs = int(input('Escolha um exercicio: '))

match exs:
    case 1:
        ex1()

    case 2:
        ex2()

    case 3:
        ex3()

    case 4:
        ex4()

    case 5:
        ex5()

    case 6:
        ex6()

    case 7:
        ex7()

    case 8:
        ex8()

    case 9:
        ex9()

    case 10:
        ex10()

    case 11:
        ex11()

    case 12:
        ex12()


