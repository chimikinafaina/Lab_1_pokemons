from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Чтение списка покемонов из файла
def read_pokemon_list():
    with open('file.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# Инициализация списка покемонов
pokemon_list = read_pokemon_list()

@app.route('/')
def index():
    return render_template('index.html', pokemon_list=pokemon_list)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        pokemon_name = request.form['pokemon_name']
    else:
        pokemon_name = request.args.get('pokemon_name')

    if pokemon_name in pokemon_list:
        return f'Покемон {pokemon_name} найден в списке!'
    else:
        return f'Покемон {pokemon_name} не найден в списке.'

if __name__ == '__main__':
    app.run(debug=True)