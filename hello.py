from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    # HTML com a imagem de fundo e o texto minimalista
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Esportes Extremos</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
                overflow: hidden;
                font-family: Arial, sans-serif;
            }
            .background {
                background-image: url('https://i.ibb.co/xKxyGHY8/template.jpg');
                background-size: cover;
                background-position: center;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .text {
                color: white;
                font-size: 3rem;
                font-weight: bold;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="background">
            <div class="text"> Joao Saraiva </div>
            <div class="text"> Jessica Cavalcante </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)