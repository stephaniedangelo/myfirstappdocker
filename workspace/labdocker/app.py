# Importando o módulo do Flask e o módulo os 
from flask import Flask
import os

# Objeto da Classe Flask que vamos usar para configurar e executar a aplicação
app = Flask(__name__)

# Definindo a rota padrão da aplicação.
@app.route("/")

# Função que tem como objetivo printar uma mensagem já em formato HTML na tela.
def hello():
    html = "<h3>{message}</h3>"
    return html.format(message=os.getenv("MESSAGE", "Hello world"))

# Garantindo que o módulo não será executado se ele for importado por outro módulo.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
