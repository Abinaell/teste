import requests
from flask import Flask, render_template

app = Flask(__name__)

# URL do arquivo JSON no GitHub
url = 'https://raw.githubusercontent.com/username/repository/main/data.json'

@app.route('/')
def index():
    response = requests.get(url)
    data = response.json()
    users = data.get('users', [])
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
