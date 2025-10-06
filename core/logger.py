from logging import (
    Logger, 
    getLogger, 
    Formatter, 
    StreamHandler, 
    INFO
)

import logging



def setting_logger(logger: Logger) -> Logger:
    formatter = Formatter(
        datefmt='%Y-%m-%d %H:%M:%S',
        fmt="%(levelname)s - %(asctime)s - %(name)s - (Line: %(lineno)d) - [%(filename)s]: %(message)s"
    )

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.setLevel(INFO)

    return logger

bot_logger = setting_logger(
    logger=getLogger('bot')
)
api_logger = setting_logger(
    logger=getLogger('api')
)

logging.basicConfig(level=INFO)