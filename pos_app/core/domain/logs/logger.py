import logging

def setup_loggers():
    logging.basicConfig()
    logger_queries = logging.getLogger('sqlalchemy.engine')
    logger_queries.setLevel(logging.DEBUG)
    logger_connections = logging.getLogger('sqlalchemy.pool')
    logger_connections.setLevel(logging.DEBUG)
    logger_orm = logging.getLogger('sqlalchemy.orm')
    logger_orm.setLevel(logging.INFO)
    
    return logger_queries, logger_connections, logger_orm