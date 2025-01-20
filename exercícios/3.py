import json

dados_json = """ 
{
    "faturamento_mensal": [
        {"dia": 1, "valor": 1000},
        {"dia": 2, "valor": 2000},
        {"dia": 3, "valor": 0},
        {"dia": 4, "valor": 1500},
        {"dia": 5, "valor": 3000},
        {"dia": 6, "valor": 0},
        {"dia": 7, "valor": 0},
        {"dia": 8, "valor": 2500},
        {"dia": 9, "valor": 4000},
        {"dia": 10, "valor": 1800}
    ]
}
"""

dados = json.loads(dados_json)
faturamento = dados["faturamento_mensal"]

faturamento_valido = [dia["valor"] for dia in faturamento if dia ["valor"] > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")