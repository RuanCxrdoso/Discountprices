from time import sleep

print("Vamos calcular seu desconto especial !")
sleep(2)
print("A depender da quantidade de parcelas você reberá um desconto !")
sleep(2)
print("À vista receberá 20% de desconto !" "\nEm 2 vezes receberá 15% de desconto !" "\nEm 3 vezes receberá 10% de desconto !")
y = float(input("Insira o valor do produto: "))
x = int(input("Digite em quantas vezes deseja pagar: "))
if x == 1:
    z = y * 0.80
    a = y * 0.20
    print("À vista você receberá 20% de desconto sobre os R${:.2f}".format(y))
    sleep(2)
    print("Seu desconto será de R${:.2f}".format(a))
    sleep(2)
    print("Com o desconto de 20% seu produto sairá por R${:.2f} reais !".format(z))

elif x==2:
    z = y * 0.85
    a = y * 0.15
    print("Em 2 parcelas você reberá 15% de desconto sobre os R${:.2f}".format(y))
    sleep(2)
    print("Seu desconto será de R${:.2f}".format(a))
    sleep(2)
    print("Com o desconto de 15% seu produto sairá por R${:.2f} reais !".format(z))

elif x==3 :
    z = y * 0.90
    a = y * 0.10
    print("Em 3 parcelas você reberá 10% de desconto sobre os R${:.2f}".format(y))
    sleep(2)
    print("Seu desconto será de R${:.2f}".format(a))
    sleep(2)
    print("Com o desconto de 10% o seu produto sairá por R${:.2f} reais !!!".format(z))
else :
    print("Pagando em {} vezes não oferecemos desconto !".format(x))
    sleep(2)
    print("Seu produto sairá por R${:.2f} !".format(y))

quest = input("Deseja calcular outro desconto ?: ")

while quest == "sim":
    sleep(2)
    y = float(input("Insira o valor do produto: "))
    x = input("Digite em quantas vezes deseja pagar: ")
    x = int(x)
    if x == 1:
        z = y * 0.80
        a = y * 0.20
        print("À vista você receberá 20% de desconto sobre os R${:.2f}".format(y))
        sleep(2)
        print("Seu desconto será de R${:.2f}".format(a))
        sleep(2)
        print("Com o desconto de 20% seu produto sairá por R${:.2f} reais !!!".format(z))

    elif x==2:
        z = y * 0.85
        a = y * 0.15
        print("Em 2 parcelas você reberá 15% de desconto sobre os R${:.2f}".format(y))
        sleep(2)
        print("Seu desconto será de R${:.2f}".format(a))
        sleep(2)
        print("Com o desconto de 15% seu produto sairá por R${:.2f} reais !!!".format(z))

    elif x==3 :
        z = y * 0.90
        a = y * 0.10
        print("Em 3 parcelas você reberá 10% de desconto sobre os R${:.2f}".format(y))
        sleep(2)
        print("Seu desconto será de R${:.2f}".format(a))
        sleep(2)
        print("Com o desconto de 10% seu produto sairá por R${:.2f} reais !!!".format(z))
    else :
        print("Pagando em {} vezes não oferecemos desconto !".format(x))
        sleep(2)
        print("Seu produto sairá por R${:.2f} !".format(y))

    quest = input("Deseja calcular outro desconto ?: ")

sleep(2)
print("Obrigado e volte sempre !")
