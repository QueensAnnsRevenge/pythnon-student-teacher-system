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
        return f"{self.naziv}({self.broj_ESPB})"

class profesor:

    def __init__(self, id, ime, prezime):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        

    def __str__(self) -> str:
        return f"{self.ime} {self.prezime}"



class ispit:

    def __init__(self, ocena, student_id, predmet_id):
        self.ocena = ocena
        self.student = db.get_student(student_id)
        self.predmet = db.get_predmet(predmet_id)


    def __str__(self) -> str:
        return f"{self.ocena}"