from lib.TextColor import TextColor

class Fail(Exception):
    def __init__(self, type, info = ""):
        self.type = type
        self.info = info
        if info == "":
            super().__init__(TextColor().red(f"[{self.type}]"))
        else:
            super().__init__(TextColor().red(f"[{self.type}]: {self.info}"))

class Success(Exception):
    def __init__(self, info = "success."):
        self.type = type
        self.info = info
        super().__init__(TextColor().green(self.info))
