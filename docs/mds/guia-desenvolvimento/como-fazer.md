Como Fazer
==========

## Rodar o Frontend

### Em desenvolvimento
Acessar a pasta do projeto
setar as seguintes variaveis de ambinte:
```.sh
# 'endereço do servidor da api , formato: [protocolo]://[host]:[porta]'
export REACT_APP_BACKEND_HOST=http://localhost:8080
```

### Em produção
Hoje a aplicação tem como C.I o circle.ci
é importante setar a seghinte variavel de ambinete com o endpoint final de puplicação, exemplo 
PUBLIC_URL=https://meusite.com.br


## Rodar o Backend

### Em desenvolvimento

### Em produção


## Rodar o Backend

### Em desenvolvimento

### Em produção

## Rodar a Documentação

### BDD
Pre requisitos
baixar o e colocar no path do sistema operacional
`export PATH=$PATH:/home/xxxxx/Downloads/geckodriver-v0.20.1-linux64`


##  Variaveis de ambiente

```
# spring
export SECRET_MARINA_SERVER=patati-patata

# mysql
export MYSQL_ROOT_PASSWORD=root
export MYSQL_USERNAME=user
export MYSQL_PASSWORD=rooot
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_DATABASE=database

#hibernat
export DATASOURCE_URL="jdbc:mysql://$MYSQL_HOST:$MYSQL_PORT/$MYSQL_DATABASE"
export HIBERNATE_DDL=update

#watson marina
export WATSON_CONVERSATION_WORKSPACE_ID=xxxxxxxxx-xxxx-xxxx-xxxxx-xxxxxxxxxxxx
export WATSON_CONVERSATION_USERNAME=xxxxx-xxxxxx-xxxx-xxxx-xxxxxxxxxxxxx
export WATSON_CONVERSATION_PASSWORD=xxxxxxxxxx

#sqs
export MARINA_QUEUE_REGION=us-east-1
export MARINA_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/000000000000/QueueName

#aws api (backend api)
export REACT_APP_BACKEND_HOST=http://localhost:8080

#React
export PUBLIC_URL=http://localhost:3000
```