# ========================================
# Exercícios - Manipulação de Listas
# Autor: Thiago Almeida Souza
# ========================================
# ========================================
"""
Objetivo:
Praticar manipulação de listas em Python utilizando:
- Fatiamento 
- Estruturas de repetição 
- Condicionais 
- Funções nativas: sum(), len(), max(), min()
- Listas auxiliares
- Ordenação com sort()
"""
# ========================================

# EXERCÍCIO 1 - Fatiamento e Filtro

#=========================================

precos = [
    1200,350,500,2200,150
]
print('Lista Original: ')
print(precos)

print('\nOs tres primeiros valores')
print(precos[ : 3])


print('\nOs dois ultimos valores')
print(precos[-2:])

print('\nValores maior que 500: ')

for i in precos:
  if i > 500:
    print(i)


print('='*50)


#EXERCICIO 2 - operações matematicas 
print('\nSoma dos valores')
print(sum(precos))#sum() -soma os valores da lista

print('\nMedia dos valores')
print(sum(precos) / len(precos)) #len()- mostrar a quantidade de indices na lsita 

#max - mostrar o maior valor da lista e min mostra o menor valor 
print(f'\nO maior valor é: {max(precos)} e o menor valor é: {min(precos)}')
print('='*50)

#EXERCICIO 3 - Aplicar desconto 
print('\nCrie uma nova lista com 10% de desconto aplicado apenas aos preços acima de 500.')
desconto = []

for i in precos:
  if i > 500:
    i = i * 0.9
    desconto.append(i)
    print('\valores maiores que 500 com 10% de desconto: ')
print(desconto)


#EXERCICIO 4 - Separar valores altos e baixos

precos_altos = []

precos_baixo = []

for n in precos:
  if n > 1000:
    precos_altos.append(n)

  else:
    precos_baixo.append(n)


print('\nValores Acima de 1000')
precos_altos.sort()#sort() - deixa a lista na ordem crescente e sort(reverse=true) - ordem decrescente 
print(precos_altos)

print('\nValores Baixo de 1000')
precos_baixo.sort()
print(precos_baixo)




