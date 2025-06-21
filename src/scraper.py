import requests
from bs4 import BeautifulSoup
import csv

urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

headers = {'User-Agent': 'Mozilla/5.0'}
resultados = []

for url in urls:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    nome = soup.find("h1").text.strip()
    preco = soup.find("p", class_="price_color").text.strip().replace("£", "R$")

    resultados.append({"Produto": nome, "Preco": preco, "URL": url})

with open("precos.csv", "w", newline="", encoding="windows-1252") as f:
    writer = csv.DictWriter(f, fieldnames=["Produto", "Preco", "URL"])
    writer.writeheader()
    writer.writerows(resultados)

print("✅ Arquivo 'precos.csv' criado com sucesso.")
input("\nPressione Enter para sair...")
