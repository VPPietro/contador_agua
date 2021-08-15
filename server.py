from wsgiref.simple_server import make_server
from mysqldb import database
import json

aguadb = database
aguadb.nome_database = 'aguadatabase'
aguadb.nome_user = 'root2'
aguadb.password = 'toor'
database.cria_db(aguadb)

def get_JSON_REQUEST(environment):
    # Pega o comprimento de body do POST
    lenght_input = int(environment.get('CONTENT_LENGTH')) if environment.get('CONTENT_LENGTH') else 0
    # Pega o body do POST de acordo com o comprimento
    body = environment['wsgi.input'].read(lenght_input) if lenght_input > 0 else ''
    # Converte em dict
    return json.loads(body)

def web_app(environment, response):
    headers = [('Content-type', 'text/json; charset=utf-8')]
    env_method = environment.get('REQUEST_METHOD')

    if env_method == 'GET':
        usuarios = database.get_SELECT(aguadb)
        data = {}
        for x in usuarios:
            temp_result = database.get_SELECT(aguadb, x['idusuario'])
            try:
                database.open_connection(aguadb)
                data[x['nome']] = {'quantidade_agua': 0, 'quantidade_inputs': 0, 'id': database.get_idusuario(aguadb, x['nome'])}
            finally:
                database.close_connection(aguadb)
            for y in temp_result:
                data[x['nome']]['quantidade_agua'] += y['quantidade']
                data[x['nome']]['quantidade_inputs'] += 1
        data = json.dumps(data)
        status = '200 OK'
        response(status, headers)
        return [data.encode('utf-8')]

    elif env_method == 'POST' or env_method == 'PUT':
        status = '201 CREATED'
        body = get_JSON_REQUEST(environment)
        retorno = {}
        try:
            lista_nomes = list(body.keys())
            for x in lista_nomes:
                if database.existente(aguadb, x):
                    if env_method == 'POST':
                        retorno[x] = 'Already Exists'
                    else:
                        retorno[x] = 'Updated'
                        database.put_UPDATE(aguadb, x, body[x]['quantidade_agua'])
                else:
                    if env_method == 'POST':
                        retorno[x] = 'Created'
                        database.post_INSERT(aguadb, x, body[x]['quantidade_agua'])
                    else:
                        retorno[x] = "Doesn't Exists"
        except:
            print('JSON invalido')
            status = '406 NOT_ACCEPTABLE'
            response(status, headers)
            return [b'JSON invalido']

        if not 'Created' in retorno.values() and env_method == 'POST':
            status = '208 ALREADY_REPORTED'
        elif not 'Updated' in retorno.values() and env_method == 'PUT':
            status = '204 NO_CONTENT'
        elif 'Updated' in retorno.values() and env_method == 'PUT':
            status = '202 ACCEPTED'
        response(status, headers)
        retorno = json.dumps(retorno)
        return [retorno.encode('utf-8')]

    elif env_method == 'DELETE':
        status = '200 OK'
        body = get_JSON_REQUEST(environment)
        retorno = {}
        try:
            deletion_id = int(environment.get('PATH_INFO')[1:])
        except:
            status = '304 NOT_MODIFIED'
            response(status, headers)
            return [b'Sem id para deletar']
        if deletion_id <= 0:
            status = '304 NOT_MODIFIED'
            response(status, headers)
            return [b'Sem id para deletar']
        try:
            if database.existente(aguadb, id_usuario=deletion_id):
                retorno = 'Deleted'
                database.delete_DELETE(aguadb, deletion_id)
            else:
                retorno = "Doesn't Exists"
        except:
            print('JSON inválido')
            status = '406 NOT_ACCEPTABLE'
            response(status, headers)
            return [b'JSON invalido']
        if not 'Deleted' in retorno:
            status = '204 NO_CONTENT'
        response(status, headers)
        retorno = json.dumps(retorno)
        return [retorno.encode('utf-8')]

with make_server('', 8000, web_app) as server:
    print("Executando")
    server.serve_forever()
