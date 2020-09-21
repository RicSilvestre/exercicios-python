"""
# 2 - Leia um número fornecido pelo usuário. Se esse número for positivo , calcule a raiz 
# quadrada do número. Se for negativo, mostre uma mensagem dizendo que o número é inválido

rquad = int(input("Coloque um número\n"))

if rquad > 0:
    print(rquad ** 1/2)
else:
    print("Número inválido")


# 4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: 
# o número digitado ao quadrado e sua raiz quadrada

rquad2 = int(input("Coloque um número\n"))

if rquad2 > 0:
    print("O número ao quadrado é: " + str(rquad2 ** 2))
    print("A raiz quadrada é: " + str(rquad2 *15* (1/2)))


# 5 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar

numparim = int(input("Coloque um número\n"))

if numparim % 2 == 0:
    print("O número " + str(numparim) + " é par")
else:
    print("O número " + str(numparim) + " é ímpar")


# 6 - Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, 
# assim como a diferença existente entre ambos:

num_2 = [int(input("Coloque o primeiro número\n")), int(input("Coloque o primeiro número\n"))]

if num_2[0] > num_2[1]:
    print(num_2[0])
    print(num_2[0] - num_2[1])
else:
    print(num_2[1])
    print(num_2[1] - num_2[0])



# 8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas 
# e exiba na tela a média dessas notas. Uma nota válida deve ser, obrigatoriamente, um valor 
# entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado

#a = 1
#b = 2
#c = True

#rules = [a == 1,
         #b == 2,
         #c == True]

#if all(rules):
    #print("Success!")

notas = [int(input("Diga a nota 1\n")), int(input("Diga a nota 2\n"))]

if notas[0] > 0 and notas[0] < 10 and notas[1] > 0 and notas[1] < 10:
    print("A média é: " + str((notas[0] + notas[1])/2))
else:
    print("Você inseriu uma nota que não é válida")



# 9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a 
# prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso 
# contrário, imprima: Empréstimo concedido

salario = int(input("Insira seu salário aqui\n"))
prestacao = int(input("A prestação do empréstimo é?\n"))

if prestacao > (0.2 * salario):
    print('Empréstimo não concedido')
else:
    print("Empréstimo concedido")



# 10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre 
# seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):

altura = float(input("Coloque sua altura aqui\n"))
sexo = input("Qual seu gênero?\n")

if sexo == "masculino":
    print("Peso ideal é: " + str((72.7 * altura) - 58) + " kg")
elif sexo == "feminino":
    print("Peso ideal é: " + str((62.1 * altura) - 44.7) + " kg")
else:
    print("Insira as palavras "masculino" ou "feminino"")




# 11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, 
# a soma de todos os seus algarismos. Se o número não for maior que 0, terminar com a mensagem 
# "Número Inválido"

NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI
NÃO CONSEGUI

numero_alg = int(input("Escreva seu número\n"))

if numero_alg > 0:
    conv = str(numero_alg)
    i = 1
    soma_um = int(conv[0]) + int(conv[i])
    i += 1
    if conv[i]:
        soma = soma_um + int(conv[i])
        print("A soma é: " + str(soma))
        

    #if numero_alg[i]:

    #soma = int(conv[0]) + int(conv[0:])
    #print("A soma dos algarismos é: " + str(numero_alg[0]))
    #print(soma)




# 13 - Faça um algoritmo que calcule a média ponderada da nota de 3 provas. A primeira e a segunda 
# tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se foi aprovado 
# ou reprovado. A nota deve ser superior a 60 pontos.

notas = [int(input("nota 1\n")), int(input("nota 2\n")), int(input("nota 3\n"))]
media = (notas[0] + notas[1] + (notas[2] * 2))/4

print("Sua média é: " + str(media))
if media > 60:
    print("Parabéns, você foi aprovado")
else:
    print("Infelizmente não rolou")[




# 15 - Escreva um programa que leia um inteiro entre 1 e 7 e diga o dia da semana.

dia = input("Diga o número do dia\n")

if dia == "1":
    print("Seu dia é domingo")
elif dia == "2":
    print("Seu dia é segunda")
elif dia == "3":
    print("Seu dia é terça")
elif dia == "4":
    print("Seu dia é quarta")
elif dia == "5":
    print("Seu dia é quinta")
elif dia == "6":
    print("Seu dia é sexta")
elif dia == "7":
    print("Seu dia é sábado")



# 18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas. 
# O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza 
# a operação, mostrando o resultado e saindo.

oper = input("Escolha uma das operações:\nSoma\nSubtração\nMultiplicação\nDivisão\n")
valores = [int(input("Digite o primeiro valor\n")), int(input("Digite o segundo valor\n"))]

if oper == "soma":
    print("O resultado é: " + str(valores[0] + valores[1]))
elif oper == "subtração":
    print("O resultado é: " + str(valores[0] - valores[1]))
elif oper == "divisão":
    print("O resultado é: " + str(valores[0]/valores[1]))
elif oper == "multiplicação":
    print("O resultado é: " + str(valores[0] * valores[1]))
else:
    print("Insira uma opção válida")




# 19 - Faça um programa pra verificar se determinado número inteiro é divisível por 3 ou 5, mas
# não pelos 2

num_trecinco = int(input("Digite um número\n"))

if not (num_trecinco % 5 == 0 and num_trecinco % 3 == 0) and (num_trecinco % 5 == 0 or num_trecinco % 3 == 0):
    print("Dibas")
else:
    print("Não tá dibas")

# ou método 2:

#if  and num_trecinco % 5 == 0 or num_trecinco % 3 == 0:
#    print("Dibas")
#elif num_trecinco % 5 == 0 and num_trecinco % 3 == 0:
#    print("Não tá dibas")
#else:
#    print("Não tá dibas")



# 20 - Dados três valores, verificar se podem compor um triângulo, e dizer seu tipo

print("Diga três valores")
triang = [int(input()), int(input()), int(input())]

a = triang[0]
b = triang[1]
c = triang[2]

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É um triângulo")

    if a == b and a == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")




# 22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou 
# não se aposentar.

numb3rs = [int(input("idade?\n")), int(input("tempo de carreira?\n"))]

if (numb3rs[0] >= 65) or (numb3rs[1] >= 30) or (numb3rs[0] >= 60 and numb3rs[1] >= 25):
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar")




# 23 - Determine se um ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 
# ou se for divisível por 4 e não for por 100

ano = 2020

if (ano % 400 == 0) or (ano % 4 == 0 and not ano % 100 == 0):
    print("Ano bissexto!")



# 24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui 
# uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa 
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço 
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado 
# não for válido, mostrar uma mensagem de erro.

estados = ["MG", "SP", "RJ", "MS"]
taxa = [1.07, 1.12, 1.15, 1.08]

valor = int(input("Valor?\n"))
# if variavel2 inside array estados[] - como eu escrevo isso?
escolha = input("Estado?\n")

if escolha != estados[-1]:
    print("Estado válido")

    if escolha == estados[0]:
        print("O preço é: R$" + str(valor * taxa[0]))
    elif escolha == estados[1]:
        print("O preço é: R$" + str(valor * taxa[1]))
    elif escolha == estados[2]:
        print("O preço é: R$" + str(valor * taxa[2]))
    elif escolha == estados[3]:
        print("O preço é: R$" + str(valor * taxa[3]))

# ou:

escolha2 = int(input("Digite uma das opções:\n1 - MG\n2 - SP\n3 - RJ\n4 - MS\n"))
var_2 = escolha2 - 1

if estados[var_2]:
    print("O preço é: R$" + str(valor * taxa[var_2]))



# 25 - Calcule as raízes da equação de segundo grau. A variável a tem que ser diferente de zero. 
# Caso seja igual, imprima a mensagem "Não é equação de segundo grau". Se delta > 0, não existe 
# real. Imprima a mensagem "Não existe raiz" 
# Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única". 
# Se delta >= 0, imprima as duas raízes reais.

a = int(input("Valor de a\n"))
b = int(input("Valor de b\n"))
c = int(input("Valor de c\n"))

delta = (b ** 2) - (4 * a * c)
r_delta = (delta ** 0.5)
x1 = - b + r_delta/(2 * a)
x2 = - b - r_delta/(2 * a)

if a != 0:
    print("A equação de segundo grau é: " + str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0")
    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        print("Raiz única de " + str(x1))
    else:
        print("As raízes são: " + str(x1) + " e " + str(x2))



# 26 - Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro 
# em um percurso, calcule o consumo em km/l e escreva uma mensagem de acordo com a tabela abaixo
kml = [int(input("Quantos km?\n")), int(input("Quantos litros?\n"))]

if kml[0]/kml[1] < 8:
    print("Venda o carro!")
elif kml[0]/kml[1] < 14:
    print("Econômico!")
else:
    print("Super econômico!")



# 28 - Faça um programa que leia três numeros inteiros positivos e efetue o cálculo de uma das 
# seguintes médias de acordo com um valor numérico digitado pelo usuário:

print("Digite três numeros")

x = int(input())
y = int(input())
z = int(input())

geometrica = (x * y * z) ** (1/3)
ponderada = (x + (2 * y) + (3 * z))/6
harmonica = 1/(1/x + 1/y + 1/z)
aritmetica = (x + y + z)/3

medias = [geometrica, ponderada, harmonica, aritmetica]

escolha = int(input("Escolha uma opção de cálculo de média:\n1 - Geométrica\n2 - Ponderada\n"
"3 - Harmônica\n4 - Aritmética\n"))

i = escolha - 1

if medias[i]:
    print("A sua média deu: " + str(medias[i]))


# 30 - Faça um programa que receba três números e mostre-os em ordem decrescente:

num_3 = [int(input("Número 1\n")), int(input("Número 2\n")), int(input("Número 3\n"))]
num_3.sort()
num_3.reverse()
print(num_3)



# 32 - Escreva um programa que leia um código de produto de cardápio e a quantidade. O programa 
# deve calcular o valor a ser pago por aquele lanche. 

precos = [1.20, 1.30, 1.50, 1.20, 1.70, 2.20, 1.00]

print("Que produto você quer? Digite o código abaixo\n100 - Cachorro Quente - 1,20\n101 - Bauru "
"Simples - 1,30\n102 - Bauru com Ovo - 1,50\n103 - Hamburguer - 1,20\n104 - Cheeseburger - 1,70"
"\n105 - Suco - 2,20\n106 - Refrigerante - 1,00")

inputs = [int(input()), int(input("Agora diga a quantidade\n"))]

i = inputs[0] - 100

if precos[i]:
    total = precos[i] * inputs[1]
    print("O preço total do seu pedido será: " + str(total.__round__(2)))




# 33 - Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule
# e escreva o preço novo, e escreva uma mensagem em função dele

preco_antigo = int(input("Diga o preço atual\n"))

if preco_antigo < 50:
    preco_novo = preco_antigo * 1.05
elif preco_antigo < 100:
    preco_novo = preco_antigo * 1.10
else:
    preco_novo = preco_antigo * 1.15

print("O preço novo será R$" + str(preco_novo))

if preco_novo < 80:
    print("Barato")
elif preco_novo <= 120:
    print("Normal")
elif preco_novo <= 200:
    print("Caro")
else:
    print("Muito caro")




# 34 - Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela 
# abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

notas = int(input("Qual a nota?\n"))
faltas = int(input("Quantas faltas?\n"))

if notas <= 3.9:
    print("O conceito é E")
elif notas <= 4.9:
    if faltas <= 20:
        print("O conceito é D")
    else:
        print("O conceito é E")
elif notas <= 7.4:
    if faltas <= 20:
        print("O conceito é C")
    else:
        print("O conceito é D")
elif notas <= 8.9:
    if faltas <= 20:
        print("O conceito é B")
    else:
        print("O conceito é C")
elif notas <= 10:
    if faltas <= 20:
        print("O conceito é A")
    else:
        print("O conceito é B")
else:
    print("Nota não válida")

# 36 - Escreva o programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao 
# vendedor. Para calcular a comissão, considere a tabela abaixo:

venda = int(input("Qual o preço da venda?\n"))

if venda < 20_000:
    print("A comissão é de R$" + str(400 + (venda * 0.14)))
elif venda < 40_000:
    print("A comissão é de R$" + str(500 + (venda * 0.14)))
elif venda < 60_000:
    print("A comissão é de R$" + str(550 + (venda * 0.14)))
elif venda < 80_000:
    print("A comissão é de R$" + str(600 + (venda * 0.14)))
elif venda < 100_000:
    print("A comissão é de R$" + str(650 + (venda * 0.14)))
else:
    print("A comissão é de R$" + str(700 + (venda * 0.16)))




# 37 - As tarifas de certo parque de estacionamento são as seguintes: 1a e 2a hora: 1 real cada 
# 3 e 4 hora: 1,4 cada. 5a hora e seguinte: 2 reais cada. O número a pagar é sempre inteiro e 
# arredondado por excesso (61 minutos = pagar 2 horas). Chegada e saída são apresentados na forma 
# de pares de números inteiros. 12 50 = 10 para a uma da tarde. Pretende-se cirar um programa que, 
# lidos os momentos de chegada e saída, escreva o preço cobrado. Intervalo não pode ser superior 
# a 24 horas. Portando, se dada hora de chegada for superior a de partida, não é erro.

chegada = [int(input("Diga a hora do horário de chegada\n")), 
int(input("Diga os minutos do horário de chegada\n"))]

saida = [int(input("Diga a hora do horário de saída\n")), 
int(input("Diga os minutos do horário de saída\n"))]

if (saida[0] < chegada[0]) and (saida[1] - chegada[1]):
    duracao = ((saida[0] - chegada[0]) * -60) + ((saida[1] - chegada[1]) * -1) 
elif saida[0] < chegada[0]:
    duracao = ((saida[0] - chegada[0]) * -60) + (saida[1] - chegada[1])
elif saida[1] < chegada[1]:
    duracao = ((saida[0] - chegada[0]) * 60) + ((saida[1] - chegada[1]) * -1)
else:
    duracao = ((saida[0] - chegada[0]) * 60) + (saida[1] - chegada[1])

if duracao <= 120:
    preco_hora = 1
elif duracao <= 240:
    preco_hora = 1.4
else:
    preco_hora = 2

total_horas = (duracao - (duracao % 60))/60

if duracao % 60 != 0:
    total_horas += 1

print("O preço a ser pago é: R$" + str(total_horas * preco_hora))



# 38 - Leia uma data de nascimento fornecida através de três numeros inteiros. Teste a validade 
# desta data para saber se é válida

print("Digite, em ordem, o dia, mês e ano do seu nascimento")

dia = int(input())
mes = int(input())
ano = int(input())
ano_atual = 2008

if ano > ano_atual:
    print("Ano inválido")
else:
    if ano % 4 == 0:
        if mes == 2:
            if dia > 0 and dia <= 29:
                print("Tudo válido")
            else:
                print("Dia inválido")
    else:
        if mes > 0 and mes <= 12:
            if mes == 2:
                if dia > 0 and dia <= 28:
                    print("Tudo válido")
                else:
                    print("Dia inválido")
            if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia > 0 and dia <= 30:
                    print("Tudo válido")
                else:
                    print("Dia inválido")
            else:
                if dia > 0 and dia <= 31:
                    print("Tudo válido")
                else:
                    print("Dia inválido")
        else:
            print("Mês inválido")


# 39 - Uma empresa decidde dar um aumento aos funcionários de acordo com uma tabela que considera 
# o salário atual e o tempo de serviço. Quem tem salário maior, vai ter um aumento menor, e vice 
# versa. E receberão um bônus adicional de salário baseado no tempo de serviço. Faça um programa 
# que leia o salário atual e o número de anos trabalhando.

salario = int(input("Diz o teu salário\n"))
tempo_servico = int(input("Diz quantos anos trabalha\n"))

if salario <= 500:
    salario_novo = salario * 1.25
elif salario <= 1000:
    salario_novo = salario * 1.2
elif salario <= 1500:
    salario_novo = salario * 1.15
elif salario <= 2000:
    salario_novo = salario * 1.1
else:
    salario_novo = salario

if tempo_servico > 10:
    salario_novo = salario_novo + 500            
elif tempo_servico >= 7:
    salario_novo = salario_novo + 300
elif tempo_servico >= 4:
    salario_novo = salario_novo + 200
elif tempo_servico >= 1:
    salario_novo = salario_novo + 100

if salario_novo == salario:
    print("Sem aumento pra você")
else:
    print("Você teve um aumento de: R$" + str(salario_novo - salario) + ". Seu salário era de R$"
     + str(salario) + " e agora é de R$" + str(salario_novo))



# 40 - O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão e dos 
# impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a 
# tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor

custo_fabrica = int(input("Qual o custo de fábrica?\n"))

if custo_fabrica > 25_000:
    preco_cons = custo_fabrica * 1.35
elif custo_fabrica > 12_000:
    preco_cons = custo_fabrica * 1.25
else:
    preco_cons = custo_fabrica * 1.05

print("O preço pro consumidor é: R$" + str(preco_cons))


"""




