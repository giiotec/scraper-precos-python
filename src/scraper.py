import requests
from bs4 import BeautifulSoup
import csv

# URLs simuladas
urls = [
    "https://example.com/produto-a",
    "https://example.com/produto-b"
]

headers = {"User-Agent": "Mozilla/5.0"}
resultados = []

for url in urls:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    nome = soup.title.text.strip() if soup.title else "Produto Desconhecido"
    preco = "R$ 99,90"  # Preço simulado

    resultados.append({"Produto": nome, "Preço": preco, "URL": url})

with open("precos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Produto", "Preço", "URL"])
    writer.writeheader()
    writer.writerows(resultados)

print("✓ Arquivo precos.csv criado com sucesso.")
