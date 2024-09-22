from executables.TimeCalculator import CalculateDifferenceTime, CalculateTotalTime
from lib.Option import Option

executables_list = [
    ["CalculateDifferenceTime", CalculateDifferenceTime()],
    ["CalculateTotalTime", CalculateTotalTime()]
]

def main():
    main_option = Option(executables_list)
    main_option.print()
    b = True
    while b:
        b = main_option.execute()

if __name__ == "__main__":
    main()
    input("\nPress any key to close the window...")