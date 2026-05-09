''' A aplicação realiza a busca do cep via terminal'''

import requests
from models.usuario import Usuario
from models.endereco import Endereco
from exceptions.custom_exception import CustomException

'''Localiza o CEP através da API BrasilAPI'''
def localizar_cep(cep: str):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    return url

'''Pega a localização e retorna um Json com as informações de endereço'''
def requisitar_cep(cep: str):
    localizacao = localizar_cep(cep)
    request = requests.get(localizacao)
    if request.status_code == 200: 
        return request.json()
    else: # Exception Customizado
        raise CustomException("CEP não encontrado, tente novamente!")

'''Exibe os dados informados e pesquisados'''
def exibir_dados():
    resposta = requisitar_cep(cep)  
    endereco = Endereco(cep, resposta['street'], resposta['neighborhood'], resposta['city'], resposta['state'])
    usuario = Usuario(nome, email, endereco)
    usuario.imprimir()

'''Tratamento de erros com Exception Customizada'''

print("\n### Busca Cep ###\n")

try:
    nome = input("Informe seu nome: ")
    email = input("Informe seu email: ")
    cep = input("Informe o CEP: ")

    if nome == "" or email == "" or cep == "":
        raise CustomException("Informe os dados para continuar!")

    exibir_dados()

except CustomException as erro:
    print(f"\nErro: {erro}\n")

except Exception as erro:
    print(f"\nErro: {erro}\n")
