# Introdução

print("╭━━╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
print("╰┫┣╯╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
print("╱┃┃╱╭━━╮╰╮╭╯╭━╮╭━━╮╭━╯┃╭╮╭╮╭━━╮╭━━╮╭━━╮")
print("╱┃┃╱┃╭╮┃╱┃┃╱┃╭╯┃╭╮┃┃╭╮┃┃┃┃┃┃╭━╯┃╭╮┃┃╭╮┃")
print("╭┫┣╮┃┃┃┃╱┃╰╮┃┃╱┃╰╯┃┃╰╯┃┃╰╯┃┃╰━╮┃╭╮┃┃╰╯┃")
print("╰━━╯╰╯╰╯╱╰━╯╰╯╱╰━━╯╰━━╯╰━━╯╰━━╯╰╯╰╯╰━━╯")
print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")


input("Ola este é um projeto teste que foi criado por diversão, pressione qualquer tecla para continuar")
input("Para ter acesso ao menu interativo iremos passar por um sistema de desbloqueio!")
input("É algo bem simples, Você tera que adivinhar qual numero ira desbloquear o menu!")
input("Te desafio a acertar de primeira")

# PROJETO MENU INTERATIVO

print("╔╗───────╔╗────")
print("║║─╔═╗╔═╗╠╣╔═╦╗")
print("║╚╗║╬║║╬║║║║║║║")
print("╚═╝╚═╝╠╗║╚╝╚╩═╝")
print("──────╚═╝──────")


print("Sistema de desbloqueio!")
login_acesso = 0
while login_acesso != 3:
    print('''    [ 1 ]
    [ 2 ]
    [ 3 ]
    [ 4 ]''')
    login_acesso = int(input("Qual a opção para acessar?: "))
    # Acesso Fake
    if login_acesso == 1:
        print("Sem acesso")
    # Acesso Fake
    elif login_acesso == 2:
        print("Sem acesso")
    # Acesso Real
    elif login_acesso == 3:
        print("Parabens, Acesso liberado!")
    # Acesso Fake
    elif login_acesso == 4:
        print("Sem acesso")

print("║║║║║╔═╗╔═╦╗╔╦╗  ╚║║╝╔═╦╗║╚╗╔═╗╔╦╗╔═╗─║╚╗╠╣╔═╦═╗╔═╗")
print("║║║║║║╩╣║║║║║║║  ╔║║╗║║║║║╔╣║╩╣║╔╝║╬╚╗║╔╣║║╚╗║╔╝║╬║")
print("╚╩═╩╝╚═╝╚╩═╝╚═╝  ╚══╝╚╩═╝╚═╝╚═╝╚╝─╚══╝╚═╝╚╝─╚═╝─╚═╝")


opção = 0
while opção != 6:
    print('''        [ 1 ] Somar
        [ 2 ] Multiplicação
        [ 3 ] Conversor de moedas
        [ 4 ] Multiplicação Fatorial
        [ 5 ] Opção em desenvolvimento
        [ 6 ] Encerrar o Processo''')
    opção = int(input('Qual sua opção?: '))
    # Opção 1
    if opção == 1:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
        soma = n1 + n2
        print("a soma entre {} e {} é {}".format(n1, n2, soma))
    # Opção 2
    elif opção == 2:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
        produto = n1 * n2
        print("A multiplicação entre {} e {} é {}".format(n1, n2, produto))
    # Opção 3
    elif opção == 3:
        real = float(input("Quanto esta o dolar?: "))
        conversor = float(input("Quanto deseja converter?: "))
        resultado = real / conversor
        print("Convertendo R${:.2f} em dolares daria U${:.2f}".format(real, conversor, resultado))
    # Opção 4
    elif opção == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
        n3 = int(input("Digite novamente outro valor: "))
        n4 = int(input("Digite novamente outro valor: "))
        calculo = n1 * n2 * n3 * n4
        print("A multiplicação fatorial entre {} {} {} {} é {}".format(n1, n2, n3, n4, calculo))
    # Encerramento do processo
    elif opção == 5:
        input("O processo esta em fase de desenvolvimento, Pressione qualquer tecla para retornar ao menu de opções!")
    elif opção == 6:
        input("O processo esta sendo encerrado, Pressione qualquer tecla!")
    else:
        print("Opção invalida, Tente novamente!")