"""Exercícios Python - Seção 04

# 1 - Faça um programa ler um número inteiro e o imprima.

valor = 12
print(valor)

# 2 - Faça um programa que leia um número real e o imprima

valor_real = 15.97
print(valor_real)

# 3 - Peça ao usuário para digitar três valores inteiro e imprima a soma deles

print("Insira três valores")

# Método que funcionou para colocar os números e imprimiu só os números
#numeros = [input(), input(), input()]
#print(int(numeros[0]) + int(numeros[1]) + int(numeros[2]))

#print("A soma dos seus números é: " + numeros[0] + numeros[1] + numeros[2]) - funciona, mas
#imprime os valores como uma string (2 + 3 + 5 = 235)

#print("A soma dos seus números é: " + (int(numeros[0] + numeros[1] + numeros[2]))) - não
#funciona, porque precisa concatenar str com str

numeros = [int(input()), int(input()), int(input())]

print("A soma dos seus números é: " + str(numeros[0] + numeros[1] + numeros[2]))

# 4 - Leia um número real e imprima o resultado do quadrado desse número

print("Coloque um número aqui")
num_4 = float(input())
print("O quadrado do seu número é: " + str(num_4 ** 2))

# 5 - Leia um número real e imprima a quinta parte desse número

print("Insira um número real (quebrado) aqui")
num_5 = float(input())
print("A quinta parte do seu número é: " + str(num_5/5))

# 6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.

print("Coloque uma temperatura Celsius aqui")
num_fah = int(input())
F = (num_fah * 1.8) + 32
print("Sua temperatura, em Fahrenheit, é: " + str(F) + " ºF")

# 7 - Leia uma temperatura em graus Fahrenheit e converta-a em Celsius.

print("Coloque uma temperatura Fahrenheit aqui")
num_cel = float(input())
C = (5 * (num_cel - 32))/9
print("Sua temperatura, em Celsius, é: " + str(C) + " ºC")

# 8 - Leia uma temperatura em graus Kelvin e converta-a em Celsius.

print("Coloque uma temperatura Kelvin aqui")
num_kel = float(input())
C2 = num_kel - 273.15
print("Sua temperatura, em Celsius, é: " + str(C2) + " ºC")

# 28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados deles

tres_valores = [int(input()), int(input()), int(input())]

print("A soma do quadrado dos valores é: " + str((tres_valores[0] ** 2) + (tres_valores[1] ** 2) + 
(tres_valores[2] ** 2)))

# 29 - Leia quatro notas, calcule a média aritmética e imprima o resultado

notas = [int(input()), int(input()), int(input()), int(input())]

print("A média das notas é " + str((notas[0] + notas[1] + notas[2] + notas[3])/4))


# 31 - Leia um número inteiro e imprima seu sucessor e seu antecessor

num_int = int(input())

print(str(num_int + 1) + " e " + str(num_int - 1))

# 32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o 
# antecessor de seu dobro

print("Fale aqui o seu número")
num_imp = int(input())

print(((num_imp * 3) + 1) + ((num_imp * 2) - 1))


# 35 - Sejam a e b catetos de um triângulo, a hipotenusa é obtida pela 
# equação: hipo = raizde a² + b². Faça um programa que receba esses valores 
# e calcule a hipotenusa. Imprima o resultado

def hipotenusa(a, b):
    hipo = (((a ** 2) + (b ** 2)) ** 0.5)
    print(hipo)

hipotenusa(4, 10)


# 37 - Faça um programa que leia o valor de um produto e imprima com desconto de 12%

def desconto(a):
    #print(a * 0.88)
    print("Com desconto fica por " + str(a * 0.88))

desconto(24)


# 39 - 780 mil reais serão divididos entre três ganhadores do concurso. O primeiro,
# ganhará 46%, o segundo 32% e o terceiro, o restante. Calcule quanto cada um ganhou

premio = 780_000

print("O primeiro colocado ganhará R$" + str(premio * 0.46) + ", o segundo ganhará R$" +
str(premio * 0.32) + ", e o terceiro ganhará R$" + str(premio * 0.22))


# 40 - Uma empresa contrata um encanador a 30 reais por dia. Faça um programa 
# que solicite o número de dias trabalhados pelo encanador e imprima a quantia 
# líquida que deve ser paga, descontando 8% pro imposto

diaria = 30

tempo = int(input("Quantos dias de trabalho?\n"))

print("Devem pagar R$" + str((tempo * diaria) * 0.92) + " por " + str(tempo) + " dias de trabalho.")


# 43 - Escreva um programa de ajuda para vendedores. 
# A partir de um valor total lido, mostre: o total a pagar com desconto de 10%, 
# o valor de cada parcela (no caso de parcelamento 3x sem juros), 
# comissão do vendedor, no caso de venda à vista (5% sobre o valor com desconto), 
# a comissão do vendedor, no caso de venda parcelada (5% sobre o valor total)

def descontao(a):
    print("O valor com 10% de desconto será de R$" + str(a * 0.9))
    print("O valor de cada parcela de três vezes será de R$" + str(a/3))
    print("A comissão do vendedor, em caso de venda à vista será de R$" + str((a * 0.9) * 0.05))
    print("A comissão do vendedor, em caso de venda parcelada será de R$" + str((a) * 0.05))

descontao(int(input()))


# 44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar 
# subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo

def escada(alt_d, alt):
    print("Para atingir a altura de " + str(alt) + 'cm, serão necessários ' + str(alt/alt_d) + 
    " degraus")

escada(int(input('Indique aqui a altura do degrau\n')), int(input('Indique aqui a altura\n')))


# 46 - Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999). 
# Gere outro número formado pelos dígitos invertidos do número lido. 
# Exemplo: Numerolido = 123 NumeroGerado = 321

numero_escrito = input()
numero_gerado = numero_escrito[::-1]

print(numero_gerado)


# 47 - leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima um dígito por linha

num_4 = input("Coloque um número de 4 dígitos \n")
print(num_4[0])
print(num_4[1])
print(num_4[2])
print(num_4[3])


# 48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos

segundos = int(input("Coloque uma quantidade de segundos aqui\n"))

#print("Isso dá um total de " + str(segundos/3600) + " horas, " + 
#str(segundos/60) + " minutos e " + str(segundos%60) + " segundos.")

print("Isso dá um total de " + str((segundos - segundos%3600)/3600) + " horas, " + 
str(((segundos%3600 - ((segundos%3600)%60))/60)) + " minutos e " + 
str(((segundos%3600)%60)) + " segundos.")



#49 - Faça um programa para ler o horário de início e a duração, em segundos, 
# de uma experiência biológica. O programa deve resultar com o novo horário, 
# do termino da mesma


def experiencia():
    horario = [int(input("Coloque a hora de início\n")), int(input("Coloque os minutos\n")), 
    int(input("Coloque os segundos\n"))]

    duracao = int(input("Coloque a duração, em segundos\n"))

    #calculo_duracao = [((duracao - duracao%3600)/3600), ((duracao%3600 - ((duracao%3600)%60))/60),
    #((duracao%3600)%60) ]
    #horario_final = [(horario[0] + calculo_duracao[0]), (horario[1] + calculo_duracao[1]),
    #(horario[2] + calculo_duracao[2])]

    seg_somados = horario[2] + duracao

    horario_final = [horario[0], horario[1], seg_somados]

    if seg_somados > 59:
        seg_restantes = seg_somados%60
        horario_final[1] = horario[1] + ((seg_somados - (seg_restantes))/60)
        horario_final[2] = 0 + seg_restantes

        if horario_final[1] > 59:
            min_restantes = horario_final[1]%60
            horario_final[0] = horario[0] + ((horario_final[1] - (min_restantes))/60)
            horario_final[1] = 0 + min_restantes

            if horario_final[0] > 23:
                horario_final[0] = horario_final[0] - 24
            
    
    print("O horário inicial do experimento será " + str(horario[0]) + ":" + str(horario[1]) +
    ":" + str(horario[2]) + " e, após uma duração de " + str(duracao) + " segundos, terminará às "
    + str(int(horario_final[0])) + ":" + str(int(horario_final[1])) + ":" + str(horario_final[2]))


print(experiencia())

# 50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua 
# idade e do ano atual

idade = int(input("Diga sua idade\n"))
ano = int(input("Diga o ano que estamos\n"))

print("Você nasceu em " + str(ano - idade))


# 52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve 
# ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um 
# programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um 
# ganharia do prêmio com base no valor investido

aposta = [int(input("A aposta do apostador 1 foi\n")), int(input("A aposta do apostador 2 foi\n")), 
int(input("A aposta do apostador 3 foi\n"))]

aposta_total = aposta[0] + aposta[1] + aposta[2]
prcnt_indv = [(aposta[0]/aposta_total), (aposta[1]/aposta_total), (aposta[2]/aposta_total)]

premio = int(input("O prêmio é de quantos reais?\n"))

print("O primeiro ganhará R$ " + str(premio * prcnt_indv[0]) + ", o segundo ganhará R$ " + 
str(prcnt_indv[1] * premio) + " e o terceiro ganhará R$ " + str(premio * prcnt_indv[2]))


# 53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem 
# como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

c = int(input("O comprimento é:\n"))
l = int(input("A largura é:\n"))
p = int(input("E o preço de metro de tela é:\n"))

print("Para cobrir o total do seu terreno você irá precisar de R$ " + str(p * (2 * (c + l))))


"""












