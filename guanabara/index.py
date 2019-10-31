# # TOCANDO UM MP3
# import pygame
# pygame.init()
# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()


# # SORTEANDO UMA ORDEM NA LISTA
# import random
# a1 = str(input('primeiro aluno: '))
# a2 = str(input('segundo aluno: '))
# a3 = str(input('terceiro aluno: '))
# a4 = str(input('quarto aluno: '))
# lista = [a1, a2, a3, a4]
# random.shuffle(lista)
#print(lista)


# # SORTEANDO UM ITEM NA LISTA
# import random
# a1 = str(input('primeiro aluno: '))
# a2 = str(input('segundo aluno: '))
# a3 = str(input('terceiro aluno: '))
# a4 = str(input('quarto aluno: '))
# lista = [a1, a2, a3, a4]
# print('escolhido eh: {}'.format(random.choice(lista)))


# # CATETOS E HIPOTENUSA
# import math
# co = float(input('digite o cateto oposto: '))
# ca = float(input('digite o cateto adjacente: '))
# result = math.hypot(co, ca)
# print('{:.2f}'.format(result))


# # ANALISANDO TEXTOS
# nome = str(input('digite o nome completo: ')).strip() #cortar os espaços antes e depois
# print('nome maiusculo: {}'.format(nome.upper()))
# print('nome minusculo: {}'.format(nome.lower()))
# print('qtd de letras: {}'.format(len(nome) - nome.count(' ')))
# # print('primeiro nome: {}'.format(nome.find(' ')))
# separar = nome.split()
# print('primeiro nome: {}'.format(separar[0]))
# print('qtd de letras 1º nome: {}'.format(len(separar[0])))


# # SEPARANDO DIGITOS DE UM NUMERO
# num = int(input('digite um numero: '))
# print('unidade: {}'.format(num // 1 % 10))
# print('dezena: {}'.format(num // 10 % 10))
# print('centena: {}'.format(num // 100 % 10))
# print('milhar: {}'.format(num // 1000 % 10))


# # VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
# cidade = str(input('digite o nome da cidade: ')).strip()
# print(cidade[:5].lower() == 'santo')


# # PROCURANDO UMA STRING DENTRO DE OUTRA
# nome = str(input('digite seu nome: ')).strip()
# print('tem silva no nome? {}'.format('silva' in nome.lower()))


# # PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING
# frase = str(input('digite a frase: ')).strip().lower()
# print('qtd de vezes aparece a letra A: {}'.format(frase.count('a')))
# print('primeira letra A: {}'.format(frase.find('a')+1))
# print('ultima letra A: {}'.format(frase.rfind('a')+1))


# # PRIMEIRO E ULTIMO NOME
# nome = str(input('digite seu nome completo: ')).lower().strip()
# nome = nome.split()
# print('primeiro nome: {}'.format(nome[0]))
# print('ultimo nome: {}'.format(nome[len(nome)-1]))


# # RANDOM COM IF
# import random
# computador = random.randint(0, 5)
# jogador = int(input('digite um numero: '))
# if jogador == computador:
#     print('jogador ganhou!')
# else:
#     print('computador ganhou!')


# # RADAR ELETRONICO
# speed = int(input('digite sua velocidade: '))
# max_speed = 80
# if speed > max_speed:
#     tax = (speed - max_speed) * 7
#     print('multado! valor: {} reais'.format(tax))
# else:
#     print('segue')


# # PAR OU IMPAR
# num = int(input('digite um numero: '))
# if num % 2 == 0:
#     print('numero eh par!')
# else:
#     print('numero eh impar!')


# # CUSTO DA VIAGEM
# distance = int(input('digite a distancia da viagem: '))
# limit = 200
# if distance > limit:
#     price = distance * 0.45
#     print('valor: {}'.format(price))
# else:
#     price = distance * 0.50
#     print('valor: {}'.format(price))


# # ANO BISSEXTO
# from datetime import date
# year = int(input('digite o ano (0 para ano atual): '))
# if year == 0:
#     year = date.today().year
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('ano bissexto')
# else:
#     print('ano nao eh bissexto')


# # MAIOR E MENOR VALOR
# n1 = int(input('digite o 1 valor: '))
# n2 = int(input('digite o 2 valor: '))
# n3 = int(input('digite o 3 valor: '))
# # minor value
# minor = n1
# if n2 < n1 and n2 < n3:
#     minor = n2
# if n3 < n1 and n3 < n2:
#     minor = n3
# # major value
# major = n1
# if n2 > n1 and n2 > n3:
#     major = n2
# if n3 > n1 and n3 > n2:
#     major = n3
# print('menor: {}'.format(minor))
# print('maior: {}'.format(major))


