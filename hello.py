from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

@app.route("/")
def loading():
    loading_html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Loading...</title>
        <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet">
        <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
        <style>
            body { 
                background:#0b0b0b; 
                padding:0; 
                width:100vw;
                height:100vh; 
                overflow:hidden; 
                font-family:Poppins; 
            }
            .loading-page { 
                background:#161616; 
                width:100%; 
                height:100vh; 
                position: fixed; 
                top: 0; 
                left: 0; 
            }
            .loading-page .counter h1 { 
                position: fixed; 
                top:50%; 
                left:50%; 
                transform:translate(-50%, -50%); 
                color:grey; font-size:100px; 
                font-weight:bolder; 
            }
        </style>
    </head>
    <body>
        <div class="loading-page">
            <div class="counter"><h1>0</h1></div>
        </div>
        <script>
            $(document).ready(function() {
                var counter = 0;
                var c = 0;
                var i = setInterval(function() {
                    $(".loading-page .counter h1").html(c);
                    counter++;
                    c++;
                    if(counter == 101) {
                        clearInterval(i);
                        window.location.href = "/home"; // Redireciona após carregar
                    }
                }, 50);
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(loading_html)

@app.route("/home")
def home():
    main_html = """
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
                font-family: Arial, 
                sans-serif; 
            }
            .background { 
                background-image: url('https://i.ibb.co/xKxyGHY8/template.jpg'); 
                background-size: cover; 
                background-position: center; 
                height: 100%; 
                display: flex; 
                flex-direction: column; 
                justify-content: center; 
                align-items: center; 
            }
            .text { 
                color: white; 
                font-size: 3rem; 
                font-weight: bold; 
                text-align: center; 
                margin: 10px; 
            }
            .discreet-button { 
                position: absolute; 
                bottom: 10px; 
                right: 10px; 
                background: transparent; 
                border: none; 
                color: white; 
                cursor: pointer; 
                font-size: 0.8rem; 
            }
        </style>
    </head>
    <body>
        <div class="background">
            <div class="text"> Joao Saraiva </div>
            <div class="text"> Jessica Cavalcante </div>
            <form action="/form" method="get">
                <button class="discreet-button" type="submit">Form</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(main_html)

## Página de formulário gerada pelo copilot
# Lista para armazenar os dados do formulário
form_data = []
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Aqui você pode adicionar a lógica para criar, atualizar ou deletar dados
        nome = request.form.get("nome")
        sobrenome = request.form.get("sobrenome")
        # Adicione os dados à lista
        form_data.append({"nome": nome, "sobrenome": sobrenome})
        #return jsonify({"message": "Dados enviados com sucesso!"})

    main_html = """
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
                flex-direction: column; 
                justify-content: center; 
                align-items: center; 
            }
            .text { 
                color: white; 
                font-size: 3rem; 
                font-weight: bold; 
                text-align: center; 
                margin: 10px; 
            }
            .form-container { 
                background: rgba(0, 0, 0, 0.5); 
                padding: 20px; 
                border-radius: 10px; 
            }
            .form-container input { 
                margin: 10px 0; 
                padding: 10px; 
                width: 100%; 
            }
            .form-container button { 
                padding: 10px 20px; 
                background: #fff; 
                border: none; 
                cursor: pointer; 
            }
        </style>
    </head>
    <body>
        <div class="background">
            <div class="text"> Joao Saraiva </div>
            <div class="text"> Jessica Cavalcante </div>
            <div class="form-container">
                <form method="POST">
                    <input type="text" name="nome" placeholder="Nome" required>
                    <input type="text" name="sobrenome" placeholder="Sobrenome" required>
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(main_html)
@app.route("/api/form_data", methods=["GET"])
def get_form_data():
    return jsonify(form_data)

@app.route("/results", methods=["GET"])
def results():
    
    main_html = """
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
                flex-direction: column; 
                justify-content: center; 
                align-items: center; 
            }
            .text { 
                color: white; 
                font-size: 3rem; 
                font-weight: bold; 
                text-align: center; 
                margin: 10px; 
            }
            .form-container { 
                background: rgba(0, 0, 0, 0.5); 
                padding: 20px; 
                border-radius: 10px; 
            }
            .form-container input {
                margin: 10px 0; 
                padding: 10px; 
                width: 100%; 
            }
            
            .form-container button { 
                padding: 10px 20px; 
                background: #fff; 
                border: none; 
                cursor: pointer; 
            }
            
            .results { 
                background: rgba(0, 0, 0, 0.5);
                padding: 20px;
                border-radius: 10px; 
                margin-top: 20px; 
                width: 80%; 
            }
            
            .results h2 { 
                color: white; 
                font-size: 2rem; 
            }
            
            .results ul { 
                list-style: none;
                padding: 0; 
            }
            
            .results li { 
                color: white; 
                font-size: 1.2rem; 
                margin: 10px 0; 
            }
            
            .search-container {
                margin: 20px 0; 
            }
            
            .search-container input { 
                padding: 8px; 
                width: 100%; 
            }
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                fetch('/api/form_data')
                    .then(response => response.json())
                    .then(data => {
                        const resultsList = document.getElementById('results-list');
                        const searchInput = document.getElementById('search-input');
                        
                        function renderList(filteredData) {
                            resultsList.innerHTML = '';
                            filteredData.forEach(item => {
                                const li = document.createElement('li');
                                li.textContent = `${item.nome} ${item.sobrenome}`;
                                resultsList.appendChild(li);
                            });
                        }

                        renderList(data);

                        searchInput.addEventListener('input', function() {
                            const searchTerm = searchInput.value.toLowerCase();
                            const filteredData = data.filter(item => 
                                item.nome.toLowerCase().includes(searchTerm) || 
                                item.sobrenome.toLowerCase().includes(searchTerm)
                            );
                            renderList(filteredData);
                        });
                    })
                    .catch(error => console.error('Error fetching data:', error));
            });
        </script>
    </head>
    <body>
        <div class="background">
            <div class="text"> Formulário </div>
            <div class="results">
                <h2>Resultados</h2>
                <div class="search-container">
                    <input type="text" id="search-input" placeholder="Pesquisar...">
                </div>
                <ul id="results-list"></ul>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(main_html)

@app.route("/grid", methods=["GET"])
def grid():
    main_html = """
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
                font-family: Arial, sans-serif; 
            }
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .parent {
                display: grid;
                grid-template-columns: repeat(5, 1fr);
                grid-template-rows: repeat(5, 1fr);
                gap: 8px;
                width: 80%;
                height: 80%;
            }
            .parent img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: 10px;
            }
            .background { 
                background-image: url('https://i.ibb.co/xKxyGHY8/template.jpg'); 
                background-size: cover; 
                background-position: center; 
                height: 100%; 
                display: flex; 
                flex-direction: column; 
                justify-content: center; 
                align-items: center; 
            }
            .card { 
                background: rgba(0, 0, 0, 0.5); 
                border-radius: 10px; 
            }
            .parent {
                display: grid;
                grid-template-columns: repeat(5, 1fr);
                grid-template-rows: repeat(5, 1fr);
                gap: 8px;
            }
                
            .div1 {
                grid-column: span 4 / span 4;
                grid-row: span 3 / span 3;
                border-radius: 10px;
            }

            .div2 {
                grid-row: span 4 / span 4;
                grid-column-start: 5;
                border-radius: 10px;
            }

            .div3 {
                grid-row: span 2 / span 2;
                grid-column-start: 4;
                grid-row-start: 4;
                border-radius: 10px;
            }

            .div4 {
                grid-column-start: 5;
                grid-row-start: 5;
                border-radius: 10px;
            }

            .div5 {
                grid-column: span 3 / span 3;
                grid-row: span 2 / span 2;
                grid-column-start: 1;
                grid-row-start: 4;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="background">
        <div class="parent">
        <div class="div1">
            <img src="https://i.pinimg.com/736x/16/4f/6a/164f6ac2cf536a4e14f359e7a74f1826.jpg" alt="Meu ovo">
        </div>
        <div class="div2">
            <img src="https://i.pinimg.com/474x/77/ec/21/77ec217b8aa8c5a64237666861f8c3e4.jpg" alt="Meu ovo">
        </div>
        <div class="div3">
            <img src="https://i.pinimg.com/474x/87/cc/0d/87cc0d1d6f3355fb117b51ce469d641e.jpg" alt="Meu ovo">
        </div>
        <div class="div4">
            <img src="https://i.pinimg.com/474x/53/f1/44/53f144e7054692f94c3515b87b83bf9e.jpg" alt="Meu ovo">
        </div>
        <div class="div5">
            <img src="https://i.pinimg.com/474x/e8/cd/e5/e8cde521848762bd13327e3d8822b78b.jpg" alt="Meu ovo">
        </div>
</div>
    </body>
    </html>
    """
    return render_template_string(main_html)


if __name__ == "__main__":
    app.run(debug=True)
