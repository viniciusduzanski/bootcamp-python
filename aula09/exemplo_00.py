from loguru import logger
from sys import stderr

# logger.add("meu_log.log", level="CRITICAL") # Vai criar automaticamente um arquivo de log e salvar somente os de nível CRITICAL

# Removendo os handlers existentes para evitar duplicação
logger.remove()

# Configuração do logger para stderr
logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# Configuração do logger para arquivo de log
logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

logger.add(
                "meu_arquivo_de_logs_critical.log",
                format="{time} {level} {message} {file}",
                level="CRITICAL"
            )

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Você digitou valores corretos {soma}")
        return soma
    except:
        logger.critical("Você tem digitar valores corretos")

(soma(2,3)) # Vai gerar um log info
(soma(2,"3")) # Vai gerar um erro CRITICAL porque vai cair no except