# # AUMENTOS MULTIPLOS
# salary = int(input('digite o salario: '))
# max_salary = 1250
# if salary <= max_salary:
#     salary = salary + (salary * 0.15)
#     print('novo salario: {}'.format(salary))
# else:
#     salary = salary + salary * 0.10
#     print('novo salario: {}'.format(salary))


# # ANALISANDO TRIANGULO
# r1 = float(input('primeiro segmento: '))
# r2 = float(input('segundo segmento: '))
# r3 = float(input('terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('podem formar triangulos!')
# else:
#     print('nao podem formar triangulos!')

# # APROVANDO EMPRESTIMO
# house_price = float(input('valor da casa: '))
# salary = float(input('valor do salario: '))
# years = int(input('quantos anos: '))
# if house_price / (years * 12) <= salary * 0.30: #prestacao <= 30% do salario
#     print('emprestimo aceitado')
# else:
#     print('emprestimo negado')


# # CONVERSOR DE BASES NUMERICAS
# num = int(input('digite o numero inteiro: '))
# choice = int(input('''escolha a opcao:
# 1- binario
# 2- octal
# 3- hexadecimal
# '''))
# if choice == 1:
#     print('numero binario: {}'.format(bin(num)[2:]))
# elif choice == 2:
#     print('numero octal: {}'.format(oct(num)[2:]))
# elif choice == 3:
#     print('numero hexadecimal: {}'.format(hex(num)[2:]))
# else:
#     print('user burro!')


# # COMPARANDO NUMEROS
# n1 = int(input('digite o primeiro numero: '))
# n2 = int(input('digite o segundo numero: '))
# if n1 == n2:
#     print('iguais!')
# elif n1 > n2:
#     print('primeiro eh maior')
# else:
#     print('segundo eh maior')


# # ALISTAMENTO MILITAR
# from datetime import date
# year = int(input('digite o ano de nascimento: '))
# actual = date.today().year
# age = actual - year
# if age == 18:
#     print('hora de se alistar')
# elif age > 18:
#     print('passou {} ano(s)'.format(age - 18))
# else:
#     print('restam {} ano(s)'.format(18 - age))


# # MEDIA CLASSICA
# n1 = float(input('digite a primeira nota: '))
# n2 = float(input('digite a segunda nota: '))
# avg = (n1 + n2) / 2
# if avg < 5.0:
#     print('media: {} | reprovado'.format(avg))
# elif avg >= 5.0 and avg <= 6.9:
#     print('media: {} | recuperacao'.format(avg))
# else:
#     print('media: {} | aprovado'.format(avg))


# # CLASSIFICANDO ATLETAS
# from datetime import date
# year = int(input('digite o ano de nascimento: '))
# actual = date.today().year
# age = actual - year
# if age <= 9:
#     print('mirim')
# elif age <= 14:
#     print('infantil')
# elif age <= 19:
#     print('junior')
# elif age <= 25:
#     print('senior')
# else:
#     print('master')


# # ANALISANDO TRIANGULOS V2.0
# r1 = float(input('primeiro segmento: '))
# r2 = float(input('segundo segmento: '))
# r3 = float(input('terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('forma um triangulo ', end='')
#     if r1 == r2 == r3:
#         print('equilatero')
#     elif r1 != r2 != r3 != r1:
#         print('escaleno')
#     else:
#         print('isosceles')
# else:
#     print('nao forma um triangulo!')


# # INDICE DE MASSA CORPOREA
# weight = float(input('digite seu peso: '))
# height = float(input('digite sua altura: '))
# imc = weight / (height ** 2)
# print(imc)
# if imc < 18.5:
#     print('abaixo do peso')
# elif 18.5 <= imc < 25:
#     print('peso ideal')
# elif 25 <= imc < 30:
#     print('sobrepeso')
# elif 30 <= imc < 40:
#     print('obesidade')
# else:
#     print('obesidade morbida')


