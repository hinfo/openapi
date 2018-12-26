API openapi

***************
REQUISITOS:
***************

Python 3.6.6
Django Version 1.11.17
djangorestframework Version 3.9.0

********************
COMO UTILIZAR
********************
Execute no terminal dentro do diretório: /Api/openapi/
    $python manage.py runserver

Métodos da API:
- GET: 
    url: http://127.0.0.1:8000/api/components/schemas/Contato
        Retorna uma lista com todos os contatos registrados no banco, mostrando 10 registros por página
        
    url: http://127.0.0.1:8000/api/components/schemas/Contato/{id}
        Retorna o registro do contato com {id} especificado no parâmetro
        
    url: http://127.0.0.1:8000/api/components/schemas/Contato?page=1&size=4
        Retorna a primeira página com uma lista mostrando 4 registros por página
- POST:
    url: http://127.0.0.1:8000/api/components/schemas/ContatoCreate
        Adiciona um novo contato com valores informados na requisição html
        Exemplo: {
                    "nome": "Monty Python",
                    "canal": "email",
                    "valor": "monty@python.com",
                    "obs": "python rules"
                }
- PUT:
     url: http://127.0.0.1:8000/api/components/schemas/ContatoUpdate/{id}
        Atualiza o registro do contato com {id} especificado no parâmetro com novos valores.

- DELETE:
     url: http://127.0.0.1:8000/api/components/schemas/Contato/{id}
        Remove o registro do contato com {id} especificado no parâmetro
