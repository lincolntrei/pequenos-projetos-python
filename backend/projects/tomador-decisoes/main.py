"""Script principal do projeto Tomador de Decisões. 
Seu objetivo é receber pontos da decisão A e B junto com seus pesos, converter esses pesos em porcentagem e exibir."""

lista_decisao_a = []
lista_decisao_b = []

def adicionar_decisao_a(ponto, peso):
    lista_decisao_a.append([ponto, peso])

def adicionar_decisao_b(ponto, peso):
    lista_decisao_b.append([ponto, peso])

def calcular_porcentagens():
    total_decisao_a = sum(peso for _, peso in lista_decisao_a)
    total_decisao_b = sum(peso for _, peso in lista_decisao_b)
    total = total_decisao_a + total_decisao_b
    porcentagem_decisao_a = (total_decisao_a / total) * 100 if total > 0 else 0
    porcentagem_decisao_b = (total_decisao_b / total) * 100 if total > 0 else 0

    # retorna as porcentagens com 2 numeros decimais
    return round(porcentagem_decisao_a, 2), round(porcentagem_decisao_b, 2)

def resetar_listas():
    global lista_decisao_a, lista_decisao_b
    lista_decisao_a = []
    lista_decisao_b = []

# TESTE: Fazer cirurgia ou não?
adicionar_decisao_a("Benefício da cirurgia", 8)
adicionar_decisao_a("Recuperação mais rápida", 6)
adicionar_decisao_b("Risco de complicações", 5)
adicionar_decisao_b("Custo elevado", 4)

resultado = calcular_porcentagens()
print(f"Decisão A: {resultado[0]}%\nDecisão B: {resultado[1]}%")