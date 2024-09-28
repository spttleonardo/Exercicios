"""
Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
b) Evite usar funções prontas, como, por exemplo, reverse; 
"""

string = str(input("Informe uma string: "))

# variável para armazenar a string invertida
invertida = ""

# laço que percorre a string original de trás para frente
for i in range(len(string) - 1, -1, -1):
    invertida += string[i]

print(invertida)