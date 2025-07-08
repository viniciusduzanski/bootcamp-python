from loguru import logger

logger.debug("Um aviso para o desenvolvedor")
logger.info("Informação importante do processo")
logger.warning("Um aviso que algo vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu um erro que aborta a aplicação")