# # GERENCIADOR DE PAGAMENTOS
# price = float(input('digite o valor: '))
# choice = int(input('''condicao de pagamento
# 1- a vista no dinheiro/cheque
# 2- a vista no cartao
# 3- 2x no cartao
# 4- 3x ou mais no cartao
# '''))
# if choice == 1:
#     price = price - (price * 0.1)
#     print('valor final: {}'.format(price))
# elif choice == 2:
#     price = price - (price * 0.05)
#     print('valor final: {}'.format(price))
# elif choice == 3:
#     print('valor final: {}'.format(price))
# elif choice == 4:
#     price = price + (price * 0.2)
#     print('valor final: {}'.format(price))
# else:
#     print('user burro')


# # PEDRA PAPEL TESOURA
# import random
# choice = int(input('''escolha um numero
# 0- pedra
# 1- papel
# 2- tesoura
# '''))
# items = ('pedra', 'papel', 'tesoura')
# computer = random.randint(0, 2)
# print('jogador: {}'.format(items[choice]))
# print('computador: {}'.format(items[computer]))
# if computer == 0: #pedra
#     if choice == 0:
#         print('empate')
#     elif choice == 1:
#         print('jogador vence')
#     elif choice == 2:
#         print('computador vence')
#     else:
#         print('opcao invalida')
# elif computer == 1: #papel
#     if choice == 0:
#         print('computador vence')
#     elif choice == 1:
#         print('empate')
#     elif choice == 2:
#         print('jogador vence')
#     else:
#         print('opcao invalida')
# elif computer == 2: #tesoura
#     if choice == 0:
#         print('jogador vence')
#     elif choice == 1:
#         print('computador vence')
#     elif choice == 2:
#         print('empate')
#     else:
#         print('opcao invalida')

# # CONTAGEM REGRESSIVA
# import time
# for c in range(10, 0-1, -1):
#     print(c)
#     time.sleep(1)
# print('acabou')


# # CONTAGEM DE PARES
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)
# print('fim')


# # SOMA DE IMPARES E MULTIPLOS DE TRES
# sum = 0
# for i in range(1, 500+1):
#     if i % 2 == 1:
#         if i % 3 == 0:
#             print(i)
#             sum += i
# print(sum)


# # TABUADA V2
# num = int(input('digite o numero: '))
# for i in range(0, 10+1):
#     print('{} x {} = {}'.format(num, i, num*i))


# # SOMA DOS PARES
# sum = 0
# for i in range(1, 6+1):
#     num = int(input('digite o {} numero: '.format(i)))
#     if num % 2 == 0:
#         sum += num
# print(sum)


# # PROGRESSAO ARITMETICA
# num = int(input('digite o primeiro termo: '))
# rate = int(input('digite a razao: '))
# dec = num + (10 - 1) * rate
# for i in range(num, dec + rate, rate):
#     print(i)


# # PALINDROMO
# phrase = str(input('digite a frase: ')).strip().lower()
# words = phrase.split()
# together = ''.join(words)
# x = ''
# for i in range(len(together) - 1, -1, -1):
#     x += together[i]
# print('frase: {} | inverso: {}'.format(together, x))
# if together == x:
#     print('palindromo')
# else:
#     print('nao eh palindromo')


# # GRUPO DA MAIORIDADE
# from datetime import date
# min = 0
# max = 0
# for i in range(0, 7):
#     year = int(input('digite o ano de nascimento: '))
#     if date.today().year - year >= 18:
#         max += 1
#     else:
#         min += 1
# print('menores: {} | maiores: {}'.format(min, max))


# # MAIOR E MENOR DA SEQUENCIA
# min = 0
# max = 0
# for i in range(1, 5+1):
#     weight = float(input('peso da {} pessoa: '.format(i)))
#     if i == 1:
#         max = weight
#         min = weight
#     else:
#         if weight > max:
#             max = weight
#         elif weight < min:
#             min = weight
# print('maior peso: {} | menor peso: {}'.format(max, min))


# # ANALISADOR COMPLETO
# avg_age = 0
# max_age = 0
# name_max_age = ''
# qtd_women = 0
# for i in range(1, 4+1):
#     print('{} PESSOA'.format(i))
#     name = str(input('digite o nome: ')).strip()
#     age = int(input('digite a idade: '))
#     gender = str(input('digite o sexo: ')).strip()
#     avg_age += age
#     if gender == 'M':
#         if i == 1:
#             max_age = age
#             name_max_age = name
#         else:
#             if age > max_age:
#                 max_age = age
#                 name_max_age = name
#     if gender == 'F':
#         if age < 20:
#             qtd_women += 1
# avg_age = avg_age / 4
# print('media de idade: {} | nome do homem mais velho: {} | qtd de mulheres menos de 20 anos: {}'.format(avg_age, name_max_age, qtd_women))


