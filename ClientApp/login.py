from global_storage import GlobalStorage
from hashlib import md5
class Login :
    temp_username = 'user123'
    temp_password = 35223524413618242205997641121151244752 #haslo123

    def logging (self, global_storage : GlobalStorage)->bool: #jesli wleci argument innego typu program wyrzuci wyjątek
        #self, - daje dostep do zmiennych spoza metody 
        #funkcja zwraca wartość typu bool
        print('Podaj login')
        global_storage.login=input()
        print('Podaj hasło')
        global_storage.password=input()


        passoword_bytes = global_storage.password.encode() #encode zwraca bajty ze stringa password
        md5_bites = md5(passoword_bytes).digest() #md5 wylicza md5 (hasz) z podanych bajtow, a digest zamienia obiekt md5 na bajty
        global_storage.password = int.from_bytes(md5_bites, 'big') #zamiana bajtow na inta, big oznacza ze najbardziej znaczacy bajt jest na początku
        #print(global_storage.password)
        # metoda from_bytes która konwertuje bajty na inty
        if self.temp_username == global_storage.login and self.temp_password == global_storage.password:
            print ('Zalogowano')
            return True
        else:
            print("NIE zalogowano")
            return False