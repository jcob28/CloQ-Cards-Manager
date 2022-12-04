#!/usr/bin/python3
from global_storage import GlobalStorage
from login import Login
from menu import Menu

if __name__ == '__main__': #Aby nie można było go dołączyć do innych plików, bo to główny plik
    global_storage = GlobalStorage() #stworzenie obiektu (zmienna posiadajaca atrybuty i metody danej klasy)
    login = Login ()
    menu = Menu ()
    while True:
        if login.logging(global_storage) == True :
            break
    menu.choose ()
        
#exit(0) - wychodzi z programu
