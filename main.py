from src import TimeCalculator

_list = [
    TimeCalculator.CalculateDifferenceTime(),
    TimeCalculator.CalculateTotalTime()
]

def main():
    index = 0
    print_option()
    
    while True:
        index = input("Please enter the event: ")
        if index == 'q' :
            print("quit.")
            return
        
        try:
            _list[int(index)-1].execute()
            print()
        except:
            print("Invalid input.")

def print_option():
    for i in range(0, len(_list)):
        print(f"{i+1}: {_list[i].__class__.__name__}")
    print("q: quit\n")

if __name__ == "__main__":
    main()
    input("\nPress any key to close the window...")