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

Para atualizar no git
    docker build -t saraiva1/app-web
    docker tag saraiva1/app-web saraiva1/app-web:v2
    docker login
    docker push saraiva1/app-web:v2


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


# Aula de Volumes / vincular volume em containers

doucker pull ubuntu 

docker run --name linux0 -d -it ubuntu
docker run --name linux1 -d -it ubuntu

docker volume create dados
docker volume ls

docker run --name linux3 -d -it -v dados:/meus-dados ubuntu
docker run --name linux4 -d -it -v dados:/meus-dados ubuntu

docker inspect linux3

Criar uma nova janela:
1° com linux3
docker exec -it linux3 bash
ls -> procurar pasta meus-dados
cd meus-dados
echo "sou o linux03" > linux03.txt
cat linux04.txt


3° com linux4
docker exec -it linux4 bash
ls -> procurar pasta meus-dados
cd meus-dados
cat linux03.txt

