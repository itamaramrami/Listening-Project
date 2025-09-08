import logging
from elasticsearch import Elasticsearch
from datetime import datetime



class Logger_log:
    _logger = None
    @classmethod
    def get_logger(cls, name="logger_name", es_host='http://localhost:9200',
        index="logger_loges", level=logging.DEBUG):
            if cls._logger:
                return cls._logger
            logger = logging.getLogger(name)
            logger.setLevel(level)
            if not logger.handlers:
                es = Elasticsearch(es_host)
                if not es.indices.exists(index=index):
                    es.indices.create(index=index)
            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(index=index, document={
                        "timestamp": datetime.utcnow().isoformat(),
                        "level": record.levelname,
                        "logger": record.name,
                        "message": record.getMessage()
                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())
            cls._logger = logger
            return logger


# a=Logger.get_logger()

# a.info("itamar")
# a.error("amrami")
# v=Alastic()
# print(v.GetData())