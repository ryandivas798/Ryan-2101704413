class Vending_Machine():
        def __init__(self, milo, pepsi, indomilk, aqua, fruit_tea):
            self.milo = str('Milo')
            self.pepsi = str('Pepsi')
            self.indomilk = str('Indomilk')
            self.aqua = str('Aqua')
            self.fruit_tea = str('Fruit Tea')
        def choice(self):
            x = str(input('Available Drink Choices : (Milo/Pepsi/Indomilk/Aqua/Fruit Tea)\n Your Choice Of Edible Minerals : ')).title()
            while True:
                if x == 'Milo':
                    print('You have chosen Milo(Pops out Milo from vending machine)')

                elif x == 'Pepsi':
                    print('You have chosen Pepsi(Pops Pepsi out from vending machine)')

                elif x == 'Indomilk':
                    print('You have chosen Indomilk(Pops Indomilk out from vending machine)')

                elif x == 'Aqua':
                    print('You have chosen Aqua(Pops Aqua out from vending machine)')

                elif x == 'Fruit Tea':
                    print('You have chosen Fruit Tea(Pops Fruit Tea out from vending machine)')


                print('Do you wish to choose a different drink?\n Yes or No')
                y = str(input(':')).title()
                while True:
                    if y == 'Yes':
                     choose.choice()
                    elif y == 'No':
                        print('Thank you for buying a drink! Come again next time')
                        exit()
                    else:
                        print('You must either be brain dead or stupid')
                        exit()

choose = Vending_Machine('','','','','')
choose.choice()

