

#from requests import post, get, put, delate # Biblioteka request służy do łączenia się z API 
# get - pobieranie danych z serwera (odczyt)
#post - dodanie danych na serwer    (zapis)
#put - edycja danych na serwerze    (zmiana)
#delate - usunięcie danych na serwerze  (usunięcie)
class Menu :

    if_manager = False #czy uzytkownik jest menager

    """
    Metoda show służy do wyświetlenia głównego menu.
    """
    def show (self): #metoda, ktora wyswietla menu |self, - daje dostep do zmiennych spoza metody 
        print('Wybierz opcję:\n')
        print ('1. Wyloguj mnie,\n')
        print('2. Wybierz dzień do sprawdzenia,\n') #dokładny opis w metodzie GetDay
        print('3.Wybierz miesiąc, aby zrobić zestawienie,\n') #zestawienie- wypłata, nieobecności, spóźnienia, przebyte urlopy
        print('4.Lista urlopów,\n') #dostępne urlopy
        if self.if_manager == True:
            print ('5.Wybierz pracownika do sprawdzenia') #dokładny opis w metodzie showManagerMenu

    ############################################################
    """
    Metoda choose służy do obsługi głównej pętli programu.
    """
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

                self.getDay()
            elif choice == 3:
                self.getMonth()
            elif choice == 4:
                self.getLeaves()
            elif choice == 5 and self.if_manager == True:
                self.showManagerMenu()
            else:
                print('Nie ma takiego wyboru! Wybierz jeszcze raz!')

    ############################################################
    """
    Metoda getDay służy do wyboru dnia w celu sprawdzenia godzin z danego dnia.
    """
    def getDay (self):
        dateStr=input('Podaj datę. Format dd/mm/rrrr\n') #data w stringu
        dateArray=dateStr.split('/') #tablica 3-elementowa, [dzien,miesiac, rok]
        day=int(dateArray[0]) #zamiana 1 elementu ze string na int
        month=int(dateArray[1]) #zamiana 2 elementu ze string na int
        year=int(dateArray[2]) #zamiana 3 elementu ze string na int

        print('Pobieranie z serwera...')
        # Tutaj będzie wysyłanie requestu GET na serwer w celu podania dnia i uzyskania godzin przyjścia i wyjścia za ten dzień
        print('Pobrano:')
        # Tutaj będzie wyświetlanie tych godzin.

    ############################################################
    """
    Metoda getMonth służy do wyboru miesiąca w celu sporządzenia zestawienia i podania wysokości wypłaty.
    """
    def getMonth(self):
        dateStr=input('Podaj miesiąc i rok. Format mm/rrrr\n') #data w stringu
        dateArray=dateStr.split('/') #tablica 2-elementowa, [miesiac, rok]
        month=int(dateArray[0]) #zamiana 1 elementu ze string na int
        year=int(dateArray[1]) #zamiana 2 elementu ze string na int

        print('Pobieranie z serwera...')
        # Tutaj będzie wysyłanie requestu GET na serwer w celu podania miesiąca
        # i uzyskania godzin przyjścia i wyjścia przez cały miesiąc oraz stawki godzinowej
        print('Pobrano:')
        # Tutaj będzie wyświetlanie miesięcznego raportu oraz wyliczanie wysokości wypłaty.
    
    ############################################################
    """
    Metoda showManagerMenu służy do podmenu akcji menedżera.
    """
    def showManagerMenu(self):
        print('Pobieranie z serwera...')
        # Tutaj będzie wysyłanie requestu GET na serwer w celu 
        # uzyskania listy pracowników.
        print('Pobrano:')
        # Tutaj będzie wyświetlanie listy podwładnych.
        # Będzie możliwość wyboru podwładnego.
        # Po wybraniu pokazane zostaną opcje:
        # Raport miesięczny, możliwość edycji godzin w wybrany dzień, export pliku csv.

    ############################################################
    """
    Metoda getLeaves służy do podania dni urlopowych pracownikowi.
    """
    def getLeaves(self):
        print('Pobieranie z serwera...')
        # Tutaj będzie wysyłanie requestu GET na serwer w celu
        # uzyskania raportu zawierającego zaplanowane daty urlopów w tym roku.
        print('Pobrano:')
        # Tutaj będzie wyświetlanie raportu oraz wyliczanie ilości pozostałych dni urlopu.

