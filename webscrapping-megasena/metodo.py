from bs4 import BeautifulSoup

def buscar_resultados(request):
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    uls = soup.find_all("ul",{"class":"balls -lg"})

    lista_resultados = []
    for ul in uls:
        resultado = []
        i=0
        while i < 6:
            resultado.append(int(ul.find_all("li")[i].text))
            i+=1
        lista_resultados.append(resultado)
    return lista_resultados

def criar_variavel_estatistica():
    dic = {}
    for i in range(1, 61):
        dic[i] = 0
    return dic

def contar_resultados(lista_resultados, estatistica):
    for resultado in lista_resultados:
        i=0
        while i < 6:
            estatistica[resultado[i]] = estatistica[resultado[i]] + 1
            i+=1

    return estatistica

def estatistica_lista(dicionario):
    lista = []
    i=1
    while i < 61:
        lista.append({"numero" : str(i),"repeticoes" : "0" + str(dicionario[i])})
        i+=1
    return lista

def criar_variavel_pares():
    dic = {}
    for i in range(1, 61):
        for x in range(i+1, 61):
            dic[str(i) + "-" + str(x)] = 0
    return dic

def contar_pares(lista_resultados, lista_pares):
    for item in lista_resultados:
        for i in range(1, 61):
            for x in range(i+1, 61):
                if i in item and x in item:
                    lista_pares[str(i) + "-" + str(x)] = lista_pares[str(i) + "-" + str(x)] + 1
    return lista_pares

def pares_lista(dicionario):
    lista = []
    for i in range(1, 61):
        for x in range(i+1, 61):
            lista.append({"par" : str(i) + "-" + str(x), "valor" : str(dicionario[str(i) + "-" + str(x)])})
    return lista