# # VALIDACAO DE DADOS
# gender = str(input('digite seu sexo [M/F]: ')).strip().lower()[0]
# while gender not in 'mf':
#     gender = str(input('digite seu sexo [M/F]: ')).strip().lower()[0]
# print('sexo {}'.format(gender))


# # RANDOM COM IF
# import random
# computer = random.randint(0, 5)
# win = False
# while not win:
#     player = int(input('digite um numero: '))
#     if player == computer:
#         print('jogador ganhou!')
#         win = True
#     else:
#         print('computador ganhou!')
#         win = False


# # CRIANDO UM MENU DE OPCOES
# num1 = int(input('digite o primeiro numero: '))
# num2 = int(input('digite o segundo numero: '))
# choice = 0
# while choice != 5:
#     choice = int(input('''escolha uma opcao:
#     1- somar
#     2- multiplicar
#     3- maior
#     4- novos numeros
#     5- sair do programa
#     '''))
#     if choice == 1:
#         print('soma: {}'.format(num1 + num2))
#     elif choice == 2:
#         print('multiplicacao: {}'.format(num1 * num2))
#     elif choice == 3:
#         if num1 > num2:
#             print('{} eh maior'.format(num1))
#         elif num2 > num1:
#             print('{} eh maior'.format(num2))
#         elif num1 == num2:
#             print('sao iguais')
#     elif choice == 4:
#         num1 = int(input('digite o primeiro numero: '))
#         num2 = int(input('digite o segundo numero: '))
#     elif choice == 5:
#         print('logout')
#     else:
#         print('user burro')


# CALCULO DE FATORIAL
# import math
# fat = int(input('digite o numero a ser fatorado: '))
# print(math.factorial(fat))
#---------------------------------------------------
# fat = int(input('digite o numero a ser fatorado: '))
# c = fat
# f = 1
# print('{}! = '.format(fat), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print('{}'.format(f))


# PROGRESSO ARITMETICA V2
# num = int(input('digite o primeiro termo: '))
# rate = int(input('digite a razao: '))
# count = 1
# while count <= 10:
#     print(num)
#     num += rate
#     count += 1


# # PROGRESSO ARITMETICA V3
# num = int(input('digite o primeiro termo: '))
# rate = int(input('digite a razao: '))
# count = 1
# choice = 10
# total = 0
# while choice != 0:
#     total += choice
#     while count <= total:
#         print(num)
#         num += rate
#         count += 1
#     choice = int(input('quantos termos a mais deseja: '))
# print('{} termos'.format(total))


# # SEQUENCIA DE FIBONACCI V1
# num = int(input('quantos termos você quer mostrar: '))
# num1 = 0
# num2 = 1
# count = 3
# print('{} - {}'.format(num1, num2), end='')
# while count <= num:
#     num3 = num1 + num2
#     print(' - {}'.format(num3), end='')
#     num1 = num2
#     num2 = num3
#     count += 1
# print('')
# print('acabou')


# # TRATANDO VARIOS VALORES V1
# sum = 0
# num = 0
# count = 0
# while num != 999:
#     num = int(input('digite um numero [999] para parar: '))
#     if num != 999:
#         sum += num
#         count += 1
# print('qtd de numeros: {} | soma: {}'.format(count, sum))


# # MAIOR E MENOR VALOR
# choice = ''
# count = 0
# sum = 0
# max = 0
# min = 0
# while choice in 's':
#     num = int(input('digite um numero: '))
#     sum += num
#     if count == 0:
#         max = min = num
#     else:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#     count += 1
#     choice = str(input('deseja continuar? [S/N] ')).strip().lower()[0]
# print('media: {} | maior: {} | menor: {}'.format(sum / count, max, min))


# # VARIOS NUMEROS COM FLAG
# n = 0
# count = 0
# sum = 0
# while True:
#     n = int(input('digite um numero (999 para parar): '))
#     if n == 999:
#         break
#     count += 1
#     sum += n
# print(f'qtd de numeros digitados: {count} | soma: {sum}')


# # TABUADA V3
# while True:
#     num = int(input('digite o numero: '))
#     if num < 0:
#         break
#     for i in range(0, 10+1):
#         print('{} x {} = {}'.format(num, i, num*i))


