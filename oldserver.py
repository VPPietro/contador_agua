if env_method == 'GET':
            # Recebe usuários da db
            usuarios = database.get_SELECT(aguadb)
            data = {}
            # Organiza os usuários em um dict
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
            # Converte dict de usuários para JSON e retorna
            data = json.dumps(data)
            status = '200 OK'
            response(status, headers)
            return [data.encode('utf-8')]

elif env_method == 'POST':
    status = '201 CREATED'
    body = get_JSON_REQUEST(environment)
    retorno = {}
    user_http_hash = environment.get("HTTP_AUTHORIZATION")[6:]

    response(status, headers)
    return [b'nothing']

elif env_method == 'POST' or env_method == 'PUT':
    status = '201 CREATED'
    # Recebe JSON da requisição
    body = get_JSON_REQUEST(environment)
    retorno = {}
    # Verifica se JSON é valido e se usuário existe,
    # então CRIA, ATUALIZA ou IGNORA de acordo com o metodo da request
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
    # Caso JSON não seja válido
    except:
        status = '406 NOT_ACCEPTABLE'
        response(status, headers)
        return [b'JSON invalido']
    # Define status de retorno para diferentes cenários e retorna
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
    retorno = {}
    print(environment.get('HTTP_AUTHORIZATION'))
    # Recebe id de usuário que esta tentando deletar
    # testa se foi informado e se é valido
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
    # Testa se existe id validado e então deleta ou ignora
    if database.existente(aguadb, id_usuario=deletion_id):
        retorno = {deletion_id: 'Deleted'}
        database.delete_DELETE(aguadb, deletion_id)
    else:
        retorno = {deletion_id: "Doesn't Exists"}
    # Define status 204 caso não exista o id ou ignora caso exista e retorna
    if not 'Deleted' in retorno.values():
        status = '204 NO_CONTENT'
    response(status, headers)
    retorno = json.dumps(retorno)
    return [retorno.encode('utf-8')]