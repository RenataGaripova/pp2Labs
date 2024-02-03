class MyString:
    value = ""

    def getString(self):
        self.value = input()

    def printString(self):
        print(self.value.upper())

a = MyString()

a.getString()

a.printString()