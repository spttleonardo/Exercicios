"""
1- Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0; 
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA); 
"""

indice = 13
K = 0
SOMA = 0

while K < indice:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)