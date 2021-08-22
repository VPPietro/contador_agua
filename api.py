from mysqldb import database
import func

from wsgiref.simple_server import make_server


def web_app(environment, response):
    # Obtendo dados iniciais:
    headers = [('Content-type', 'text/json; charset=utf-8')]
    env_method = environment.get('REQUEST_METHOD')
    usuario_request_hash = func.hash_http_auth(environment.get('HTTP_AUTHORIZATION')[6:]) if environment.get('HTTP_AUTHORIZATION') else False
    try:
        database.open_connection(aguadb)
        usuario = database.get_usuario_if_exists(aguadb, hash=usuario_request_hash) if usuario_request_hash else False
        if usuario:
            idusuario = usuario[0]['idusuario']
            usuario = usuario[0]['nome']
        path_info = int(environment.get('PATH_INFO')[1:]) if environment.get('PATH_INFO')[1:] else 0
    except ValueError:
        path_info = 0
        # func.finaliza_request(status, headers, response, result)
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
            return func.finaliza_request(status, headers, response, result)

        elif env_method == 'POST':
            status = '201 CREATED'
            try:
                database.open_connection(aguadb)
                # Define que o JSON venha de forma correta (somente 'quantidade_agua')
                body = func.get_JSON_REQUEST(environment)
                func.testa_body(body)
                quantidade_agua = body['quantidade_agua']
                # Efetua o POST caso o JSON seja valido
                database.post_INSERT(aguadb, idusuario, quantidade_agua)
                select = database.get_SELECT(aguadb, idusuario)
                result = {usuario: {'input_id': select[-1]['idagua'],'quantidade_agua': quantidade_agua}}
            except:
                status = '406 NOT_ACCEPTABLE'
                result = {"ERROR": "JSON inválido"}
            finally:
                database.close_connection(aguadb)
            # Cria a response com o status (de erro ou sucesso) converte o JSON e retorna
            return func.finaliza_request(status, headers, response, result)

        elif env_method == 'PUT':
            status = '202 ACCEPTED'
            result = []
            try:
                database.open_connection(aguadb)
                # testa a id do input do path info
                func.testa_path_info(path_info)
                # Testa se JSON existe na db para o usuário
                input_db = []
                if path_info:
                    input_db = database.put_SELECT(aguadb, path_info)
                if not input_db:
                    status = '204 NO_CONTENT'
                    result = {"ERROR": "ID do input informado não existe"}
                    raise ValueError
                # Testa o body da requisição para verificar se esta correto e se é igual o que esta na db
                body = func.get_JSON_REQUEST(environment)
                func.testa_body(body)
                if body['quantidade_agua'] == input_db[0]['quantidade']:
                    status = '208 ALREADY_REPORTED'
                    result = {"ERROR": "ID do input informado já possui os mesmos valores passados"}
                    raise ValueError
                # Caso exista o input e o body esteja correto, altera com os dados na db
                database.put_UPDATE(aguadb, body['quantidade_agua'], path_info)
                result = {usuario: {'input_id': path_info, 'quantidade_agua': body['quantidade_agua']}}
            except:
                if not result:
                    status = '406 NOT_ACCEPTABLE'
                    result = {'ERROR': 'JSON ou id informado incorreto'}
            finally:
                database.close_connection(aguadb)
            return func.finaliza_request(status, headers, response, result)

        elif env_method == 'DELETE':
            status = '200 OK'
            result = {'OK': 'Deletado'}
            try:
                database.open_connection(aguadb)
                # testa se path_info esta correto
                func.testa_path_info(path_info)

                # deleta id informado
                rows = database.delete_DELETE(aguadb, path_info)

                if not rows:
                    status = '304 NOT_MODIFIED'
                    result = {'ERROR': 'ID não encontrado'}

            except:
                status = '406 NOT_ACCEPTABLE'
                result = {"ERROR": "ID informado inválido"}
            finally:
                database.close_connection(aguadb)
            return func.finaliza_request(status, headers, response, result)

    else:  # Se não esta logado:
        print('não logado / incorreto')
        status = '401 UNAUTHORIZED'
        retorno = func.json.dumps({'ERROR': 'Credenciais não informadas ou incorretas!'})
        response(status, headers)
        return [retorno.encode('utf-8')]


# Configure sua conexão com o MySQL aqui:
aguadb = database
aguadb.nome_database = 'aguadatabase'
aguadb.nome_user = 'root2'
aguadb.password = 'toor'
database.cria_db(aguadb)

# Sobe o server
with make_server('', 8000, web_app) as server:
    print("Executando")
    server.serve_forever()
