from threading import Lock
class Database:
    _instance = None
    _lock = Lock()

    def __call__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(cls)
        return cls._instance


'''
    Database
    Loggers
    Analytics
    Cache
'''