# # PAR OU IMPAR
# import random
# count = 0
# while True:
#     player = int(input('digite um numero: '))
#     computer = random.randint(0, 11)
#     sum = player + computer
#     answer = str(input('par ou impar (P/I): ')).strip().lower()[0]
#     print(computer)
#     if answer == 'p':
#         if sum % 2 == 0:
#             print('jogador venceu!')
#             count += 1
#         else:
#             print('computador venceu!')
#             break
#     if answer == 'i':
#         if sum % 2 == 1:
#             print('jogador venceu!')
#             count += 1
#         else:
#             print('computador venceu!')
#             break
# print(f'vitorias consecutivas: {count}')


# # ANALISE DE DADOS NO GRUPO
# age_18 = 0
# count_man = 0
# count_woman = 0
# while True:
#     age = int(input('digite a idade: '))
#     gender = str(input('digite o sexo (M/F): ')).strip().lower()[0]
#     x = str(input('deseja continuar (S/N): ')).strip().lower()[0]
#     if age > 18:
#         age_18 += 1
#     if gender == 'm':
#         count_man += 1
#     if gender == 'f' and age < 20:
#         count_woman += 1
#     if x == 'n':
#         break
# print('qtd pessoas com mais de 18 anos: {} | qtd de homens: {} | qtd de mulheres com menos de 20: {}'.format(age_18, count_man, count_woman))


# # ESTATISTICAS EM PRODUTOS
# total = 0
# count_1000 = 0
# name_min = ''
# price_min = ''
# count = 0
# while True:
#     name = str(input('digite o nome do produto: ')).strip()
#     price = float(input('digite o valor do produto: '))
#     x = str(input('deseja continuar? (S/N): ')).strip().lower()[0]
#     count += 1
#     total += price
#     if price > 1000:
#         count_1000 += 1
#     if count == 1:
#         name_min = name
#         price_min = price
#     else:
#         if price < price_min:
#             price_min = price
#             name_min = name
#     if x == 'n':
#         break
# print('total gasto: {} | qtd de produtos acima de 1000: {} | nome do mais barato: {}'.format(total, count_1000, name_min))


# # SIMULADOR DE CAIXA ELETRONICO
# value = int(input('digite o valor a ser sacado: '))
# total = value
# ced = 100
# tot_ced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         tot_ced += 1
#     else:
#         if tot_ced > 0:
#             print('{} cedulas de R${}'.format(tot_ced, ced))
#         if ced == 100:
#             ced = 50
#         elif ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 5
#         elif ced == 5:
#             ced = 1
#         tot_ced = 0
#         if total == 0:
#             break


# # NUMERO POR EXTENSO
# cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
# num = int(input('digite um numero entre 0 e 10: '))
# print(cont[num])


# # TUPLAS COM TIMES DE FUTEBOL
# teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
#          'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória',
#          'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
# print('5 primeiros: {}'.format(teams[0:5]))
# print('4 últimos: {}'.format(teams[-4:]))
# print('ordem alfabética: {}'.format(sorted(teams)))
# print('chapecoense tá na {}º posicao'.format(teams.index('Chapecoense')))


# # MAIOR E MENOR VALORES EM TUPLA
# import random
# nums = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
# for i in nums:
#     print('{} '.format(i))
# print('max: {}'.format(max(nums)))
# print('min: {}'.format(min(nums)))


# # ANALISE DE DADOS EM UMA TUPLA
# nums = (int(input('digite o 1 numero: ')), 
#         int(input('digite o 2 numero: ')), 
#         int(input('digite o 3 numero: ')),
#         int(input('digite o 4 numero: ')))
# print('numero 9 apareceu: {} vezes'.format(nums.count(9)))
# if 3 in nums:
#     print('numero 3 apareceu na {} posicao'.format(nums.index(3)+1))
# else:
#     print('o numero 3 nao foi digitado')
# print('numeros pares: ')
# for i in nums:
#     if i % 2 == 0:
#         print(i)


# # LISTA DE PRECOS COM TUPLA
# listing = ('lapis', 1.75,
#             'borracha', 2,
#             'caderno', 15.90,
#             'estojo', 25)
# for i in range(0, len(listing)):
#     if i % 2 == 0:
#         print('produto: {}'.format(listing[i]))
#     else:
#         print('preco: {}'.format(listing[i]))


# # CONTANDO VOGAIS EM TUPLA
# words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis')
# for i in words:
#     print('na palavra {} tem as vogais: '.format(i))
#     for j in i:
#         if j in 'aeiou':
#             print(j)


