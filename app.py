from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

url = 'https://v6.exchangerate-api.com/v6/3cd526eedc01d6c5cb6b58f2/latest/USD'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        montante = request.form.get('montante', type=float, default=0)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            cotação_atual = data['conversion_rates']['BRL']
            valor_convertido =  montante / cotação_atual 
            return render_template('index.html', valor_convertido=f'{valor_convertido:.2f}', montante=montante)
        else:
            return render_template('index.html', erro='Erro ao obter a cotação atual')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


