
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL страницы с акциями
url = "https://store.playstation.com/en-tr/category/83a687fe-bed7-448c-909f-310e74a71b39/1"

# Выполняем HTTP запрос
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Находим элементы, содержащие информацию об играх
games = soup.find_all('div',    class_="psw-l-w-1/1")
# Хранение информации о играх
game_data = []
#Проходим по всем найденным элементам и извлекаем нужную информацию
try:
    for k in range(0, 1000):
        for item in soup.find_all('div', class_='psw-l-w-1/1'):
            title = item.find_all_next('span', 'psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2')[k].text.strip()
            current_price = item.find_all_next('span', 'psw-m-r-3')[k].text[:-3]
            old_price = item.find_all_next('s', 'psw-c-t-2')[k].text.strip()[:-3]
            discount_percentage = item.find_all_next('span',
                                     'psw-body-2 psw-badge__text psw-badge--none psw-text-bold psw-p-y-0 psw-p-2 psw-r-1 psw-l-anchor')[k].text.strip()
            k += 1

            # Добавляем данные в список
            game_data.append({
                'title': title,
                'current_price': current_price,
                'old_price': old_price,
                'discount_percentage': discount_percentage,
            })
except:
    pass

# Сохранение данных в формате JSON
with open('discounted_games.json', 'w', encoding='utf-8') as json_file:
    json.dump(game_data, json_file, ensure_ascii=False, indent=4)

# Сохранение данных в формате CSV
df = pd.DataFrame(game_data)
df.to_csv('discounted_games.csv', index=False)

print("Данные успешно сохранены в discounted_games.json и discounted_games.csv")