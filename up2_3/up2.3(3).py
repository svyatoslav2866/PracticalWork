class Calculation:
    def __init__(self, calculationLine1, calculationLine2):
        self.calculationLine = calculationLine1
        self.calculationLine2 = calculationLine2

    def SetCalculationLine(self, new_calculationLine):
        self.calculationLine = new_calculationLine

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        print(f"значение: {self.calculationLine}")

    def GetLastSymbol(self):
        if len(self.calculationLine) > 0:
            return self.calculationLine[-1]
        return ""

    def DeleteLastSymbol(self):
        if len(self.calculationLine) > 0:
            self.calculationLine = self.calculationLine[: - 1]


value = Calculation("hello", "")

while True:
    choice = int(input("\nВыберите действие:"
                       "\n1 - изменить значение"
                       "\n2 - добавить в конце строки символ"
                       "\n3 - вывести значение свойства"
                       "\n4 - получение последнего символа"
                       "\n5 - удаление последнего сивола из строки"
                       "\n6 - выход из программы"))

    match choice:
        case 1:
           calculationLine1 = input("введите новое значение: ")
           value.SetCalculationLine(calculationLine1)
        case 2:
            symbol = input("добавьте в конце строки символ: ")
            value.SetLastSymbolCalculationLine(symbol)
        case 3:
            value.GetCalculationLine()
        case 4:
            last_symbol = value.GetLastSymbol()
            print(f"последний символ: {last_symbol}")
        case 5:
            value.DeleteLastSymbol()
            print("последний символ удален")
        case 6:
            break
        case _:
            print("неверный выбор!")