import requests
from bs4 import BeautifulSoup
import pandas

print("Vamos iniciar a busca!")
cidade = input("Digite o nome da cidade que deseja buscar imoveis (sem acentos): ").lower().replace(" ", "-")

request = requests.get("https://www.vivareal.com.br/venda/sp/" + cidade + "/")
content = request.content
soup = BeautifulSoup(content,"html.parser")

artigos = soup.find_all("article",{"class":"property-card__container js-property-card"})

imoveis = []
for artigo in artigos:
    imovel = {}
    #descricao
    imovel["descricao"] = artigo.find("span",{"class","property-card__title js-cardLink js-card-title"}).text
    #endereco
    imovel["endereco"] = artigo.find("span",{"class":"property-card__address"}).text
    #area
    imovel["area"] = artigo.find("span",{"class":"property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area"}).text.replace(" ","")
    #quartos
    quarto = artigo.find("li",{"class":"property-card__detail-item property-card__detail-room js-property-detail-rooms"})
    imovel["quarto"] = quarto.find("span").text.replace(" ","")
    #banheiro
    banheiro = artigo.find("li",{"class":"property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom"})
    imovel["banheiro"] = banheiro.find("span").text.replace(" ","")
    #vagas na garagem
    vaga = artigo.find("li",{"class":"property-card__detail-item property-card__detail-garage js-property-detail-garages"})
    imovel["vaga"] = vaga.find("span").text.replace(" ","")
    #preco
    imovel["preco"] = artigo.find("div",{"class":"property-card__price js-property-card-prices js-property-card__price-small"}).text.strip()
    imoveis.append(imovel)

df = pandas.DataFrame(imoveis)
df.to_csv("resultado.csv")