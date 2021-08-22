>GET:
>'/' Necessário realizar uma requisição GET na raiz do endereço do server para receber todos os usuarios com suas informação de consumo de água


>POST:
>'/' Necessário realizar uma requisição POST na raiz do endereço do server com um arquivo JSON no body formatado da seguinte forma para criar um novo input para o usuário logado.
>{
>    "quantidade_agua": 250
>}



>PUT:
>'/' Necessário realizar uma requisição PUT na raiz do endereço do server + /'id_do_input' com um arquivo JSON no body formatado da seguinte forma para alterar um input do usuario
>{
    "quantidade_agua": 100
}
>* Caso não exista será informado na resposta


>DELETE:
>'/id_do_input' Necessário realizar uma requisição DELETE e adicionar / + id do input que deseja deletar
>* caso não exista o id, será informado.


**Lembrando que o usuário deve estar logado para conseguir fazer qualquer requisição na API
