from random import randint


def ex1():
    even = []
    odd = []
    for i in range(10):
        n = int(input("Digite um numero: "))
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    print(f"Pares: {even} \n Impares: {odd}")


def ex2():
    nums = []
    sum = 0
    sumEven = 0
    for i in range(10):
        num = int(input("Digite um numero: "))
        nums.append(num)
        sum += num
        if num % 2 == 0:
            sumEven += num
    print(f"Media: {sum/10} \n Soma pares: {sumEven}")

def ex3():
    nums = []
    sum = 0

    for i in range(20):
        num = randint(1, 50)
        nums.append(num)

        sum += num

    print(f"Numeros: {nums} \nSomatorio: {sum}\nMenor: {min(nums)}  \nMaior: {max(nums)}");



def ex4():
    names = []
    ages = []
    for i in range(10):
        name = input("Digite seu nome: ")
        age = int(input("Digite sua idade: "))
        names.append(name)
        ages.append(age)

    for i in range(len(ages)):
        if ages[i] >= 18:
            print(f"{names[i]} tem mais de 18 anos")

def ex5():
    nums = []
    for i in range(10):
        nums.append(randint(0, 100))
    print(nums)
    num = int(input("Digite um numero: "))
    if num in nums:
        print("Esse numero aparece na lista")
    else:
        print("Esse numero nao aparece na lista")

def ex6():
    grades = []
    sum = 0
    while True:
        grade = int(input("Digite a nota: "))
        if grade < 0:
            break
        grades.append(grade)
        sum += grade

    avg = 0
    for grade in grades:
        if grade >= ( sum / (len(grades))):
            avg += 1

    print(f"Notas: {grades}\n"
          f"Quantidade de notas: {len(grades)}\n"
          f"Média:{sum / (len(grades))}\n"
          f"Quantidade acima da media: {avg}"
          )
    
lista = [3,10,7,8,1,9,8,5,8]
def listaMin():
  min = 0
  for i in range(len(lista)): 
    if i == 0: 
      min = lista[i]

    if lista[i] < min: 
      min = lista[i]
    
  return min
  
def listaMax():
  max = 0


  for i in range(len(lista)): 
    if i == 0: 
      max = lista[i]
    if lista[i] > max: 
      max = lista[i]
    
  return max
    

#print(listaMin())
#print(listaMax())

    
ex = int(input("Ex: "))

match ex:
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
