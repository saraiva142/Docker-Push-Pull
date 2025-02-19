# Comandos para o docker:

docker pull ubuntu

docker run -d -it --name linux0 ubuntu

docker exec -it linux0 bash  
    apt update
    apt install git
    exit

## Criando uma imagem minha

https://docs.docker.com/build/concepts/dockerfile/

docker build -t saraiva1/app-flask-v2 .

Subir para o github: 
    docker login
    docker push saraiva1/app-flask-v2 


Baixar da Jessica:

docker pull jessicavalcante/app-flask-v2

Para Executar a aplicação:
docker run -p 127.0.0.1:8000:8000 jessicavalcante/app-flask-v2

http://localhost:8000/

## Atualizar

docker stop app-web        # Para o container atual
docker rm app-web          # Remove o container antigo
docker build -t app-web .  # Recria a imagem com o código atualizado
docker run --name app-web -p 127.0.0.1:8000:8000 app-web  # Roda um novo container
