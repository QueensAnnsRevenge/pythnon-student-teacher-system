import dataBase as db
import mysql.connector
from mysql.connector import Error
import classes as clss
    

def main():

   ime = input("ime profesora: ")
   prezime = input("prezime profesora: ")



   db.unesi_profesora(clss.profesor(0 ,ime, prezime))

   lista_profesora = db.get_all_proffesors()

   for progesor in lista_profesora:
      print(progesor)


main()