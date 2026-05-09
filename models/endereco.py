class Endereco:
    '''Modelo: Endereço'''
    def __init__(self, cep: str, logradouro: str, bairro: str, cidade: str, estado: str):
        self.__cep = cep
        self.__logradouro = logradouro
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
 
    def getter_cep(self):
        return self.__cep 

    def getter_logradouro(self):
        return self.__logradouro    

    def getter_bairro(self):
        return self.__bairro
    
    def getter_cidade(self):
        return self.__cidade

    def getter_estado(self):
        return self.__estado
    
    