class CustomException(Exception):
    '''Exception Customizada para evento de buscar CEP'''
    def __init__(self, mensagem):
        super().__init__(mensagem)
        