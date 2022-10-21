import requests
import pandas
import metodo

request = requests.get("https://www.megasena.com/resultados/ano-2022")
resultados2022 = metodo.buscar_resultados(request)
request = requests.get("https://www.megasena.com/resultados/ano-2021")
resultados2021 = metodo.buscar_resultados(request)
request = requests.get("https://www.megasena.com/resultados/ano-2020")
resultados2020 = metodo.buscar_resultados(request)

estatisticas = metodo.criar_variavel_estatistica()
estatisticas = metodo.contar_resultados(resultados2022, estatisticas)
df = pandas.DataFrame(metodo.estatistica_lista(estatisticas))

estatisticas = metodo.contar_resultados(resultados2021, estatisticas)
estatisticas = metodo.contar_resultados(resultados2020, estatisticas)
df = pandas.DataFrame(metodo.estatistica_lista(estatisticas))
print("Numeros repedidos 2020 a 2022:\n", df.sort_values(by=["repeticoes", "numero"], ascending=False).to_string(index=False))
df.to_csv("NumerosRepeditos2020-2022.csv")

pares = metodo.criar_variavel_pares()
pares = metodo.contar_pares(resultados2022, pares)
pares = metodo.contar_pares(resultados2021, pares)
pares = metodo.contar_pares(resultados2020, pares)
df = pandas.DataFrame(metodo.pares_lista(pares))
print("\nPares 2020 a 2022:\n", df.sort_values(by=["valor", "par"], ascending=False).to_string(index=False))
df.to_csv("ParesRepetidos2020-2022.csv")
