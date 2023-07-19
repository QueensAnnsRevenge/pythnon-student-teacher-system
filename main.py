import dataBase as db
import classes as clss
    

def main():
    
    studenti = db.get_all_students()

    print("Izaberi studenta ")
    i = 1
    for student in studenti:
        print(student)
        i = i + 1

    br = int(input("unesite redni broj studenta: "))

    br = br - 1

main()