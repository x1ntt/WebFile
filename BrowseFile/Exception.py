
# 不是目录异常
class NotIsDirException(Exception):
    def __init__(self, message):
        self.message = message