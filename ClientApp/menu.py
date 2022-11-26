class Menu :
    if_manager = False #czy uzytkownik jest menager
    def show (self): #metoda, ktora wyswietla menu |self, - daje dostep do zmiennych spoza metody 
        print('Wybierz opcję:\n')
        print ('1. Wyloguj mnie,\n')
        print('2. Wybierz dzień do sprawdzenia,\n')
        print('3.Wybierz miesiąc, aby policzyć miesięczny czas pracy,\n')
        print('4.Lista urlopów,\n')
        if self.if_manager == True:
            print ('5.Wybierz pracownika do sprawdzenia')

    def choose (self) : #Główna metoda, która służy do wyboru opcji w menu|self, - daje dostep do zmiennych spoza metody 
        pass


