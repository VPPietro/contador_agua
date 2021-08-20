from os import environ
from wsgiref.simple_server import make_server
from mysqldb import database
import json
import hashlib

aguadb = database
# Configure sua conexão com o MySQL aqui:
aguadb.nome_database = 'aguadatabase'
aguadb.nome_user = 'root'
aguadb.password = 'toor'
database.cria_db(aguadb)

def get_JSON_REQUEST(environment):
    """Recebe o JSON do body da requisição"""
    # Pega o comprimento de body do POST
    lenght_input = int(environment.get('CONTENT_LENGTH')) if environment.get('CONTENT_LENGTH') else 0
    # Pega o body do POST de acordo com o comprimento
    body = environment['wsgi.input'].read(lenght_input) if lenght_input > 0 else ''
    # Converte em dict
    return json.loads(body)

def hash_http_auth(http_auth):
        value = hashlib.md5()
        input = '%s:%s' % (http_auth, 'baconzitos')
        if not isinstance(input, bytes):
            input = input.encode('UTF-8')
        value.update(input)
        return value.hexdigest()

def web_app(environment, response):

    # Obtendo dados iniciais:
    headers = [('Content-type', 'text/json; charset=utf-8')]
    env_method = environment.get('REQUEST_METHOD')
    usuario_request_hash = hash_http_auth(environment.get('HTTP_AUTHORIZATION')[6:]) if environment.get('HTTP_AUTHORIZATION') else False
    path_info = environment.get('PATH_INFO')[1:]
    try:
        database.open_connection(aguadb)
        usuario = database.get_usuario_if_exists(aguadb, hash=usuario_request_hash) if usuario_request_hash else False
        if usuario:
            idusuario = usuario[0]['idusuario']
            usuario = usuario[0]['nome']
    finally:
        database.close_connection(aguadb)
    if usuario:  # Se esta logado:

        if env_method == 'GET':
            status = '200 OK'
            # Alterar para mostrar todos os inputs com os ids dos inputs **
            try:
                database.open_connection(aguadb)
                select = database.get_SELECT(aguadb, idusuario)
                num_input = 0
                result = {usuario: {}}
                quantidade_total = 0
                for x in select:
                    id_input = x['idagua']
                    quantidade_agua = x['quantidade']
                    quantidade_total += quantidade_agua
                    num_input += 1
                    result[usuario][num_input] = {"input_id": id_input, "quantidade_agua": quantidade_agua}
                result["quantidade_total"] = quantidade_total
                result['quantidade_inputs'] = len(select)
            finally:
                database.close_connection(aguadb)
            response(status, headers)
            result = json.dumps(result)
            return [result.encode('utf-8')]

        elif env_method == 'POST':
            status = '201 CREATED'
            # adicionar id do input e condição caso o JSON venha errado **
            try:
                database.open_connection(aguadb)
                body = get_JSON_REQUEST(environment)
                quantidade_agua = body[usuario]['quantidade_agua']
                database.post_INSERT(aguadb, idusuario, quantidade_agua)
                result = {usuario: {'quantidade_agua': quantidade_agua}}
            finally:
                database.close_connection(aguadb)

            response(status, headers)
            result = json.dumps(result)
            return [result.encode('utf-8')]

    else:  # Se não esta logado:
        print('não logado / incorreto')
        status = '401 UNAUTHORIZED'
        retorno = json.dumps({'error': 'Credenciais não informadas ou incorretas!'})
        response(status, headers)
        return [retorno.encode('utf-8')]

# criar post para criação de usuario


# Sobe o server
with make_server('', 8000, web_app) as server:
    print("Executando")
    server.serve_forever()
