# API openapi
Simple CRUD API

***************
REQUISITOS:
***************
<ul>
  <li>Python 3.6.6</li>
  <li>Django Version 1.11.17</li>
  <li>djangorestframework Version 3.9.0</li>
</ul>

********************
COMO UTILIZAR
********************
Execute no terminal dentro do diretório: /Api/openapi/ <br>
    <pre>$python manage.py runserver</pre>

Métodos da API:
- GET: <br>
    url: http://127.0.0.1:8000/api/components/schemas/Contato <br>
        Retorna uma lista com todos os contatos registrados no banco, mostrando 10 registros por página
    <br>    
    url: http://127.0.0.1:8000/api/components/schemas/Contato/{id}
        Retorna o registro do contato com {id} especificado no parâmetro
    <br>    
    url: http://127.0.0.1:8000/api/components/schemas/Contato?page=1&size=4
        Retorna a primeira página com uma lista mostrando 4 registros por página <br>
- POST: <br>
    url: http://127.0.0.1:8000/api/components/schemas/ContatoCreate <br>
        Adiciona um novo contato com valores informados na requisição html <br>
        <pre> Exemplo: { 
                    "nome": "Monty Python",
                    "canal": "email",
                    "valor": "monty@python.com",
                    "obs": "python rules"
                } </pre>
               <br> 
- PUT: <br>
     url: http://127.0.0.1:8000/api/components/schemas/ContatoUpdate/{id} <br>
        Atualiza o registro do contato com {id} especificado no parâmetro com novos valores. <br>
<br>
- DELETE: <br>
     url: http://127.0.0.1:8000/api/components/schemas/Contato/{id}<br>
        Remove o registro do contato com {id} especificado no parâmetro <br>
