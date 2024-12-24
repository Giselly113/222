import requests
from bs4 import BeautifulSoup
import json

def get_promotions():
    # URL do site parceiro com promoções
    url = "https://exemplo.com/promocoes"
    
    # Requisição HTTP para obter a página
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar {url}: {response.status_code}")
        return []

    # Parse do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar as promoções (modifique os seletores conforme a estrutura do site)
    promotions = []
    for item in soup.select(".promocao-item"):  # Exemplo de seletor CSS
        title = item.select_one(".titulo").text.strip()
        price = item.select_one(".preco").text.strip()
        link = item.select_one("a")["href"]
        image = item.select_one("img")["src"]
        
        promotions.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image
        })

    return promotions

def save_promotions_to_json(promotions, filename="promotions.json"):
    # Salva as promoções em um arquivo JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(promotions, f, ensure_ascii=False, indent=4)
    print(f"Promoções salvas em {filename}")

def main():
    print("Iniciando coleta de promoções...")
    promotions = get_promotions()
    if promotions:
        save_promotions_to_json(promotions)
        print("Promoções coletadas e salvas com sucesso!")
    else:
        print("Nenhuma promoção encontrada.")

if __name__ == "__main__":
    main()
