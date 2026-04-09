def ex3():
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))

    if x >= y:
        z = y
        x = y 
        x = z

    x += 1  

    if x % 2 == 0:
        x += 1

    while x < y:
        print(x)
        x += 2  



def ex7(): 
    num = int(input("Digite um numero: "))
    sum = 0
    while num > 0:
      digit = num % 10
      sum+=digit
      num = num // 10
    print(sum)

  
ex7()