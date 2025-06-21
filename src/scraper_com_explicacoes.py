# scraper_com_explicacoes.py
# Script para extrair nome e preço de produtos de páginas HTML e exportar para CSV.

import requests  # Faz requisições HTTP
from bs4 import BeautifulSoup  # Faz o parser do HTML
import csv  # Salva os dados em formato CSV

# Lista de URLs reais a serem raspadas
urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

# Define um cabeçalho padrão para "enganar" o servidor e evitar bloqueios
headers = {'User-Agent': 'Mozilla/5.0'}

# Lista para armazenar os resultados extraídos
resultados = []

# Loop pelas URLs
for url in urls:
    r = requests.get(url, headers=headers)  # Requisição HTTP GET
    soup = BeautifulSoup(r.text, "html.parser")  # Parser do HTML

    # Extração do nome do produto
    nome = soup.find("h1").text.strip()

    # Extração do preço
    preco = soup.find("p", class_="price_color").text.strip().replace("£", "R$")

    # Adiciona os dados à lista de resultados
    resultados.append({"Produto": nome, "Preço": preco, "URL": url})

# Cria o arquivo CSV com os resultados
with open("precos.csv", "w", newline="", encoding="windows-1252") as f:
    writer = csv.DictWriter(f, fieldnames=["Produto", "Preço", "URL"])
    writer.writeheader()
    writer.writerows(resultados)

print("✅ Arquivo 'precos.csv' criado com sucesso.")
input("\nPressione Enter para sair...")
