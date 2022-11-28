class Menu :
    if_manager = False #czy uzytkownik jest menager
    def show (self): #metoda, ktora wyswietla menu |self, - daje dostep do zmiennych spoza metody 
        print('Wybierz opcję:\n')
        print ('1. Wyloguj mnie,\n')
        print('2. Wybierz dzień do sprawdzenia,\n')
        print('3.Wybierz miesiąc, aby zrobić zestawienie,\n') #zestawienie- wypłata, nieobecności, spóźnienia, przebyte urlopy
        print('4.Lista urlopów,\n') #dostępne urlopy
        if self.if_manager == True:
            print ('5.Wybierz pracownika do sprawdzenia')

    def choose (self) : #Główna metoda, która służy do wyboru opcji w menu|self, - daje dostep do zmiennych spoza metody 
        while True:
            self.show()
            try:
                choice = int(input())
            except(ValueError):
                choice = 0

            if choice == 1:
                break
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5 and self.if_manager == True:
                pass
            else:
                print('Nie ma takiego wyboru! Wybierz jeszcze raz!')

        

        