# # MAIOR E MENOR VALORES NA LISTA
# nums = [int(input('digite o primeiro numero: ')),
#         int(input('digite o segundo numero: ')),
#         int(input('digite o terceiro numero: ')),
#         int(input('digite o quarto numero: ')),
#         int(input('digite o quinto numero: '))]
# # nums = []
# # for i in range(0, 5):
# #     nums.append(int(input('digite o {} numero: '.format(i+1))))
# print('max: {}'.format(max(nums)))
# print('min: {}'.format(min(nums)))


# # VALORES UNICOS EM UMA LISTA
# nums = []
# choice = ''
# while choice in 's':
#     num = int(input('digite um valor: '))
#     if num not in nums:
#         nums.append(num)
#     choice = str(input('deseja continuar? [S/N]: ')).strip().lower()[0]
# nums.sort()    
# print(nums)


# # LISTA ORDENADA SEM REPETICOES
# nums = []
# for i in range(0, 5):
#     num = int(input('digite o {} valor: '.format(i+1)))
#     if i == 0 or num > nums[-1]:
#         nums.append(num)
#     else:
#         pos = 0
#         while pos < len(nums):
#             if num <= nums[pos]:
#                 nums.insert(pos, num)
#                 break
#             pos += 1
# print(nums)


# # EXTRAINDO DADOS DE UMA LISTA
# nums = []
# choice = ''
# while choice in 's':
#     nums.append(int(input('digite um valor: ')))
#     choice = str(input('deseja continuar? [S/N]: ')).strip().lower()[0]
# print('qtd de numeros: {}'.format(len(nums)))
# nums.sort(reverse=True)
# print('decrescente: {}'.format(nums))
# if 5 in nums:
#     print('numero 5 foi digitado')
# else:
#     print('numero 5 nao foi digitado')


# # DIVIDINDO VALORES EM VARIAS LISTAS
# nums = []
# evens = []
# odds = []
# choice = ''
# while choice in 's':
#     num = int(input('digite um valor: '))
#     nums.append(num)
#     choice = str(input('deseja continuar? [S/N]: ')).strip().lower()[0]
#     if num % 2 == 0:
#         evens.append(num)
#     elif num % 2 == 1:
#         odds.append(num)
# print('lista: {}'.format(nums))
# print('pares: {}'.format(evens))
# print('impares: {}'.format(odds))


# # BHASKARA
# a = int(input('digite o valor de A: '))
# b = int(input('digite o valor de B: '))
# c = int(input('digite o valor de C: '))
# delta = (b**2) - (4 * a * c)
# x1 = int((-b + (delta ** (1/2))) / (2 * a))
# x2 = int((-b - (delta ** (1/2))) / (2 * a))
# print('DELTA: {} | X¹ (+): {} | X² (-): {}'.format(delta, x1, x2))


# # VALIDANDO EXPRESSOES MATEMATICAS
# exp = str(input('digite a expressao: '))
# stack = []
# for i in exp:
#     if i == '(':
#         stack.append('(')
#     elif i == ')':
#         if len(stack) > 0:
#             stack.pop()
#         else:
#             stack.append(')')
#             break
# if len(stack) == 0:
#     print('expressao valida!')
# else:
#     print('expressao nao valida!')


# # LISTA COMPOSTA E ANÁLISE DE DADOS
# people = list()
# person = []
# choice = ''
# max_weight = 0
# min_weight = 0
# while choice in 's':
#     person.append(str(input('digite o nome: ')).strip())
#     person.append(float(input('digite o peso: ')))

#     if len(people) == 0:
#         max_weight = min_weight = person[1]
#     else:
#         if person[1] > max_weight:
#             max_weight = person[1]
#         if person[1] < min_weight:
#             min_weight = person[1]
    
#     people.append(person[:])
#     person.clear()
#     choice = str(input('deseja continuar? [S/N]: ')).strip().lower()[0]
# print(people)
# print('qtd de pessoas: {}'.format(len(people)))
# print('maior peso: {}'.format(max_weight))
# print('menor peso: {}'.format(min_weight))


# # LISTAS COM PARES E IMPARES
# nums = [[], []]
# for i in range(0, 7):
#     num = int(input('digite o numero: '))
#     if num % 2 == 0:
#         nums[0].append(num)
#     if num % 2 == 1:
#         nums[1].append(num)
# nums[0].sort()
# nums[1].sort()
# print('pares: {}'.format(nums[0]))
# print('impares: {}'.format(nums[1]))


