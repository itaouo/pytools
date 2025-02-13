from lib.CustomException import Fail, Success
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
            index = int(index) - 1
            if index < 0 and index > len(self._list): raise Exception
        except:
            print(TextColor().red("Invalid event.\n"))
            return True

        try:
            self._list[index][1].execute()
        except Fail as e:
            print(e)
        except Success as e:
            print(e)
        except Exception as e:
            print(TextColor().red(f"[Exception]: {str(e)}"))
        print()
        return True
        