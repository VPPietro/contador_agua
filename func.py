import hashlib
import json

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

def testa_body(body):
    if len(body) != 1 or not body['quantidade_agua'] or not isinstance(body['quantidade_agua'], int) or body['quantidade_agua'] < 1:
        raise ValueError

def testa_path_info(path_info):
    if not isinstance(path_info, int) or path_info < 1:
        raise ValueError

def finaliza_request(status, headers, response, result):
    response(status, headers)
    result = json.dumps(result)
    return [result.encode('utf-8')]
