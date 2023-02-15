import dataBase as db

class student:
    def __init__(self, id ,ime, prezime):
        self.id = id
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        return f"{self.ime} {self.prezime}"


class predmet:

    def __init__(self, id, naziv, broj_ESPB):
        self.id = id
        self.naziv = naziv
        self.broj_ESPB = broj_ESPB
        

    def __str__(self) -> str:
        return f"{self.id} {self.naziv}({self.broj_ESPB})"

class profesor:

    def __init__(self, id, ime, prezime):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        

    def __str__(self) -> str:
        return f"{self.id} {self.ime} {self.prezime}"



class ispit:

    def __init__(self, id, profesor, predmet, datum):
        self.id = id
        self.profesor = profesor
        self.predmet = predmet
        self.datum = datum


    def __str__(self) -> str:
        return f"Predmet: {self.predmet}, Profesor: {self.profesor}"
    
    def get_profesor(self):
        return self.profesor
    
    def get_predmet(self):
        return self.predmet