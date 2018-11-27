#import tkinter#
from tkinter import *

#define constants used for fonts#
HEADER_FONT = "Arial", 12
BUTTON_FONT = "Arial", 8, "bold"
NORMAL_FONT = "Arial", 10
PROMPT_FONT = "Arial", 10, "italic"

#define main class#
class BankManager:
    def __init__(self):
        window = Tk()
        window.title("Friendly Bank")
        window.geometry("500x300")

        welcome = Label(window, text = "Welcome to the Friendly Bank account manager app!", font = HEADER_FONT)
        welcome.pack()

        deposit = Button(window, text = "Make a deposit", font = BUTTON_FONT, command = DepositPage)
        deposit.pack()

        
#create window to make deposits#
class DepositPage:
    def __init__(self):
        window = Tk()
        window.title("Deposits")

        makeDeposit = Label(window, text = "Where would you like to make the deposit?", font = HEADER_FONT)
        makeDeposit.pack()

        savingsBtn = Button(window, text = "Savings Account", font = BUTTON_FONT, command = SavingsPage)
        savingsBtn.pack()

        checkingBtn  = Button(window, text = "Checking Account", font = BUTTON_FONT, command = CheckingPage)
        checkingBtn.pack()


#create window to deposit into savings account#
class SavingsPage:
    def __init__(self):
        window = Tk()
        window.title("Savings Account")

        label = Label(window, text = "How much would you like to deposit?", font = PROMPT_FONT)
        label.pack()

        entrySavings = Entry(window)
        entrySavings.pack()

#create window to deposit into checking account#
class CheckingPage:
    def __init__(self):
        window = Tk()
        window.title("Checking Account")

        label = Label(window, text = "How much would you like to deposit?", font = PROMPT_FONT)
        label.pack()

        entryChecking = Entry(window)
        entryChecking.pack()
        
        window.mainloop()
BankManager()
