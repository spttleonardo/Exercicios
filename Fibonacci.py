"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência 
de Fibonacci e retorne uma mensagem avisando 
se o número informado pertence ou não a sequência. 
"""

def sequencia_fibonacci(num):
    list_fibonacci = [0,1]
    for i in range(1,num*2): 
        list_fibonacci.append(list_fibonacci[i-1]+ list_fibonacci[i])

    return list_fibonacci
    

def verifica_sequencia(seq_fibonacci):
    if num in seq_fibonacci:
        print('Numero esta contido na lista')
    else:
        print('Numero não esta contido na lista')   


num = int(input('Digite um numero para verificar se está na sequência de Fibonacci:  '))

seq_fibonacci = sequencia_fibonacci(num)

verifica_sequencia(seq_fibonacci)