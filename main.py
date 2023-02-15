import dataBase as db
import mysql.connector
from mysql.connector import Error
import classes as clss
    

def main():
    
    ime = input("ime profesora: ")
    prezime = input("prezime profesora:")

    profa = clss.profesor(0 ,ime, prezime)

    db.unesi_profesora(profa)

    



    


main()