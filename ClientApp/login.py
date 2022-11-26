from global_storage import GlobalStorage
class Login :
    temp_username = 'user123'
    temp_password = 'haslo123'

    def logging (self, global_storage : GlobalStorage)->bool: #jesli wleci argument innego typu program wyrzuci wyjątek
        #self, - daje dostep do zmiennych spoza metody 
        #funkcja zwraca wartość typu bool
        print('Podaj login')
        global_storage.login=input()
        print('Podaj hasło')
        global_storage.password=input()
        if self.temp_username == global_storage.login and self.temp_password == global_storage.password:
            print ('Zalogowano')
            return True
        else:
            print("NIE zalogowano")
            return False



    
