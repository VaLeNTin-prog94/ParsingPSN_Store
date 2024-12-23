from flask import Flask, request, jsonify
import json


app = Flask(__name__)

# Загружаем данные из JSON файла
with open('discounted_games.json', 'r', encoding='utf-8') as f:
    games_data = json.load(f)


@app.route('/')
def get_all_games():
    return [game for game in games_data]


@app.route('/games', methods=['GET'])
def get_games():
    # Фильтрация по уровню скидки
    min_discount = request.args.get('min_discount', default=0, type=int)
    filtered_games = [game for game in games_data if game['discount_percentage'] >= min_discount]

    return jsonify(filtered_games)


@app.route('/game_details/<int:game_id>', methods=['GET'])
def get_game_details(game_id):
    # Получаем подробности об игре
    game = games_data[game_id]
    return jsonify(game)


if __name__ == '__main__':
    app.run(debug=True)
