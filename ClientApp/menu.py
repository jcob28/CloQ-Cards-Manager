from global_storage import GlobalStorage
from employee_maganer import EmpolyeeManager
import os

from requests import post, get, put, delete # Biblioteka request służy do łączenia się z API
# get - pobieranie danych z serwera     (odczyt)
# post - dodanie danych na serwer       (zapis)
# put - edycja danych na serwerze       (zmiana)
# delate - usunięcie danych na serwerze (usunięcie)
class Menu :

    def __init__(self, global_storage: GlobalStorage):
        self.gs = global_storage

    """
    Metoda show służy do wyświetlenia głównego menu.
    """
    def show (self) -> str: #metoda, ktora wyswietla menu |self, - daje dostep do zmiennych spoza metody
        optionsStr="""Wybierz opcję:\n
        1. Wyloguj mnie,\n
        2. Wybierz dzień do sprawdzenia,\n
        3. Wybierz miesiąc, aby zrobić zestawienie,\n
        4. Lista urlopów,\n"""
        if self.gs.if_manager == True:
            optionsStr += '5.Wybierz pracownika do sprawdzenia' #dokładny opis w metodzie showManagerMenu

        return optionsStr

    ############################################################
    """
    Metoda choose służy do obsługi głównej pętli programu.
    """
    def choose (self) : #Główna metoda, która służy do wyboru opcji w menu|self, - daje dostep do zmiennych spoza metody

        self.clearTerm()

        while True:
            print(self.show())
            try:
                choice = int(input())
            except(ValueError):
                choice = 0

            if choice == 1:
                self.clearTerm()
                print("Do widzienia!")
                break

            elif choice == 2:
                self.clearTerm()
                self.getDay()

            elif choice == 3:
                self.clearTerm()
                self.getMonth()

            elif choice == 4:
                self.clearTerm()
                self.getLeaves()

            elif choice == 5 and self.gs.if_manager == True:
                self.showManagerMenu() # Nie skończone, wyłączone

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

        print('\nPobieranie z serwera...\n')

        # Tutaj jest wysyłanie requestu GET na serwer w celu podania dnia i uzyskania godzin przyjścia i wyjścia za ten dzień
        r = get(self.gs.url + 'v1/registers', headers=self.gs.getAuth())

        for entry in r.json():
            if entry['employee_id'] == self.gs.emp_id:
                if entry['date_in'] == str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2):

                    print('Czas wejścia: ' + str(entry['time_in']))
                    print('Czas wyjścia: ' + str(entry['time_out']))

                    t_in  = self.getTimeFromTimeStr(entry['time_in'])
                    t_out = self.getTimeFromTimeStr(entry['time_out'])
                    print("Przepracowano: " + self.min2hAndMin(t_out - t_in) + ".\n")

    ############################################################
    """
    Metoda getMonth służy do wyboru miesiąca w celu sporządzenia zestawienia i podania wysokości wypłaty.
    """
    def getMonth(self):

        dateStr=input('Podaj datę. Format mm/rrrr\n') #data w stringu
        dateArray=dateStr.split('/') #tablica 3-elementowa, [dzien,miesiac, rok]
        month=int(dateArray[0]) #zamiana 1 elementu ze string na int
        year=int(dateArray[1]) #zamiana 2 elementu ze string na int

        print('\nPobieranie z serwera...\n')

        # Tutaj jest wysyłanie requestu GET na serwer w celu podania dnia i uzyskania godzin przyjścia i wyjścia za ten dzień
        r = get(self.gs.url + 'v1/registers', headers=self.gs.getAuth())

        sum = 0
        for entry in r.json():
            if entry['employee_id'] == self.gs.emp_id:
                if str(year) + '-' + str(month).zfill(2) in entry['date_in']:

                    t_in  = self.getTimeFromTimeStr(entry['time_in'])
                    t_out = self.getTimeFromTimeStr(entry['time_out'])

                    print("Dnia " + entry['date_in'] + " przepracowano: " + self.min2hAndMin(t_out - t_in) + ".")
                    sum += t_out - t_in

        print("\nŁącznie w miesiącu przepracowano: " + self.min2hAndMin(sum) + ".\n")

    ############################################################
    """
    Metoda showManagerMenu służy do podmenu akcji menedżera.

    IMPORTANT! Moduł managera miał być napisany, ale nie starczyło na to czasu. Nie jest on jeszcze działający,
    stąd został wyłączony. Uznajemy, że to firma informatyczna i managerowie umieją korzystać z systemu używając
    np. Postmana (współczuję im pracy).
    """
    def showManagerMenu(self):
        print('Pobieranie z serwera...')
        r = get(self.gs.url + 'employee/listformanager', auth='Authorization: Token token='+str(self.gs.token))
        # Tutaj jest wysyłanie requestu GET na serwer w celu
        # uzyskania listy pracowników.
        print('Pobrano:')
        employees = r.json () ['employees']
        for employee in employees :
            print('ID pracownika: ' + str(employee['EmployeeId']))
            print('Imię pracownika: ' + str(employee['FirstName']))
            print('Nazwisko pracownika: ' + str(employee['LastName']))
        # Tutaj jest wyświetlanie listy podwładnych.
        # Będzie możliwość wyboru podwładnego.

        choosenEmployee = input('Wybierz id pracownika: ')

        employeeManager = EmpolyeeManager(self.gs, choosenEmployee)
        print(employeeManager.optionString())
        employeeManager.choose()

        # Po wybraniu pokazane zostaną opcje:
        # Raport miesięczny, możliwość edycji godzin w wybrany dzień, export pliku csv.

    ############################################################
    """
    Metoda getLeaves służy do podania dni urlopowych pracownikowi.
    """
    def getLeaves(self):

        print('\nPobieranie z serwera...\n')

        # Tutaj jest wysyłanie requestu GET na serwer w celu podania dnia i uzyskania godzin przyjścia i wyjścia za ten dzień
        r = get(self.gs.url + 'v1/vacations', headers=self.gs.getAuth())
        count = 0

        for entry in r.json():
            if entry['employee_id'] == self.gs.emp_id:

                print("Rodzaj urlopu: " + entry['vacation_type'])
                print("Od " + entry['start_date'] + " do " + entry['end_date'] + ".")

                if entry['decision']:
                    print('Zatwierdzony\n')
                    count += 1
                else:
                    print('Niezatwierdzony\n')

        print("Zatwierdzonych urlopów: " + str(count) + ".")

    ############################################################

    """
    Metoda getTimeFromTimeStr służy do przetworzenia pobranego czasu na minuty.
    String postaci: 2000-01-01T15:00:00.000Z,
    Postać docelowa: 15*3600 + 0*60 + 0.
    """
    def getTimeFromTimeStr(self, timeStr: str) -> int:

        timeTab = timeStr.split('T')[1].split(':')
        return int(timeTab[0]) * 60 + int(timeTab[1])

    ############################################################

    """
    Metoda min2hAndMin służy do zamiany minut na czas w godzinach i minutach.
    """
    def min2hAndMin(self, minutes: int) -> str:

        return str(int(minutes/60)) + 'h ' + str(minutes%60) + 'min'

    ############################################################

    """
    Metoda clearTerm służy do czyszczenia terminala. Wywołuje:
    - cls na Windowsie,
    - clear na Linuxie / Macu / Unixie.
    """
    def clearTerm(self):

        os.system('cls' if os.name == 'nt' else 'clear')