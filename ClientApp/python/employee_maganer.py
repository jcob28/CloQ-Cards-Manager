from global_storage import GlobalStorage
from requests import post, get, put, delete # Biblioteka request służy do łączenia się z API 

"""
IMPORTANT! Moduł managera miał być napisany, ale nie starczyło na to czasu. Nie jest on jeszcze działający,
stąd został wyłączony. Uznajemy, że to firma informatyczna i managerowie umieją korzystać z systemu używając
np. Postmana (współczuję im pracy).
"""

class EmpolyeeManager:

    def __init__(self, global_storage: GlobalStorage, employeeId: int) -> None:

        self.gs = global_storage
        self.id = employeeId

    ############################################################

    def optionString(self) -> str:

        return """\
        1. Wybierz dzień dla pracownika (sprawdzenie godzin, edycja),
        2. Wybierz miesiąc (zestawienie),
        3. Pokaż urlopy (akceptacja).
        """

    ############################################################

    def choose(self) -> None:

        try:
            choice = int(input())
        except(ValueError):
            choice = 0
        
        if choice == 1:
            self.dayManagerView()
        elif choice == 2:
            self.monthManagerView()
        elif choice == 3:
            self.dayManagerView()
        else:
            return

    ############################################################

    def dayManagerView(self) -> None:

        dateStr=input('Podaj datę. Format dd/mm/rrrr\n') #data w stringu
        dateArray=dateStr.split('/') #tablica 3-elementowa, [dzien,miesiac, rok]
        day=int(dateArray[0]) #zamiana 1 elementu ze string na int
        month=int(dateArray[1]) #zamiana 2 elementu ze string na int
        year=int(dateArray[2]) #zamiana 3 elementu ze string na int

        print('Pobieranie z serwera...')

        # Tutaj jest wysyłanie requestu GET na serwer w celu podania dnia i uzyskania godzin przyjścia i wyjścia za ten dzień
        payload = {'EmployeeId':self.id,"day":day,"month":month, 'year':year}
        r = get(self.gs.url + 'employee/meatday', auth='Authorization: Token token='+str(self.gs.token), json=payload)
        #arriveTime = 0
        #departureTime = 0
        registers = r.json () ['registers']
        for register in registers :
            print('Czas wejścia: ' + str(register['TimeIn']))
            print('Czas wyjścia: ' + str(register['TimeOut']))
        print('Pobrano:')
        # Tutaj będzie wyświetlanie tych godzin.

    ############################################################

    def monthManagerView(self) -> None:

        dateStr=input('Podaj miesiąc i rok. Format mm/rrrr\n') #data w stringu
        dateArray=dateStr.split('/') #tablica 2-elementowa, [miesiac, rok]
        month=int(dateArray[0]) #zamiana 1 elementu ze string na int
        year=int(dateArray[1]) #zamiana 2 elementu ze string na int

        print('Pobieranie z serwera...')
        # Tutaj jest wysyłanie requestu GET na serwer w celu podania miesiąca
        # i uzyskania godzin przyjścia i wyjścia przez cały miesiąc oraz stawki godzinowej
        payload = {'EmployeeId':self.id,'month':month, 'year':year}
        r = get(self.gs.url + 'employee/month', auth='Authorization: Token token='+str(self.gs.token), json=payload)
        #arriveTime = 0
        #departureTime = 0
        dni =[None] * 31
        registers = r.json () ['registers']
        for register in registers :
            dayIn = register['DateIn']
            dni [dayIn] = []
            dni [dayIn].append (register['TimeIn'])
            dni [dayIn].append (register['TimeOut'])
        for i in range (0,31):
            if dni[i] != None:
                print(str(i+1) + dni[i])

        print('Pobrano:')
        # Tutaj będzie wyświetlanie miesięcznego raportu oraz wyliczanie wysokości wypłaty.

    ############################################################

    def vacationManagerView(self) -> None:

        dateStr=input('Podaj rok.\n') #data w stringu
        year=int(dateStr) #zamiana ze string na int

        print('Pobieranie z serwera...')

        # Tutaj jest wysyłanie requestu GET na serwer w celu
        # uzyskania raportu zawierającego zaplanowane daty urlopów w tym roku.
        payload = {'EmployeeId':self.id,'year':year}
        r = get(self.gs.url + 'employee/leaves', auth='Authorization: Token token='+str(self.gs.token), json=payload)
        leaves = r.json () ['leaves']

        # Tutaj jest wyświetlanie raportu oraz wyliczanie ilości pozostałych dni urlopu.

        for leaves in leaves :
            print('Początek urlopu: ' + str(leaves['StartDate']))
            print('Koniec urlopu: ' + str(leaves['EndDate']))
            print('Rodzaj urlopu: ' + str(leaves['LeaveType']))
            print('Zgoda na urlop: ' + str(leaves['Decision']))
        print('Pobrano:')