# # MATRIZ
# matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# evens = third = max_value = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         num = int(input('digite o valor da posicao [{}][{}]: '.format(i, j)))
#         matrix[i][j] = num
#         if num % 2 == 0:
#             evens += num
#         if j == 2:
#             third += num
# for i in range(0, 3):
#     for j in range(0, 3):
#         print('[{}]'.format(matrix[i][j]), end='')
#     print()
# for i in range(0, 3):
#     if i == 0:
#         max_value = matrix[1][0]
#     elif matrix[1][i] > max_value:
#         max_value = matrix[1][i]
# print('soma dos pares: {}'.format(evens))
# print('soma da terceira coluna: {}'.format(third))
# print('maior valor da segunda linha: {}'.format(max_value))


# # MEGA-SENA
# import random
# import time
# listing = list()
# games = list()
# nums = int(input('quantos jogos deseja jogar: '))
# tot = 1
# while tot <= nums:
#     cont = 0
#     while True:
#         num = random.randint(1, 61)
#         if num not in listing:
#             listing.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     listing.sort()
#     games.append(listing[:])
#     listing.clear()
#     tot += 1
# for i, j in enumerate(games):
#     print('jogo {}: {}'.format(i+1, j))
#     time.sleep(1)


# # BOLETIM COM LISTAS COMPOSTAS
# listing = list()
# choice = ''
# while choice in 's':
#     name = str(input('digite o nome: ')).strip()
#     n1 = float(input('digite a n1: '))
#     n2 = float(input('digite a n2: '))
#     avg = (n1 + n2) / 2
#     listing.append([name, [n1, n2], avg])
#     choice = str(input('deseja continuar [S/N]: ')).strip().lower()[0]
# # for i, j in enumerate(listing):
# #     print(f'{i:<4}{j[0]:<10}{j[2]:>8.1f}')
# print(listing)
# while True:
#     student = int(input('qual aluno deseja ver as notas (999 interrompe): '))
#     if student == 999:
#         break
#     if student <= len(listing) - 1:
#         print(f'{listing[student][0]}: {listing[student][1]}')


# # DICIONARIO EM PYTHON
# student = dict()
# student['name'] = str(input('digite o nome do aluno: ')).strip()
# student['avg'] = float(input('digite a media do aluno: '))
# if student['avg'] >= 7:
#     student['status'] = 'aprovado'
# elif student['avg'] >= 5 and student['avg'] < 7:
#     student['status'] = 'recuperacao'
# else:
#     student['status'] = 'reprovado'
# print(student)


# # JOGO DE DADOS EM PYTHON
# import random
# from operator import itemgetter
# game = {
#     'p1': random.randint(1, 6),
#     'p2': random.randint(1, 6),
#     'p3': random.randint(1, 6),
#     'p4': random.randint(1, 6),
# }
# print(game)
# ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
# print(ranking)


# # CARTEIRA DE TRABALHADOR EM PYTHON
# from datetime import datetime
# worker = dict()
# worker['name'] = str(input('digite o nome: ')).strip()
# year = int(input('digite o ano de nascimento: '))
# worker['age'] = datetime.now().year - year
# worker['card'] = int(input('digite a carteira de trabalho: '))
# if worker['card'] != 0:
#     worker['year'] = int(input('digite o ano da contratacao: '))
#     worker['salary'] = float(input('digite o salario: '))
#     worker['old'] = worker['age'] + (worker['year'] + 35) - datetime.now().year
# print(worker)


# # CADASTRO DE JOGADOR DE FUTEBOL
# player = dict()
# games = list()
# player['name'] = str(input('digite o nome do jogador: ')).strip()
# total = int(input('quantas partidas jogou? '))
# for i in range(0, total):
#     games.append(int(input('quantos gols na partida {}? '.format(i+1))))
# player['gols'] = games[:]
# player['total'] = sum(games)
# print(player)


# # UNINDO DICIONARIOS E LISTAS
# person = dict()
# people = list()
# sum_age = 0
# women = 0
# while True:
#     person['name'] = str(input('digite o nome: ')).strip()
#     person['gender'] = str(input('digite o sexo [M/F]: ')).strip().lower()[0]
#     person['age'] = int(input('digite a idade: '))
#     sum_age += person['age']
#     choice = str(input('deseja continuar [S/N]? ')).strip().lower()[0]
#     people.append(person.copy())
#     if choice == 'n':
#         break
# print(people)
# print('qtd de pessoas cadastradas: {}'.format(len(people)))
# print('media das pessoas cadastradas: {}'.format(sum_age/len(people)))
# for i in people:
#     if i['gender'] in 'f':
#         women += 1
# print('qtd de mulheres cadastradas: {}'.format(women))


