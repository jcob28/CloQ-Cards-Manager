#struktura przechowująca zmienne globalne 

#docelowo przechowywany będzie tylko tokens
class GlobalStorage:

    token = ''
    emp_id = 0
    url = 'http://127.0.0.1:3000/'
    if_manager = False

    def getAuth(self) -> dict:

        return {"Authorization": "Bearer " + self.token}