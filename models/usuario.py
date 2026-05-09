from models.endereco import Endereco

class Usuario:
    '''Modelo: Usuário'''
    def __init__(self, nome: str, email: str, endereco: Endereco):
        self.__nome = nome
        self.__email = email
        self.__endereco = endereco # Associa o endereço
        
    def getter_nome(self):
        return self.__nome
    
    def getter_email(self):
        return self.__email
    
    def getter_endereco(self):
        return self.__endereco
    
    def imprimir(self):
        print("\nNome:", self.getter_nome())
        print("Email:", self.getter_email())
        print("Cep:", self.getter_endereco().getter_cep())
        print("Logradouro:", self.getter_endereco().getter_logradouro())
        print("Bairro:", self.getter_endereco().getter_bairro())
        print("Cidade:", self.getter_endereco().getter_cidade())
        print("Estado:", self.getter_endereco().getter_estado())
        print()
        
