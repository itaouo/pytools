class TextColor:
    def red(self, string):
        return "\033[31m"+ string +"\033[0m"
    def green(self, string):
        return "\033[32m"+ string +"\033[0m"
    def yellow(self, string):
        return "\033[33m"+ string +"\033[0m"
    def blue(self, string):
        return "\033[34m"+ string +"\033[0m"