def ex1():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3)/3
    print("Aprovado" if media >= 6 else "Reprovado.")

def ex2():
    valor = int(input('Digite um numero: '))
    print("Par" if valor % 2 == 0 else "Ímpar")

def ex3():
    valor = float(input("Digite um numero: "))
    print(valor if valor > 0 else valor * -1)

def ex4():
    vogais = ['a','e','i','o','u']
    letra = input("Digite uma letra: ")
    print("Vogal" if letra in vogais else 'Consoante')

def ex5():
    val = int(input('Digite um numero: '))
    if val == 0:
       print("Zero")

    print("Inteiro" if val > 0 else "Negativo.")

def ex6():
    h = int(input("Insira as horas"))
    m = int(input("Insira os minutos"))
    if h >= 24 or h < 0 or m >= 60 or m < 0:
        print("Horas invalidas.")

    print("Horas validas")