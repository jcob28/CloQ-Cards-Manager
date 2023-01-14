from global_storage import GlobalStorage
from hashlib import md5
from requests import get, post #post - wysyłanie danych na serwer, get - odczyt danych z serwera

class Login :

    def logging (self, global_storage : GlobalStorage)->bool: #jesli wleci argument innego typu program wyrzuci wyjątek
        #self, - daje dostep do zmiennych spoza metody 
        #funkcja zwraca wartość typu bool
        print('Podaj login')
        login = input()
        print('Podaj hasło')
        passwd = input()

        # Gdyby chcieć haszować w apce:
        #passoword_bytes = passwd.encode() #encode zwraca bajty ze stringa password
        #md5_bites = md5(passoword_bytes).digest() #md5 wylicza md5 (hasz) z podanych bajtow, a digest zamienia obiekt md5 na bajty
        #passwd = int.from_bytes(md5_bites, 'big') #zamiana bajtow na inta, big oznacza ze najbardziej znaczacy bajt jest na początku
        #print(passwd)
        # metoda from_bytes która konwertuje bajty na inty

        payload = {"login":login,"password":passwd}
        r= post (global_storage.url + "v1/login", json=payload) #funkcja wysyłająca request HTTP post (wysłanie danych na serwer) 
        # 1 arg - gdzie to ma być wysłane, 2 arg - co ma być wysłane

        if r.status_code==200:
            print ('Zalogowano')
            global_storage.token = r.json ()['Token']

            r = get(global_storage.url + 'v1/users', headers=global_storage.getAuth())
            
            # Szukanie id pracownika:
            for entry in r.json():
                if entry['login'] == login:

                    global_storage.emp_id = int(entry['id'])
                    print("\nDzień dobry " + entry['first_name'] + " " + entry['last_name'] + "!\n")
                    break

            #print(global_storage.token) # DEBUG
            #if r.json ()['AccountType'] == 'Manager':
            #    global_storage.if_manager = True
            return True
        else:
            print("NIE zalogowano")
            return False