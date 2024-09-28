"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
• O menor valor de faturamento ocorrido em um dia do mês; 
• O maior valor de faturamento ocorrido em um dia do mês; 
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

IMPORTANTE: 
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 
"""
# importando módulos
import json

# abrindo arquivo json
with open("./Faturamento/dados.json") as file:
    data = json.load(file)

print(type(data))

def armazena_faturamento(data):
    """Armazena os dias e seus respectivos faturamento em um dicionario 

    Args:
        data (class 'list'): _description_

    Returns:
        _type_: _description_
    """
    faturamento = {}
    for i in range(len(data)):
        if data[i]['valor'] != 0.0:
            faturamento[data[i]['dia']] = data[i]['valor']
    return faturamento

# criando dicionarios
faturamento = armazena_faturamento(data)
print(type(faturamento))
faturamento_sup = {}


for i in range(len(data)):
    if data[i]['valor'] != 0.0:
        faturamento[data[i]['dia']] = data[i]['valor']

faturamento_min = min(faturamento.values())
faturamento_max = max(faturamento.values())

print(f'O menor valor de faturamento ocorrido em um dia do mes e de {faturamento_min}')
print(f'O maior valor de faturamento ocorrido em um dia do mes e de {faturamento_max}')

faturamento_mean = sum(faturamento.values())/len(faturamento.values())

for i in range(len(data)):
    if data[i]['valor'] > faturamento_mean:
        faturamento_sup[data[i]['dia']] = data[i]['valor']

print(f'O faturamento medio e de {faturamento_mean}.')
print(f'O numero de dias que teve o faturamento acima da media e {len(faturamento_sup)}\n.Sao eles: {faturamento_sup}')