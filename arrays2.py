import random


def ex1():
    nums = []
    while len(nums) < 10:
        num = random.randint(1,20)
        if num not in nums:
            nums.append(num)
    print(nums)

def ex2():
    nums = []
    primes = []
    for i in range(30):
        nums.append(random.randint(1, 50))

    for i in range(len(nums)):
        if nums[i] < 2:
            continue

        isPrime = True
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(nums[i])

    print(primes)
    print(nums)

def ex3():
    nums = []
    for i in range(30):
        nums.append(random.randint(1, 50))

    num = int(input("Insira um numero inteiro para multiplicar os itens da lista: "))
    print(f"Antes: {nums}")
    for i in range(len(nums)):
        nums[i] = nums[i] * num
    print(f'Depois: {nums}')


def ex4():
    arr = []
    while len(arr) < 10:
        item = input("Insira algo: ")
        arr.append(item)

    isPalindrome = True
    for left in range(int(len(arr) / 2)):
        right = len(arr) - left - 1
        if arr[left] != arr[right]:
            isPalindrome = False
            break



    if isPalindrome:
        print(f'A lista {arr} é um palindromo')
    else:
        print(f"A lista {arr} não é um palindromo")

def ex5():
    arr1, arr2, arr3 = [],[],[]
    for i in range(10):
        arr1.append(random.randint(1,20))
        arr2.append(random.randint(1,20))

        arr3.append(arr1[i])
        arr3.append(arr2[i])

    print(f"{arr1}\n{arr2}\n{arr3}")

ex3()
