import mysql.connector
from mysql.connector import Error
import classes as clss



def connection_open():
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='dusan')
    if connection.is_connected():
        cursor = connection.cursor()
        return cursor, connection

def connection_close(cursor, connection):
    if connection.is_connected():
        cursor.close()
        connection.close()






#Unosenje osnovnih podataka


def unesi_studenta(student):

    cursor,connection = connection_open();
    data = (student.ime, student.prezime)
    query = "INSERT INTO student  (student_Ime, student_prezime) VALUES ( %s,  %s)"
    try:
        cursor.execute(query, data)
        connection.commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)


def unesi_predmet(predmet):
    
    cursor, connection = connection_open()

    data = (predmet.naziv, predmet.broj_ESPB)
    query = "INSERT INTO predmet (naziv_predmeta, broj_ESPB_bodova) VALUES (%s, %s)"
    try:
        cursor.execute(query, data)
        connection.commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)


def unesi_profesora(profesor):

    cursor,connection = connection_open()
    data = (profesor.ime, profesor.prezime)
    query = "INSERT INTO profesor (profesor_ime, profesor_prezime) VALUES (%s, %s)"
    try:
        #upisivanje profesora u bazu
        cursor.execute(query, data)
        connection.commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)

def unesi_ispit(ispit):

    cursor, connection = connection_open()
    query = "INSERT INTO ispit (predmet_idpredmet, profesor_idprofesor, datum) VALUES (%s, %s, %s)"
    data = ( ispit.profesor.id, ispit.predmet.id, ispit.datum)
    
    try:
        cursor.execute(query, data)
        connection.commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)












# ZASO U OVOJ METODI UZIMAMO I PREDMETID I STUDENTID????

def get_predmet_i_student_id(student, predmet):

    cursor, connection = connection_open()
    query_student = "SELECT idStudent FROM student WHERE student_ime = %s AND  student_prezime LIKE %s"
    querry_predemt = "SELECT idPredmet FROM predmet WHERE naziv_predmeta LIKE %s AND broj_ESPB_bodova LIKE %s"
    try:
        # uzizamo id studenta 
        cursor.execute(query_student,(student.ime, student.prezime))
        student_id = cursor.fetchall()
        # uzizamo id predmeta
        cursor.execute(querry_predemt, (predmet.naziv, predmet.broj_ESPB))
        predmet_id = cursor.fetchall()
        # Iz nekog razloga dobijam listu u nizu pa moram ovako da vracam vrednosti 
        
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)
        # Iz nekog razloga dobijam listu u nizu pa moram ovako da vracam vrednosti
        return (student_id[0][0], predmet_id[0][0])
    

def upis_na_predmet(student, predmet):

    ids = get_predmet_i_student_id(student, predmet)
    cursor,connection = connection_open()
    query = "INSERT INTO student_has_predmet (student_idStudent, predmet_idPredmet) VALUES (%s, %s)"
    try:
        cursor.execute(query, (ids[0], ids[1]))
        connection.commit()
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)


def get_predmet(predmet_id):

    cursor, connection = connection_open()
    query = "SELECT * FROM predmet WHERE idPredmet LIKE %s"
    predmet = ""
    try:
        cursor.execute(query,(predmet_id,))
        predmet_list = cursor.fetchall()
        predmet = clss.predmet(predmet_list[0][1], predmet_list[0][2])
        
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)
        return predmet


def get_profesor(profesor_id):

    cursor, connection = connection_open()
    query = "SELECT * FROM profesor WHERE idProfesor LIKE %s"
    profesor = ""
    try:
        cursor.execute(query, (profesor_id,))
        profesor_list = cursor.fetchall()
        profesor = clss.profesor(profesor_list[0][1], profesor_list[0][2])
        
    except Error as e:
        print("Erroer: ", e)
    finally:
        connection_close(cursor, connection)
        return profesor

def get_student(student_id):

    cursor, connection = connection_open()
    query = "SELECT * FORM profesor WHERE idStudent LIKE %s"
    try:
        cursor.execute(query, (student_id, ))
        student_list = cursor.fetchall()
        student = clss.pstudent(student_list[0][1], student_list[0][2])
        
    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)
        return student
    
def get_ispit(ispit_id):

    cursor, connection = connection_open()
    query = "SELECT * FROM ispit WHERE idispit LIKE %s"
    ispit_raw = ""

    try:
        cursor.execute(query, (ispit_id, ))
        ispit_raw = cursor.fetchall()
    
    except Error as e:
        print("Error: ", e)

    finally:
        connection_close(cursor, connection)
        return ispit_raw

       

def get_sve_studente():
    cursor, connection = connection_open()
    query = "SELECT * FROM student"

    try:
        cursor.execute(query)
        students = cursor.fetchall()
    except Error as e:
        print("Error: ", e)

    students_list = []
    
    for x in students:
        students_list.append(clss.student(x[0],x[1],x[2]))

    connection_close(cursor, connection)
    return students_list


def get_sve_profesore():
    cursor, connection = connection_open()
    query = "SELECT * FROM profesor"

    try:
        cursor.execute(query)
        profesori = cursor.fetchall()
    except Error as e:
        print("Error: ", e)

    proffesor_list = []
    
    for x in profesori:
        proffesor_list.append(clss.profesor(x[0], x[1], x[2]))

    connection_close(cursor, connection)
    return proffesor_list


def get_sve_predmete():
    cursor, connection = connection_open()
    query = "SELECT * FROM predmet"

    try:
        cursor.execute(query)
        predmeti = cursor.fetchall()
    except Error as e:
        print("Error: ", e)

    predmet_list = []
    
    for x in predmeti:
        predmet_list.append(clss.predmet(x[0], x[1], x[2]))

    connection_close(cursor, connection)
    return predmet_list



def get_sve_ispite():
        cursor, connection = connection_open()
        query = "SELECT * FROM ispit"

        try:
            cursor.execute(query)
            ispiti = cursor.fetchall()
        except Error as e:
            print("Error: ", e)

        ispiti_list = []
    
        for x in ispiti:
            ispiti_list.append(clss.ispit(x[0],x[1],x[2]))

        connection_close(cursor, connection)
        return ispiti_list

    

def upis_ocene(student, ispit, ocena):

    cursor, connection = connection_open()
    query = "INSERTI INTO  student_hes_ispit (student_idstudent, ispit_idispit, ocena) VALUES  (%s, %s, %s)"
    data = (student.id, ispit.id, ocena)

    try:
        cursor.execute(query, data)
        connection.commit()

    except Error as e:
        print("Error: ", e)
    finally:
        connection_close(cursor, connection)


def svi_ispiti_studenta(student):

    cursor, connection = connection_open()
    query = "SELECT * FROM student_has_ispit WHERE student_idstudent LIKE %s"
    data = (student.id, )
    ispiti = ""

    try:
        cursor.execute(query,data)
        ispiti = cursor.fetchall()

    except Error as e:
        print("Error: ", e)

    finally:
        connection_close(cursor, connection)
        
        for ispit in ispiti:
            print(ispit)

        return ispiti
    