# # CADASTRO DE JOGADOR DE FUTEBOL
# player = dict()
# games = list()
# team = list()
# while True:
#     player['name'] = str(input('digite o nome do jogador: ')).strip()
#     total = int(input('quantas partidas jogou? '))
#     for i in range(0, total):
#         games.append(int(input('quantos gols na partida {}? '.format(i+1))))
#     player['gols'] = games[:]
#     player['total'] = sum(games)
#     team.append(player.copy())
#     choice = str(input('deseja continuar [S/N]? ')).strip().lower()[0]
#     if choice == 'n':
#         break
#     games.clear()
# print(team)


# # FUNCAO AREA
# def area(width, height):
#     result = width * height
#     print(result)

# width = float(input('digite a largura: '))
# height = float(input('digite o comprimento: '))
# area(width, height)


# # PRINT ESPECIAL
# def write(msg):
#     print('~'*15)
#     print(' {} '.format(msg))
#     print('~'*15)

# write('Hello World!')


# # FUNCAO DE CONTADOR
# def counter(start, end, passer):
#     if start < end:
#         count = start
#         while count <= end:
#             print(count)
#             count += passer
#         print('fim')
#     else:
#         count = start
#         while count >= end:
#             print(count)
#             count -= passer

# start = int(input('digite o valor inicial: '))
# end = int(input('digite o valor final: '))
# passer = int(input('digite o valor do passo: '))
# counter(start, end, passer)


# # FUNCOES PARA SORTEAR E SOMAR
# import random
# def listing(lst):
#     for i in range(0, 5):
#         num = random.randint(1, 10)
#         lst.append(num)
#     print(lst)

# def evens(lst):
#     add = 0
#     for i in lst:
#         if i % 2 == 0:
#             add += i
#     print('soma dos pares: {}'.format(add))

# numbers = list()
# listing(numbers)
# evens(numbers)


# # FUNCOES PARA VOTACAO
# from datetime import datetime
# def votation(year):
#     age = datetime.now().year - year
#     if age >= 18:
#         return 'voto obrigatorio'
#     elif age >= 16 and age < 18:
#         return 'voto opcional'
#     else:
#         return 'voto negado'

# print(votation(2009))


# # FUNCAO PARA FATORIAL
# import math
# def factorial(fat, show=False):
#     if show == False:
#         print(math.factorial(fat))
#     else:
#         c = fat
#         f = 1
#         print('{}! = '.format(fat), end='')
#         while c > 0:
#             print('{}'.format(c), end='')
#             print(' x ' if c > 1 else ' = ', end='')
#             f *= c
#             c -= 1
#         print('{}'.format(f))

# factorial(5, True)


# # ANALISANDO E GERANDO DICIONARIOS
# def results(*num, situation=False):
#     student = dict()
#     student['qtd'] = len(num)
#     student['max'] = max(num)
#     student['min'] = min(num)
#     student['avg'] = sum(num)/len(num)
#     if situation == True:
#         if student['avg'] >= 7.0:
#             student['situation'] = 'aprovado'
#         elif student['avg'] >= 5.0 and student['avg'] < 7.0:
#             student['situation'] = 'recuperacao'
#         else:
#             student['situation'] = 'reprovado'
#     print(student)

# results(5.5, 2.5, 9, 8.5, situation=True)


# # FUNCÕES APROFUNDADAS EM PYTHON
# def readInt(msg):
#     while True:
#         try:
#             num = int(input(msg))
#         except ValueError:
#             print('ERRO - digite um numero inteiro valido')
#         except Exception as error:
#             print('erro: {}'.format(error.__class__))
#         except KeyboardInterrupt:
#             print('usuario encerrou a operacao')
#             break
#         else:
#             print('o numero inteiro: {}'.format(num))
#             break

# readInt('digite o numero: ')


# # SITE ESTA ACESSIVEL
# import urllib.request
# def online_site(url):
#     try:
#         urllib.request.urlopen(url)
#     except urllib.error.URLError:
#         print('site offline')
#     else:
#         print('site online')

# online_site('http://www.pudim.com.br')