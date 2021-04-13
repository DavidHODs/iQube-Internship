import time
from datetime import datetime as dt

now = dt.now()
month = now.strftime('%B')
day = now.strftime('%B %d')

inflow = {}
outflow = {}
balance = {}


class revenue():
    '''A class on sources of revenue income and expected revenue values'''

    def __init__(self, salary, trustfund, gigs, totalInflow):
        self.salary = salary
        self.trustfund = trustfund
        self.gigs = gigs
        self.totalInflow = totalInflow

    def inflow(self):
        self.salary = int(input('\nInput your monthly salary in digits\n$ '))
        self.trustfund = int(input('\nGot any trust fund set up by your folks.'
                                   ' Input the amount in didgits\n$ '))
        self.gigs = int(
            input('\nInput your estimated expected gigs inflow in digits\n$ '))
        self.totalInflow = self.salary + self.trustfund + self.gigs
        inflow = {'Salary': self.salary, 'Trust Fund': self.trustfund, 'Gigs': self.gigs,
                  'Total Inflow': self.totalInflow}
        print(
            f'\nYour total expected capital inflow for the month of {month} is ${self.totalInflow}\n')
        time.sleep(2)
        print(f'\nHere is the break down of your total expected cash inflow for the month of {month}:'
              f' {inflow}\n')
        time.sleep(5)


class expenses():
    '''A class on budgeted expenses'''

    def __init__(self, food, rent, clothe, gift, others, totalOutflow):
        self.food = food
        self.rent = rent
        self.clothe = clothe
        self.gift = gift
        self.others = others
        self.totalOutflow = totalOutflow

    def target(self):
        print('Input how much you want to set aside for the following categories of expenses\n')
        time.sleep(2)
        self.food = int(input('Food: $'))
        self.rent = int(input('\nRent: $'))
        self.clothe = int(input('\nClothe: $'))
        self.gift = int(input('\nGift: $'))
        self.others = int(input('\nOthers: $'))

    def outflow(self):
        self.totalOutflow = self.food + self.rent + \
            self.clothe + self.gift + self.others
        outflow = {'Food': self.food, 'Rent': self.rent, 'Clothe': self.clothe, 'Gift': self.gift,
                   'Others': self.others, 'Total Outflow': self.totalOutflow}
        print(
            f'\nYour total expected cash outflow for the month of {month} is ${self.totalOutflow}\n')
        time.sleep(2)
        print(f'\nHere is the break down of your total expected cash outflow for the month of {month}:'
              f' {outflow}\n')
        time.sleep(5)


class initialization(revenue, expenses):
    '''A class to initialize, run the app and give analysis of the budget'''

    def __init__(self):
        self = self

    def coloredText(self, text):
        print('\033[95m{}\033[00m'.format(text))

    def initialization(self):
        self.coloredText('                 Money Tracker')
        self.coloredText(
            '******Number one budget construction app in Africa******')
        time.sleep(3)
        self.coloredText(f'\nBudget design for the month of {month}')
        self.inflow()
        self.target()
        self.outflow()
        self.operators()

    def operators(self):
        deficit = self.totalInflow - self.totalOutflow
        if self.totalInflow > self.totalOutflow:
            print(f"\nIf you stay true to your budget for the month of {month}, you'll have a balance of ${deficit}."
                  " We advise you to invest it in crypto coins on Binance. By the way we'll soon launch a trading feature")
            " on this app."
            time.sleep(6)
            self.test()
        if self.totalInflow < self.totalOutflow:
            print(f'\nYour expenses are greater than your cash inflow. You will have to source for extra ${deficit}'
                  ' or cut down your expenses')
            decision = int(input('\n Would you like to reset your budget or you go roff am?\n'
                                 'Input 1 to reset     2 to roff it out\n'))
            if decision == 1:
                self.initialization()
            if decision == 2:
                print(
                    f'God speed. If you survive the month of {month}, please gist us on how you did it.')
        if self.totalInflow == self.totalOutflow:
            print('\nYour budget will work but plenty sapa go dey')
            time.sleep(3)
            self.test()
        time.sleep(6)

    def test(self):
        print(f'\nExpenses Logging for {day}')
        time.sleep(2)
        print('\nInput how much you spent today for the following categories\n')
        time.sleep(2)
        exFood = int(input('\nFood: $'))
        exRent = int(input('\nRent: $'))
        exClothe = int(input('\nClothe: $'))
        exGift = int(input('\nGift: $'))
        exOthers = int(input('\nOthers: $'))
        exTotal = exFood + exRent + exClothe + exGift + exOthers
        balTotal = self.totalOutflow - exTotal
        balance = {'Food': self.food - exFood, 'Rent': self.rent - exRent, 'Clothe': self.clothe - exClothe,
                   'Gift': self.gift - exGift, 'Others': self.others - exOthers,
                   'Total Outflow': self.totalOutflow - exTotal}
        time.sleep(2)
        print(f'\nYou spent a total of {exTotal} today. You have a budgeted fund of ${balTotal} left'
              f' for the month of {month}')
        time.sleep(5)
        print('\nWould you like to transfer budgeted froms from one category to another?')
        inp = int(input('Input in digit: 1. Yes    2. No'))
        if inp == 1:
            self.transfer()
        if inp == 2:
            print(f'\nHere is the break down of your total remaining budgeted cash for expenses for the month of {month}:'
                  f' {balance}\n')
            time.sleep(5)

    def transfer(self):
        print('\nHow much would you like to transfer\n')
        amount = int(input('$\n'))
        print(
            '\nFrom which category will you like to withdraw this amount? Input a digit\n')
        category = int(
            input('1. Food   2. Rent   3. Clothe   4. Gift   5. Others\n'))
        if category == 1:
            tr = self.food
        elif category == 2:
            tr = self.rent
        elif category == 3:
            tr = self.clothe
        elif category == 4:
            tr = self.gift
        elif category == 5:
            tr = self.others
        print('\nTo which category will you like to transfer this amount? Input a digit\n')
        cat = int(input('1. Food   2. Rent   3. Clothe   4. Gift   5. Others\n'))
        if cat == 1:
            cr = self.food
        elif cat == 2:
            cr = self.rent
        elif cat == 3:
            cr = self.clothe
        elif cat == 4:
            cr = self.gift
        elif cat == 5:
            cr = self.others
        if amount > tr:
            print(f"You didn't budget up to this amount in {tr}.")
            time.sleep(2)
            self.transfer()
        else:
            print(f'Transfer succesful. You now have a budget of ${tr - amount} left for {tr} and ${cr + amount}'
                  f' for {cr}')
            print(f'\nHere is the break down of your total remaining budgeted cash for expenses for the month of {month}:'
                  f' {balance}\n')
            time.sleep(3)


ego = initialization()
ego.initialization()
