from click import option
import requests


def main():
    print('#####################')
    print('### Consulta CEP ###')
    print('#####################')
    print()

    cep_input = input('Digite o CEP para a consulta: ')

    if len(cep_input) != 8:
        print('Quantidade de digitos invalida!')
        exit()

    # Realizando o GET da url e retornando em formato json
    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    # variavel criada para ler o arquivo no formato json,

    addres_data = request.json()

    # caso for digitado um cep invalido ele retornarar um atributo chamado {'erro: true'},
    # if para trata esse erro.
    if 'erro' not in addres_data:
        print('==> CEP ENCONTRADO <==')

        print('CEP: {}'.format(addres_data['cep']))
        print('Logradouro: {}'.format(addres_data['logradouro']))
        print('Complemento: {}'.format(addres_data['complemento']))
        print('Bairro: {}'.format(addres_data['bairro']))
        print('Cidade: {}'.format(addres_data['localidade']))
        print('Estado: {}'.format(addres_data['uf']))

    else:
        print('{}: CEP Invalido.'.format(cep_input))
        print('--------------------------------------')
    # variavel para tratar a finalização da consulta caso nao seja mais realizado

    option = int(
        input('Deseja realiar uma nova consulta ?\n1. Sim \n2. Sair '))
    if option == 1:
        main()
    else:
        print('Finalizando')


if __name__ == '__main__':
    main()
