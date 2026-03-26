import random


opt = int(input("Bem vindo a lanchonete! Escolha suas opções \n1.Lanche\n2.Bebida\n3.Sobremesa\n4.Sair\n"))
val = 0
match opt: 
    case 1: 
        opt_lanche = int(input('Escolha seu lanche:\n1.Cachorro-quente R$15.00\n2.Hamburguer R$20.0\n'))
        qnt_lanche = int(input("Digite a quantidade desse lanche: "))
        match opt_lanche: 
            case 1: 
                val += 15 * qnt_lanche
            case 2: val += 20 * qnt_lanche
    case 2: 
        opt_bebida = int(input("Escolha sua bebida\n1.Refrigerante R$6.00\n2.Suco natural R$10.00\n"))
        qnt_bebida = int(input('Digite a quantidade de bebidas: '))
        match opt_bebida:
            case 1: 
                val += 6 * qnt_bebida
            case 2: 
                val += 10 * qnt_bebida
    
    case 3: 
        opt_sobremesas = int(input("Escolha sua sobremesa\n1.Açaí R$25.00\n2.Sorvete R$18.00\n"))
        qnt_sobremesas = int(input("Digite a quantidade de sobremesas: "))
        match opt_sobremesas:
            case 1:
                val+=25*qnt_sobremesas
            case 2: 
                val+=18*qnt_sobremesas

    case 4: 
        print("obrigado, volte sempre!")
    
    case _: 
        print("Essa opção não existe.")


if(val > 0):
    print(f"Valor final do pedido R${val}\nNúmero do pedido: {random.randint(0, 100)}")
