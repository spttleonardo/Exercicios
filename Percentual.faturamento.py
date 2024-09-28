"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
•	SP – R$67.836,43 
•	RJ – R$36.678,66 
•	MG – R$29.229,88 
•	ES – R$27.165,48 
•	Outros – R$19.849,53 

Escreva um programa na linguagem que desejar onde calcule o percentual 
de representação que cada estado teve dentro do valor total mensal da distribuidora. 
"""

# criando dicionario para os faturamento no mes:
faturamento_dist = {'SP': 67836.43, 'RJ': 36678.66 , 'MG': 29229.88, 'ES': 27165.48 ,'Outros': 19849.53}

# criando dicionario para o percentual
percentual = {}

# obtendo o total do faturamento
faturamento_total = sum(faturamento_dist.values())

# laço para verificar o percentual do faturamento de cada estado
for estado, faturamento in faturamento_dist.items():
    percent = round(faturamento*100/faturamento_total, 2)
    percentual[estado] = percent

print(f' O percentual de cada estada é {percentual}')
