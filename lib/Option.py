from lib.TextColor import TextColor

class Option:
    def __init__(self, list):
        self._list = list

    def print(self):
        for i in range(0, len(self._list)):
            print(f"{i+1}: {self._list[i][0]}")
        print("q: quit\n")

    def execute(self):
        index = input("Please enter the event: ")
        if index == 'q' :
            print("quit.")
            return False
        try:
            index = int(index)
            self._list[index - 1][1].execute()
        except Exception as e:
            print(TextColor().red("Invalid input."))
            print("error: " + str(e))
            return True
        return True
        