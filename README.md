>GET:
>'/' Necessário realizar uma requisição GET na raiz do endereço do server para receber todos os usuarios com suas informação de consumo de água


>POST:
>'/' Necessário realizar uma requisição POST na raiz do endereço do server com um arquivo JSON no body formatado da seguinte forma para criar um ou mais novo(s) >usuario(s) e sua(s) informação(ões) de consumo de água iniciais
>{
    "zezinho": {
        "quantidade_agua": 250
    }
}
>* caso já exista será ignorado


PUT:
'/' Necessário realizar uma requisição PUT na raiz do endereço do server com um arquivo JSON no body formatado da seguinte forma para atualizar um ou mais consumo(s) de um usuario
{
    "zezinho": {
        "quantidade_agua": 100
    },
    "joaozinho":{
        "quantidade_agua": 200
    }
}
* Caso não exista será ignorado


DELETE:
'/id_usuario' Necessário realizar uma requisição DELETE e adicionar / + id do usuario que deseja deletar
* caso não exista o id, será ignorado.


**Lembrando que o usuário deve estar logado para conseguir fazer qualquer requisição na API
