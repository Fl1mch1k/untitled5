import requests
from bs4 import BeautifulSoup
import lxml

url = "https://rozetka.com.ua/ua/avtomobilnie-invertori/c4639256/"

agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

response = requests.get(url, headers=agent)

soup = BeautifulSoup(response.text, "lxml")
all_product = soup.find("ul", class_="catalog-grid ng-star-inserted")
list_ptoduct = all_product.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")

for elem in list_ptoduct:
    title = elem.find("span", class_="goods-tile__title")
    price = elem.find("span", class_="goods-tile__price-value").text.replace(u'\ха0', '')
    with open("product.txt", "a", encoding="UTF8") as f:
        f.write(f"{title.text,price} \n ")


