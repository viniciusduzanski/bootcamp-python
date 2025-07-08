from utils_log import log_decorator

@log_decorator # Estou adicionando toda minha capacidade de log nessa função
def soma(x, y):
    return x + y

soma(2,3)
soma(3,87)