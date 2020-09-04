# Rota de viagem

O projeto é dividido em duas partes, uma api rest em flask e um console app feito em python. Não foram usados frameworks
 além do necessário. 

## Arquitetura

A organização do projeto se da por algumas pastas:

1. challenge
    - Pasta do desafio. Nela tem todas as informações necessárias para realizar essa atividade.
1. data
    - Pasta de dados. Como o arquivo estava em '.txt', ele foi transformado em '.csv'.
1. model
    - Pasta reservada para as regras de negócio, tendo os acessos aos dados.
1. test
    - Pasta reservada para testes unitários.
1. arquivos na pasta raiz

## Api rest

Para subir o serviço você pode executar dois comandos:
* `python app.py`
* `python app.py ./data/input-file.csv`

Temos duas APIs:

### update

API responsável por escrever no arquivo por request json. O endereço é:

`http://localhost:5000/api/update` 

O formato do json é:

`{
    "data": "./data/input-file.csv",
    "line": ["MAO", "REC", "50"]
}`

O retorno desse request é uma mensagem positiva ou negativa do cadastro da rota.

### route

API responsável por pesquisar a rota mais baratas dentre todas as possibilidades, por via de um request json. O 
endereço é:

`http://localhost:5000/api/route`

O formato do json é:

`{
    "origem": "GRU",
    "destino":"CDG"
}`

## Console app

A aplicação de console terá as mesmas funcionalidades da API rest, cadastrar uma nova rota e consultar a rota mais 
barata dentre todas as possibilidades. O sistema de navegação entre as funcionalidades da aplicação se dar por meio do 
terminal, usando input text (1, 2 ou 3).

### update

Será possivel cadastrar novos roteiros, incluindo o preço, seguindo o exemplo:

`GRU-CDG-75`

### route

Será feito uma consulta via terminal, seguindo o exemplo:

`GRU-CDG`

## SonarCloud validation [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Washingtonban_rota_viagem&metric=alert_status)](https://sonarcloud.io/dashboard?id=Washingtonban_rota_viagem)