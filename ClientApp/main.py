#!/usr/bin/python3
from global_storage import GlobalStorage
from login import Login
from menu import Menu


"""
Aplikacja kliencka systemu generowania kart czasu pracy.
Program docelowo będzie łączył się z API aplikacji serwerowej za pomocą biblioteki requests.
Aktualnie program pozwala na zalogowanie się zahardcodowanymi danymi (wpisanymi na stałe),
ale już hashuje wpisane hasło.
"""

if __name__ == '__main__': #Aby nie można było go dołączyć do innych plików, bo to główny plik
    global_storage = GlobalStorage() #stworzenie obiektu (zmienna posiadajaca atrybuty i metody danej klasy)
    login = Login ()
    menu = Menu (global_storage)

    while True: #Pętla, która powtarza logowanie, w razie niepowodzenia
        if login.logging(global_storage) == True :
            break
    menu.choose ()
        
#exit(0) - wychodzi z programu
