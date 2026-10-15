import threading


class SingleMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls,*args, **kwargs):
        if cls not in SingleMeta._instances:
            with SingleMeta._lock:
                if cls not in SingleMeta._instances:
                    SingleMeta._instance[cls] = super().__call__(*args, **kwargs)
        return SingleMeta._instances[cls]