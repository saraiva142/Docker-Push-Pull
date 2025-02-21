from flask import Flask, render_template_string

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
            body { background:#0b0b0b; padding:0; width:100vw; height:100vh; overflow:hidden; font-family:Poppins; }
            .loading-page { background:#161616; width:100%; height:100vh; position: fixed; top: 0; left: 0; }
            .loading-page .counter h1 { position: fixed; top:50%; left:50%; transform:translate(-50%, -50%); color:grey; font-size:100px; font-weight:bolder; }
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
            body, html { margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: Arial, sans-serif; }
            .background { background-image: url('https://i.ibb.co/xKxyGHY8/template.jpg'); background-size: cover; background-position: center; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; }
            .text { color: white; font-size: 3rem; font-weight: bold; text-align: center; margin: 10px; }
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
    return render_template_string(main_html)

if __name__ == "__main__":
    app.run(debug=True)
